#!/usr/bin/env python3
# [OUTDATED / 非推奨] このスクリプトは実験的な中間生成用です。
# PDF生成には tools/build_pdf.py (Pandoc → XeLaTeX) を使用してください。
"""Generate PDF from concatenated manuscript chapters with math rendering."""
import glob, os, re, subprocess, tempfile, base64, sys

print("=" * 70, file=sys.stderr)
print("[ERROR] このスクリプト (generate_pdf.py) は非推奨です。", file=sys.stderr)
print("        PDF生成には tools/build_pdf.py を使用してください。", file=sys.stderr)
print("=" * 70, file=sys.stderr)
sys.exit(1)

# --- Chapter order ---
files = []
for prefix in ['preface', 'toc']:
    f = f'manuscript/ja/{prefix}.md'
    if os.path.exists(f):
        files.append(f)
for i in range(1, 12):
    f = f'manuscript/ja/ch{i:02d}/ch{i:02d}.md'
    if os.path.exists(f):
        files.append(f)
for suffix in ['afterword', 'references']:
    f = f'manuscript/ja/{suffix}.md'
    if os.path.exists(f):
        files.append(f)


def strip_yaml(content):
    if content.startswith('---'):
        end = content.find('---', 3)
        if end > 0:
            return content[end+3:].lstrip()
    return content


all_parts = []
for f in files:
    with open(f) as fh:
        content = fh.read()
    content = strip_yaml(content)
    all_parts.append(content)
    all_parts.append('\n\n<div class="page-break"></div>\n\n')

md_text = '\n'.join(all_parts)

# Write intermediate markdown
os.makedirs('exports', exist_ok=True)
with open('exports/manuscript_combined.md', 'w') as f:
    f.write(md_text)


# --- Math rendering pipeline ---
# Step 1: Extract all math, replace with safe placeholders
MATH_PLACEHOLDER = 'MATHPLACEHOLDER'
display_exprs = {}   # placeholder -> (body, is_display)
inline_exprs = {}

def replace_display(m):
    placeholder = f'%%{MATH_PLACEHOLDER}_D{len(display_exprs)}%%'
    display_exprs[placeholder] = (m.group(1).strip(), True)
    return placeholder + '\n\n'

def replace_inline(m):
    placeholder = f'%%{MATH_PLACEHOLDER}_I{len(inline_exprs)}%%'
    inline_exprs[placeholder] = (m.group(1).strip(), False)
    return placeholder

text = re.sub(r'\$\$(.+?)\$\$', replace_display, md_text, flags=re.DOTALL)
text = re.sub(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', replace_inline, text)

all_exprs = list(display_exprs.values()) + list(inline_exprs.values())
print(f'Math expressions: {len(all_exprs)} total')

# Deduplicate
dedup = {}
unique_exprs = []
for body, is_display in all_exprs:
    key = (body, is_display)
    if key not in dedup:
        dedup[key] = len(unique_exprs)
        unique_exprs.append((body, is_display))

if not unique_exprs:
    print('No math expressions found')
else:
    print(f'Unique math expressions: {len(unique_exprs)}')

    # Step 2: Build batch LaTeX document
    latex_parts = [
        r'\documentclass[multi=preview,border=1pt,varwidth]{standalone}',
        r'\usepackage{amsmath,amssymb,bm,mathtools}',
        r'\usepackage[OT1]{fontenc}',
        r'\begin{document}',
    ]
    for body, is_display in unique_exprs:
        latex_parts.append(r'\begin{preview}')
        if is_display:
            latex_parts.append(r'\[%s\]' % body)
        else:
            latex_parts.append(r'$%s$' % body)
        latex_parts.append(r'\end{preview}')
    latex_parts.append(r'\end{document}')
    latex_doc = '\n'.join(latex_parts)

    # Step 3: Compile batch xelatex -> XDV -> SVG pages
    with tempfile.TemporaryDirectory() as tmpdir:
        tex_path = os.path.join(tmpdir, 'batch.tex')
        xdv_path = os.path.join(tmpdir, 'batch.xdv')

        with open(tex_path, 'w') as f:
            f.write(latex_doc)

        print('Compiling LaTeX...')
        r = subprocess.run(
            ['xelatex', '-no-pdf', '-interaction=nonstopmode',
             '-output-directory=' + tmpdir, tex_path],
            capture_output=True, cwd=tmpdir, timeout=180
        )
        if not os.path.exists(xdv_path):
            print('ERROR: xelatex failed')
            print(r.stderr.decode()[-3000:])
            raise SystemExit(1)

        print('Converting to SVG...')
        n_unique = len(unique_exprs)
        svg_pattern = os.path.join(tmpdir, 'batch_%p.svg')
        subprocess.run(
            ['dvisvgm', '--no-fonts', '--exact', '-p', '1-',
             '-o', svg_pattern, xdv_path],
            capture_output=True, cwd=tmpdir, timeout=300
        )

        # Step 4: Load SVGs (dvisvgm creates batch_1.svg, batch_2.svg, ...)
        svg_cache = {}
        for i in range(n_unique):
            svg_path = os.path.join(tmpdir, f'batch_{i+1}.svg')
            if os.path.exists(svg_path):
                with open(svg_path, 'r') as fh:
                    svg_cache[i] = fh.read()
            else:
                svg_cache[i] = f'<svg xmlns="http://www.w3.org/2000/svg" width="1" height="1"/>'  # empty fallback

    # Step 5: Build replacement dict
    replacements = {}
    for storage, is_disp_dict in [(display_exprs, True), (inline_exprs, False)]:
        for placeholder, (body, is_d) in storage.items():
            idx = dedup[(body, is_d)]
            svg = svg_cache.get(idx)
            if svg:
                # Encode SVG to base64 data URI
                b64 = base64.b64encode(svg.encode()).decode()
                data_uri = f'data:image/svg+xml;base64,{b64}'
                if is_d:
                    replacements[placeholder] = (
                        f'<div class="math-display">'
                        f'<img src="{data_uri}" alt="{body[:80]}"/></div>'
                    )
                else:
                    replacements[placeholder] = (
                        f'<img class="math-inline" src="{data_uri}" alt="{body[:40]}"/>'
                    )
            else:
                replacements[placeholder] = f'<code class="math-failed">${body}$</code>'

    # Step 6: Replace placeholders with HTML img tags
    for ph, html in replacements.items():
        text = text.replace(ph, html)

    failed = sum(1 for v in replacements.values() if 'math-failed' in v)
    if failed:
        print(f'WARNING: {failed} math expressions failed to render')
    else:
        print('All math rendered successfully')


# --- Convert to HTML ---
from markdown import markdown
html_body = markdown(text, extensions=['tables', 'fenced_code', 'codehilite'])

html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<style>
@page {{
    size: A4;
    margin: 20mm 25mm;
    @bottom-center {{
        content: counter(page);
        font-size: 9pt;
        font-family: "IPAexMincho", serif;
    }}
}}
body {{
    font-family: "IPAexMincho", serif;
    font-size: 10.5pt;
    line-height: 1.9;
    color: #222;
    text-rendering: optimizeLegibility;
    overflow-wrap: break-word;
    font-synthesis: none;
}}
h1, h2, h3, h4, strong, th {{
    font-family: "IPAexGothic", sans-serif;
}}
h1 {{ font-size: 16pt; page-break-before: always; margin-top: 1.5em; }}
h2 {{ font-size: 13pt; page-break-before: always; margin-top: 1.2em; }}
h3 {{ font-size: 11pt; margin-top: 1em; }}
h4 {{ font-size: 10.5pt; }}
blockquote {{
    margin: 1em 2em;
    padding: 0.5em 1em;
    border-left: 3px solid #999;
    background: #f5f5f5;
    font-size: 9.5pt;
}}
code {{ font-family: "IPAexGothic", monospace; font-size: 9.5pt; }}
pre {{ background: #f0f0f0; padding: 0.5em; overflow-x: auto; white-space: pre-wrap; overflow-wrap: break-word; }}
.page-break {{ page-break-before: always; }}
table {{
    border-collapse: collapse;
    width: 100%;
    font-size: 10pt;
}}
th, td {{
    border: 1px solid #ccc;
    padding: 4px 8px;
    text-align: left;
}}
th {{
    background: #f5f5f5;
}}
.math-inline {{
    height: 1em;
    vertical-align: middle;
}}
.math-display {{
    display: block;
    text-align: center;
    margin: 0.8em 0;
}}
.math-display img {{
    max-width: 100%;
}}
.math-failed {{
    color: red;
    background: #fff0f0;
}}
</style>
</head>
<body>
{html_body}
</body>
</html>'''

with open('exports/manuscript.html', 'w') as f:
    f.write(html)

# Generate PDF
from weasyprint import HTML
print('Generating PDF...')
HTML('exports/manuscript.html').write_pdf('exports/manuscript.pdf')

print(f'PDF generated: exports/manuscript.pdf')
print(f'Chapters included: {len(files)}')

# Count pages via mutool
try:
    result = subprocess.run(
        ['mutool', 'info', 'exports/manuscript.pdf'],
        capture_output=True, text=True
    )
    for line in result.stdout.split('\n'):
        if line.startswith('Pages:'):
            print(f'{line.strip()} (via mutool)')
            break
except Exception:
    print('Page count unavailable')
