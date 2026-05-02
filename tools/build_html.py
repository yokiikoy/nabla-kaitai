#!/usr/bin/env python3
"""
Generate multi-page HTML from manuscript_combined.md using KaTeX.
Splits content by chapters and provides fast, beautiful math rendering.
"""

import re
import sys
import glob
from pathlib import Path

# --- Configuration ---

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
<title>{title} | ナブラ解体新書</title>
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
  blockquote {{ border-left: 4px solid #d0d7de; color: #57606a; background: #f6f8fa; padding: 0.5em 1.2em; margin: 1.5em 0; border-radius: 0 6px 6px 0; }}
  .nav-buttons {{ display: flex; justify-content: space-between; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #eee; }}
  .nav-buttons a {{ padding: 0.5rem 1rem; border: 1px solid #d0d7de; border-radius: 6px; color: #0969da; text-decoration: none; font-size: 0.9rem; }}
  .nav-buttons a:hover {{ background: #f6f8fa; }}
  strong {{ font-weight: 800 !important; color: #000; }}
  blockquote strong {{ color: #24292f !important; }}
  table {{ border-collapse: collapse; width: 100%; margin: 1.5em 0; font-size: 0.9em; }}
  th, td {{ border: 1px solid #d0d7de; padding: 6px 13px; }}
  tr:nth-child(even) {{ background-color: #f6f8fa; }}
  th {{ font-weight: 600; background-color: #f6f8fa; }}
  /* KaTeX responsiveness */
  .katex-display {{ overflow-x: auto; overflow-y: hidden; padding: 0.5em 0; }}
</style>
{KATEX_CDN}
</head>
  <nav class="sidebar">
    <h2><a href="index.html">ナブラ解体新書</a></h2>
    <div class="author">
      著者: yokiikoy<br>
      <a href="http://covectorspace.xyz/jp/" style="font-size: 0.75rem; color: #666; text-decoration: none;">Project Co-Vector Space</a>
    </div>
    <div class="toc">{toc}</div>
  </nav>
  <main class="main-content">
    <article class="markdown-body">
      {content}
      <div class="nav-buttons">
        {prev_button}
        {next_button}
      </div>
    </article>
  </main>
</body>
</html>'''

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
    """Apply markdown-style inline formatting (bold, italic, code, links)."""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
    return text

def render_table(lines, protector):
    """Render markdown table lines as HTML."""
    if len(lines) < 2:
        return "\n".join(lines)
    
    html = ['<table>']
    # Filter out the separator line (| :--- |)
    content_lines = [l for l in lines if not re.match(r'^\|?[:\-\s|]+\|?$', l)]
    
    for i, line in enumerate(content_lines):
        cells = [c.strip() for c in line.split('|')]
        if not cells[0]: cells = cells[1:]
        if cells and not cells[-1]: cells = cells[:-1]
        
        if i == 0:
            html.append('<thead><tr>')
            for cell in cells:
                formatted = protector.restore(apply_inline_formatting(cell))
                html.append(f'<th>{formatted}</th>')
            html.append('</tr></thead><tbody>')
        else:
            html.append('<tr>')
            for cell in cells:
                formatted = protector.restore(apply_inline_formatting(cell))
                html.append(f'<td>{formatted}</td>')
            html.append('</tr>')
    
    html.append('</tbody></table>')
    return "\n".join(html)

def process_markdown(markdown_text):
    # 0. Clean up PDF-specific markers
    text = markdown_text.replace('<!-- pagebreak -->', '')
    text = text.replace('<!-- scalebox -->', '')
    text = text.replace('<!-- endscalebox -->', '')

    # 1. Global replacement of \bm for KaTeX compatibility
    text = re.sub(r'\\bm\{([a-zA-Z0-9]+)\}', r'\\mathbf{\1}', text)
    text = re.sub(r'\\bm\{(.+?)\}', r'\\boldsymbol{\1}', text)
    text = text.replace('\\bm ', '\\boldsymbol ')
    
    protector = MathProtector()
    text = protector.protect(text)
    lines = text.split('\n')
    result = []
    in_code, in_quote, in_list, in_para, in_table = False, False, False, False, False
    table_lines = []
    
    for line in lines:
        if line.strip().startswith('```'):
            if in_table:
                result.append(render_table(table_lines, protector))
                in_table = False
            if not in_code:
                result.append('<pre><code>')
                in_code = True
            else:
                result.append('</code></pre>')
                in_code = False
            continue
        if in_code:
            result.append(line)
            continue

        # Table detection
        if line.strip().startswith('|'):
            if not in_table:
                if in_para: result.append('</p>'); in_para = False
                in_table = True
                table_lines = []
            table_lines.append(line.strip())
            continue
        elif in_table:
            result.append(render_table(table_lines, protector))
            in_table = False
            table_lines = []

        h_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if h_match:
            lv, content = len(h_match.group(1)), h_match.group(2).strip()
            # Apply inline formatting to headings too
            restored = protector.restore(apply_inline_formatting(content))
            result.append(f'<h{lv} id="{slugify(restored)}">{restored}</h{lv}>')
            in_para = in_list = False
            continue

        if line.strip() == '---':
            result.append('<hr />')
            in_para = in_list = False
            continue

        if line.strip().startswith('>'):
            content = protector.restore(apply_inline_formatting(line.strip()[1:].strip()))
            if not in_quote:
                result.append('<blockquote>')
                in_quote = True
            result.append(f'<p>{content}</p>')
            in_para = False
            continue
        elif in_quote:
            result.append('</blockquote>')
            in_quote = False

        ol_match = re.match(r'^(\d+)\.\s*(.*)', line.strip())
        ul_match = re.match(r'^[-*]\s+(.*)', line)
        
        if ol_match:
            if in_list != 'ol':
                if in_list: result.append('</ul>' if in_list == 'ul' else '</ol>')
                result.append('<ol>')
                in_list = 'ol'
            content = protector.restore(apply_inline_formatting(ol_match.group(2)))
            result.append(f'<li>{content}</li>')
            in_para = False
            continue
        elif ul_match:
            if in_list != 'ul':
                if in_list: result.append('</ul>' if in_list == 'ul' else '</ol>')
                result.append('<ul>')
                in_list = 'ul'
            content = protector.restore(apply_inline_formatting(ul_match.group(1)))
            result.append(f'<li>{content}</li>')
            in_para = False
            continue
        elif in_list:
            result.append('</ul>' if in_list == 'ul' else '</ol>')
            in_list = False

        if line.strip() == '':
            if in_para: result.append('</p>'); in_para = False
            continue
        
        # Inline formatting for normal paragraphs
        processed = apply_inline_formatting(line)
        processed = protector.restore(processed)
        
        is_block = any(processed.strip().startswith(t) for t in ['<h', '<blockquote', '<ul', '<ol', '<pre', '<hr', '<div', '$$'])
        is_inline_tag = any(processed.strip().startswith(t) for t in ['<strong', '<em', '<code', '<a', '<span'])
        
        if (not is_block or is_inline_tag) and processed.strip():
            if not in_para:
                result.append(f'<p>{processed}')
                in_para = True
            else:
                result.append(processed)
        else:
            if in_para:
                result.append('</p>')
                in_para = False
            if processed.strip():
                result.append(processed)
    
    if in_table:
        result.append(render_table(table_lines, protector))
    if in_para: result.append('</p>')
    if in_quote: result.append('</p></blockquote>')
    if in_list: result.append('</ul>' if in_list == 'ul' else '</ol>')
    return '\n'.join(result)


def main():
    md_path = Path('exports/manuscript_combined.md')
    docs_dir = Path('docs')
    docs_dir.mkdir(exist_ok=True)
    
    with open(md_path, 'r', encoding='utf-8') as f:
        full_text = f.read()

    chapters = []
    front_matter_files = glob.glob('manuscript/ja/ch00/*.md')
    front_matter_files.sort()
    front_mapping = {
        "01_preface.md": "index.html",
        "02_introduction.md": "intro.html",
        "03_portal.md": "portal.html"
    }
    
    for fpath in front_matter_files:
        fname = Path(fpath).name
        target_html = front_mapping.get(fname, fname.replace('.md', '.html'))
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else "まえがき"
            chapters.append({"title": title, "content": content.split('\n'), "filename": target_html})
    
    lines = full_text.split('\n')
    ch_count = 0
    special_mapping = {"おわりに": "postscript.html", "参考文献": "refs.html", "付録": "appendix.html"}
    current_chapter = None

    for line in lines:
        if line.startswith('# '):
            title = line.lstrip('#').strip()
            is_new = False
            new_filename = ""
            if title.startswith('第'):
                ch_count += 1
                new_filename = f"ch{ch_count:02d}.html"
                is_new = True
            else:
                for key, fname in special_mapping.items():
                    if key in title:
                        new_filename = fname
                        is_new = True
                        break
            if is_new:
                if current_chapter: chapters.append(current_chapter)
                current_chapter = {"title": title, "content": [line], "filename": new_filename}
                continue
        if current_chapter:
            current_chapter["content"].append(line)
    if current_chapter: chapters.append(current_chapter)

    # Build TOC HTML
    toc_html_parts = ["<ul>"]
    for ch in chapters:
        display_title = ch["title"]
        if '：' in display_title: display_title = display_title.split('：')[0]
        elif '——' in display_title: display_title = display_title.split('——')[0]
        toc_html_parts.append(f'<li class="level-1"><a href="{ch["filename"]}" id="link-{ch["filename"]}">{display_title}</a></li>')
    toc_html_parts.append("</ul>")
    toc_html = "\n".join(toc_html_parts)

    for i, ch in enumerate(chapters):
        sub_headings = []
        for line in ch["content"]:
            h_match = re.match(r'^(#{2,3})\s+(.+)$', line)
            if h_match:
                lv, text = len(h_match.group(1)), h_match.group(2).strip()
                temp_protector = MathProtector()
                protected = temp_protector.protect(text)
                restored = temp_protector.restore(apply_inline_formatting(protected))
                sub_headings.append((lv, restored, slugify(restored)))

        content_html = process_markdown("\n".join(ch["content"]))
        local_toc = ""
        if sub_headings:
            local_toc = '<ul class="sub-toc">'
            for lv, text, anchor in sub_headings:
                local_toc += f'<li class="level-{lv}"><a href="#{anchor}">{text}</a></li>'
            local_toc += '</ul>'

        prev_ch = chapters[i-1] if i > 0 else None
        next_ch = chapters[i+1] if i < len(chapters)-1 else None
        prev_btn = f'<a href="{prev_ch["filename"]}">← {prev_ch["title"][:15]}...</a>' if prev_ch else '<span></span>'
        next_btn = f'<a href="{next_ch["filename"]}">{next_ch["title"][:15]}... →</a>' if next_ch else '<span></span>'
        
        active_marker = f'id="link-{ch["filename"]}"'
        page_toc = toc_html.replace(active_marker, f'class="active" {active_marker}')
        if local_toc:
            short_title = ch["title"].split("：")[0] if "：" in ch["title"] else ch["title"].split("——")[0]
            find_str = f'link-{ch["filename"]}">{short_title}</a></li>'
            page_toc = page_toc.replace(find_str, find_str.replace('</li>', local_toc + '</li>'))
        
        final_html = HTML_TEMPLATE.format(
            title=ch["title"], toc=page_toc, KATEX_CDN=KATEX_CDN,
            content=content_html, prev_button=prev_btn, next_button=next_btn
        )
        with open(docs_dir / ch["filename"], 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"Generated {docs_dir / ch['filename']}")

if __name__ == '__main__':
    main()
