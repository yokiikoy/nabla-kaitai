#!/usr/bin/env python3
"""
Generate a preview-scope version of the manuscript.
Scope: front matter, Chapter 1, and back matter.
Outputs: preview/index.html, preview/manuscript-preview.pdf
"""
import os
import shutil
import subprocess
import glob
import re
from pathlib import Path
from datetime import datetime

# --- Configuration ---
PREVIEW_DIR = Path('preview')
EXPORTS_DIR = Path('exports')
MANUSCRIPT_JA_DIR = Path('manuscript/ja')

# Import functions from build_html and build_pdf if possible, 
# but for portability in this task, I will define the necessary ones.

KATEX_CDN = '''
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
            delimiters: [
                {left: "$$", right: "$$", display: true},
                {left: "$", right: "$", display: false}
            ],
            throwOnError : false
        });
    });
</script>
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | ナブラ解体新書 (先行公開版)</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5/github-markdown.min.css">
<style>
  :root {{ --sidebar-width: 320px; }}
  body {{ margin: 0; display: flex; background: #fff; line-height: 1.7; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
  .sidebar {{ width: var(--sidebar-width); height: 100vh; position: sticky; top: 0; background: #f8f9fa; border-right: 1px solid #d0d7de; overflow-y: auto; padding: 1.5rem; box-sizing: border-box; flex-shrink: 0; }}
  .sidebar h2 {{ font-size: 1.2rem; border: none; margin-bottom: 0.5rem; color: #24292f; }}
  .sidebar .author {{ font-size: 0.8rem; color: #666; margin-bottom: 1.5rem; }}
  .sidebar .toc {{ font-size: 0.85rem; }}
  .sidebar .toc ul {{ list-style: none; padding-left: 0; margin: 0; }}
  .sidebar .toc li {{ margin-bottom: 0.4rem; }}
  .sidebar .toc .level-1 {{ font-weight: bold; margin-top: 1rem; border-bottom: 1px solid #eee; padding-bottom: 2px; }}
  .sidebar .toc .sub-toc {{ font-size: 0.8rem; margin-top: 0.5rem; padding-left: 0.8rem; border-left: 2px solid #eee; }}
  .sidebar .toc .sub-toc li {{ margin-bottom: 0.2rem; font-weight: normal; }}
  .sidebar .toc .sub-toc .level-3 {{ padding-left: 0.8rem; font-size: 0.75rem; color: #666; }}
  .sidebar a {{ text-decoration: none; color: #0969da; }}
  .sidebar a:hover {{ text-decoration: underline; }}
  .sidebar .active {{ color: #cf222e; font-weight: bold; }}
  .main-content {{ flex: 1; min-width: 0; padding: 2rem 4rem; overflow-x: hidden; }}
  .markdown-body {{ max-width: 850px; margin: 0 auto; min-height: 100vh; }}
  @media (max-width: 900px) {{ 
    body {{ flex-direction: column; }} 
    .sidebar {{ width: 100%; height: auto; position: static; padding: 1rem; border-right: none; border-bottom: 1px solid #d0d7de; }} 
    .main-content {{ padding: 1rem; }} 
    .markdown-body {{ padding: 0.5rem; }}
  }}
  .preview-notice {{ background: #fff8c5; border: 1px solid #d4a72c; padding: 1rem; border-radius: 6px; margin-bottom: 2rem; font-size: 0.9rem; }}
  .nav-buttons {{ display: flex; justify-content: space-between; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #eee; }}
  .nav-buttons a {{ padding: 0.5rem 1rem; border: 1px solid #d0d7de; border-radius: 6px; color: #0969da; text-decoration: none; font-size: 0.9rem; }}
  .nav-buttons a:hover {{ background: #f6f8fa; }}
  .site-footer {{ margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #d0d7de; font-size: 0.8rem; color: #57606a; }}
</style>
{KATEX_CDN}
</head>
<body>
  <nav class="sidebar">
    <h2><a href="index.html">ナブラ解体新書</a></h2>
    <p style="font-size: 0.7rem; color: #cf222e; font-weight: bold; margin-bottom: 0.5rem;">先行公開版</p>
    <div class="author">著者: yokiikoy</div>
    <div class="toc">{toc}</div>
  </nav>
  <main class="main-content">
    <div class="preview-notice">
      <strong>先行公開版のお知らせ:</strong> このドキュメントは先行公開用であり、内容（前付け・第1章・後付類のみ）を限定しています。最新の全体版や詳細についてはポータルサイトをご確認ください。
    </div>
    <article class="markdown-body">
      {content}
      <div class="nav-buttons">
        {prev_button}
        {next_button}
      </div>
      <footer class="site-footer">
        <p>&copy; yokiikoy (CC BY-NC 4.0). 先行公開版。詳細は <a href="https://covectorspace.xyz/jp/">Project Co-Vector Space</a> へ。</p>
      </footer>
    </article>
  </main>
</body>
</html>'''

# Re-use logic from build_html.py with modifications
class MathProtector:
    def __init__(self):
        self.math_blocks = []
        self.inline_math = []
    def protect(self, text):
        def replace_display(match):
            idx = len(self.math_blocks)
            self.math_blocks.append(match.group(0))
            return f'\n\nMATH_BLOCK_{idx}_END\n\n'
        def replace_inline(match):
            idx = len(self.inline_math)
            self.inline_math.append(match.group(0))
            return f'INLINE_MATH_{idx}_END'
        text = re.sub(r'\$\$[\s\S]+?\$\$', replace_display, text)
        text = re.sub(r'(?<!\\)\$[^$\n]+?(?<!\\)\$', replace_inline, text)
        return text
    def restore(self, text):
        for i, block in enumerate(self.math_blocks):
            text = text.replace(f'MATH_BLOCK_{i}_END', block)
        for i, math in enumerate(self.inline_math):
            text = text.replace(f'INLINE_MATH_{i}_END', math)
        return text

def slugify(text):
    text = re.sub(r'\$[^$]*\$', '', text)
    text = re.sub(r'[{}\\[\\]()（）——–—ー・。、,!?！？]', '', text)
    text = re.sub(r'\s+', '-', text).strip('-')
    text = re.sub(r'[^a-zA-Z0-9\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF-]', '', text)
    return text or 'section'

def apply_inline_formatting(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
    return text

def render_table(lines, protector):
    if len(lines) < 2: return "\n".join(lines)
    html = ['<div class="table-wrapper"><table>']
    content_lines = [l for l in lines if not re.match(r'^\|?[:\-\s|]+\|?$', l)]
    for i, line in enumerate(content_lines):
        cells = [c.strip() for c in line.split('|')]
        if cells and not cells[0]: cells = cells[1:]
        if cells and not cells[-1]: cells = cells[:-1]
        if not cells: continue
        tag = 'th' if i == 0 else 'td'
        html.append('<tr>' + "".join(f'<{tag}>{protector.restore(apply_inline_formatting(c))}</{tag}>' for c in cells) + '</tr>')
    html.append('</table></div>')
    return "\n".join(html)

def process_markdown(markdown_text):
    text = markdown_text.replace('<!-- pagebreak -->', '').replace('<!-- scalebox -->', '').replace('<!-- endscalebox -->', '')
    text = re.sub(r'\\bm\{([a-zA-Z0-9]+)\}', r'\\mathbf{\1}', text)
    text = re.sub(r'\\bm\{(.+?)\}', r'\\boldsymbol{\1}', text)
    text = text.replace('\\bm ', '\\boldsymbol ')
    protector = MathProtector()
    text = protector.protect(text)
    
    lines = text.split('\n')
    result = []
    in_para = in_quote = in_table = False
    in_list = False
    table_lines = []

    def close_all():
        nonlocal in_para, in_quote, in_list, in_table, table_lines
        if in_para: result.append('</p>'); in_para = False
        if in_quote: result.append('</blockquote>'); in_quote = False
        if in_list: result.append('</ul>' if in_list == 'ul' else '</ol>'); in_list = False
        if in_table: result.append(render_table(table_lines, protector)); in_table = False; table_lines = []

    for line in lines:
        if line.strip().startswith('|'):
            if not in_table: close_all(); in_table = True
            table_lines.append(line.strip()); continue
        elif in_table: close_all()

        h_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if h_match:
            close_all()
            lv, content = len(h_match.group(1)), h_match.group(2).strip()
            restored = protector.restore(apply_inline_formatting(content))
            result.append(f'<h{lv} id="{slugify(restored)}">{restored}</h{lv}>'); continue

        if line.strip() == '---': close_all(); result.append('<hr />'); continue
        if line.strip().startswith('>'):
            if not in_quote: close_all(); result.append('<blockquote>'); in_quote = True
            result.append(f'<p>{protector.restore(apply_inline_formatting(line.strip()[1:].strip()))}</p>'); continue
        
        ol_match = re.match(r'^(\d+)\.\s*(.*)', line.strip())
        ul_match = re.match(r'^[-*]\s+(.*)', line)
        if ol_match or ul_match:
            new_list = 'ol' if ol_match else 'ul'
            if in_list != new_list: close_all(); result.append(f'<{new_list}>'); in_list = new_list
            content = ol_match.group(2) if ol_match else ul_match.group(1)
            result.append(f'<li>{protector.restore(apply_inline_formatting(content))}</li>'); continue

        if line.strip() == '': close_all(); continue
        processed = protector.restore(apply_inline_formatting(line))
        if not in_para: result.append(f'<p>{processed}'); in_para = True
        else: result.append(' ' + processed)
    close_all()
    return '\n'.join(result)

def build_preview_artifacts():
    if PREVIEW_DIR.exists(): shutil.rmtree(PREVIEW_DIR)
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Collect Files
    files = []
    # Make sure we are in the right directory or use absolute paths if needed
    # but relative to project root is fine if executed from there.
    front_matter = sorted(glob.glob(str(MANUSCRIPT_JA_DIR / 'ch00/*.md')))
    files.extend(front_matter)
    
    ch01_path = MANUSCRIPT_JA_DIR / 'ch01/ch01.md'
    if ch01_path.exists():
        files.append(str(ch01_path))
    else:
        # Try finding any .md in ch01
        fallback = glob.glob(str(MANUSCRIPT_JA_DIR / 'ch01/*.md'))
        if fallback:
            files.append(fallback[0])
        else:
            print(f"Warning: Chapter 1 not found in {MANUSCRIPT_JA_DIR / 'ch01/'}")
    for suffix in ['afterword', 'references', 'appendix']:
        f = MANUSCRIPT_JA_DIR / f'{suffix}.md'
        if f.exists(): files.append(str(f))

    # 2. Build HTML
    chapters = []
    front_mapping = {"01_preface.md": "index.html", "02_introduction.md": "intro.html", "03_portal.md": "portal.html"}
    special_mapping = {"おわりに": "postscript.html", "参考文献": "refs.html", "付録": "appendix.html"}

    for fpath in files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('---'):
                end = content.find('---', 3)
                if end > 0: content = content[end+3:].lstrip()
            
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else Path(fpath).stem
            
            filename = front_mapping.get(Path(fpath).name)
            if not filename:
                if '第1章' in title or '第１章' in title: filename = "ch01.html"
                else:
                    for key, fname in special_mapping.items():
                        if key in title: filename = fname; break
            if not filename: filename = Path(fpath).stem + ".html"
            
            chapters.append({"title": title, "content": content, "filename": filename})

    toc_html = "<ul>" + "".join(f'<li class="level-1"><a href="{ch["filename"]}" id="link-{ch["filename"]}">{ch["title"].split("：")[0]}</a></li>' for ch in chapters) + "</ul>"

    for i, ch in enumerate(chapters):
        content_html = process_markdown(ch["content"])
        prev_ch = chapters[i-1] if i > 0 else None
        next_ch = chapters[i+1] if i < len(chapters)-1 else None
        prev_btn = f'<a href="{prev_ch["filename"]}">← {prev_ch["title"][:10]}...</a>' if prev_ch else '<span></span>'
        next_btn = f'<a href="{next_ch["filename"]}">{next_ch["title"][:10]}... →</a>' if next_ch else '<span></span>'
        
        page_toc = toc_html.replace(f'id="link-{ch["filename"]}"', f'class="active" id="link-{ch["filename"]}"')
        final_html = HTML_TEMPLATE.format(title=ch["title"], toc=page_toc, content=content_html, prev_button=prev_btn, next_button=next_btn, KATEX_CDN=KATEX_CDN)
        with open(PREVIEW_DIR / ch["filename"], 'w', encoding='utf-8') as f:
            f.write(final_html)

    # 3. Build PDF via Pandoc/XeLaTeX (simplified logic from build_pdf.py)
    print("Generating Preview PDF...")
    combined_md = "\n\n\\newpage\n\n".join(ch["content"] for ch in chapters)
    # Process markers for PDF
    combined_md = combined_md.replace('<!-- pagebreak -->', '\\clearpage')
    
    # We'll use a minimal LaTeX template to ensure it builds
    preview_tex = EXPORTS_DIR / 'manuscript_preview.tex'
    
    # Run pandoc to get LaTeX body
    process = subprocess.run(['pandoc', '--from=markdown+tex_math_dollars', '--to=latex', '--top-level-division=chapter'], input=combined_md, capture_output=True, text=True)
    latex_body = process.stdout
    
    # Basic preamble
    preamble = r'''\documentclass[a4paper,12pt,openany]{book}
\usepackage{amsmath,amssymb,bm,esint,cancel,graphicx,xcolor,hyperref,geometry,fontspec}
\setmainfont{IPAexMincho}[AutoFakeBold=1.5, Ligatures=TeX]
\XeTeXlinebreaklocale "ja"
\XeTeXlinebreakskip=0pt plus 1pt minus 0.1pt
\geometry{margin=25mm}
\hypersetup{colorlinks=true,linkcolor=blue}
\begin{document}
\title{ナブラ解体新書 (先行公開版)}
\author{yokiikoy}
\date{\today}
\maketitle
\tableofcontents
'''
    with open(preview_tex, 'w', encoding='utf-8') as f:
        f.write(preamble + latex_body + r'\end{document}')
    
    # Compile
    for _ in [1, 2]:
        subprocess.run(['xelatex', '-interaction=nonstopmode', '-output-directory=preview', str(preview_tex)], capture_output=True)
    
    # Rename output
    if (PREVIEW_DIR / 'manuscript_preview.pdf').exists():
        os.rename(PREVIEW_DIR / 'manuscript_preview.pdf', PREVIEW_DIR / 'manuscript-preview.pdf')
    
    print(f"Artifacts generated in {PREVIEW_DIR}/")

if __name__ == '__main__':
    build_preview_artifacts()
