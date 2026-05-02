#!/usr/bin/env python3
"""
Generate multi-page HTML from manuscript_combined.md.
Splits content by chapters to improve MathJax performance.
"""

import re
import sys
from pathlib import Path

# --- Configuration ---

MATHJAX_CONFIG = '''window.MathJax = {
  tex: {
    inlineMath: [['$', '$']],
    displayMath: [['$$', '$$']],
    processEscapes: true
  },
  options: {
    ignoreHtmlClass: 'tex2jax_ignore',
    processHtmlClass: 'tex2jax_process'
  }
};
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
  .markdown-body {{ max-width: 850px; margin: 0 auto; }}
  @media (max-width: 900px) {{ body {{ flex-direction: column; }} .sidebar {{ width: 100%; height: auto; position: static; }} .main-content {{ padding: 1.5rem; }} }}
  blockquote {{ border-left: 4px solid #d0d7de; color: #57606a; background: #f6f8fa; padding: 0.5em 1.2em; margin: 1.5em 0; border-radius: 0 6px 6px 0; }}
  .mjx-container {{ overflow-x: auto !important; padding: 0.8em 0; max-width: 100%; }}
  .nav-buttons {{ display: flex; justify-content: space-between; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #eee; }}
  .nav-buttons a {{ padding: 0.5rem 1rem; border: 1px solid #d0d7de; border-radius: 6px; color: #0969da; text-decoration: none; }}
  .nav-buttons a:hover {{ background: #f6f8fa; }}
</style>
<script>
{MATHJAX_CONFIG}
</script>
<script id="MathJax-script" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</head>
<body>
  <nav class="sidebar">
    <h2><a href="index.html">ナブラ解体新書</a></h2>
    <div class="author">著者: yokiikoy</div>
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
            return f'\n\n<div class="math-block tex2jax_process">MATH_BLOCK_{idx}_END</div>\n\n'
        def replace_inline(match):
            idx = len(self.inline_math)
            self.inline_math.append(match.group(0))
            return f'<span class="tex2jax_process">INLINE_MATH_{idx}_END</span>'
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

def process_markdown(markdown_text):
    protector = MathProtector()
    text = protector.protect(markdown_text)
    lines = text.split('\n')
    result = []
    in_code, in_quote, in_list, in_para = False, False, False, False
    
    for line in lines:
        # Code block
        if line.strip().startswith('```'):
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

        # Headings
        h_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if h_match:
            lv, content = len(h_match.group(1)), h_match.group(2).strip()
            restored = protector.restore(content)
            result.append(f'<h{lv} id="{slugify(restored)}">{restored}</h{lv}>')
            in_para = in_list = False
            continue

        # Horizontal rule
        if line.strip() == '---':
            result.append('<hr />')
            in_para = in_list = False
            continue

        # Blockquote
        if line.strip().startswith('>'):
            content = protector.restore(line[1:].strip())
            if not in_quote:
                result.append('<blockquote><p>')
                in_quote = True
            result.append(content + '<br>')
            in_para = False
            continue
        elif in_quote:
            result.append('</p></blockquote>')
            in_quote = False

        # Lists
        ol_match = re.match(r'^(\d+)\.\s*(.*)', line.strip())
        ul_match = re.match(r'^[-*]\s+(.*)', line)
        
        if ol_match:
            if in_list != 'ol':
                if in_list: result.append('</ul>' if in_list == 'ul' else '</ol>')
                result.append('<ol>')
                in_list = 'ol'
            result.append(f'<li>{protector.restore(ol_match.group(2))}</li>')
            in_para = False
            continue
        elif ul_match:
            if in_list != 'ul':
                if in_list: result.append('</ul>' if in_list == 'ul' else '</ol>')
                result.append('<ul>')
                in_list = 'ul'
            result.append(f'<li>{protector.restore(ul_match.group(1))}</li>')
            in_para = False
            continue
        elif in_list:
            result.append('</ul>' if in_list == 'ul' else '</ol>')
            in_list = False

        # Paragraphs
        if line.strip() == '':
            if in_para: result.append('</p>'); in_para = False
            continue
        
        processed = protector.restore(line)
        if not processed.strip().startswith('<') and processed.strip():
            if not in_para:
                result.append(f'<p>{processed}')
                in_para = True
            else:
                result.append(processed)
    
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

    # Split into chapters
    chapters = []
    current_chapter = {"title": "まえがき", "content": [], "filename": "index.html"}
    
    lines = full_text.split('\n')
    ch_count = 0
    
    # Define mapping for special sections to filenames
    special_mapping = {
        "おわりに": "postscript.html",
        "参考文献": "refs.html",
        "付録": "appendix.html"
    }

    for line in lines:
        if line.startswith('# '):
            title = line.lstrip('#').strip()
            
            # Check if this is a new chapter or special section
            is_new_section = False
            new_filename = ""
            
            if title.startswith('第'):
                ch_count += 1
                new_filename = f"ch{ch_count:02d}.html"
                is_new_section = True
            else:
                for key, fname in special_mapping.items():
                    if key in title:
                        new_filename = fname
                        is_new_section = True
                        break
            
            if is_new_section:
                if current_chapter["content"]:
                    chapters.append(current_chapter)
                current_chapter = {"title": title, "content": [line], "filename": new_filename}
                continue

        current_chapter["content"].append(line)
    chapters.append(current_chapter)

    # Build TOC HTML
    toc_html_parts = ["<ul>"]
    toc_html_parts.append('<li><a href="index.html" id="link-index.html">まえがき</a></li>')
    for ch in chapters:
        if ch["filename"] == "index.html": continue
        
        # Display title: remove subtitle for cleaner sidebar
        display_title = ch["title"]
        if '：' in display_title:
            display_title = display_title.split('：')[0]
        elif '——' in display_title:
            display_title = display_title.split('——')[0]
            
        toc_html_parts.append(f'<li class="level-1"><a href="{ch["filename"]}" id="link-{ch["filename"]}">{display_title}</a></li>')
    toc_html_parts.append("</ul>")
    toc_html = "\n".join(toc_html_parts)


    # Generate each page
    for i, ch in enumerate(chapters):
        content_md = "\n".join(ch["content"])
        
        # Extract sub-headings for THIS chapter to show in sidebar
        sub_headings = []
        for line in ch["content"]:
            h_match = re.match(r'^(#{2,3})\s+(.+)$', line)
            if h_match:
                level = len(h_match.group(1))
                text = h_match.group(2).strip()
                # Protect/Restore math in heading for sidebar
                temp_protector = MathProtector()
                protected = temp_protector.protect(text)
                restored = temp_protector.restore(protected)
                sub_headings.append((level, restored, slugify(restored)))

        content_html = process_markdown(content_md)
        
        # Build local TOC for this chapter
        local_toc = ""
        if sub_headings:
            local_toc = '<ul class="sub-toc">'
            for lv, text, anchor in sub_headings:
                indent = f"level-{lv}"
                local_toc += f'<li class="{indent}"><a href="#{anchor}">{text}</a></li>'
            local_toc += '</ul>'

        # Navigation
        prev_ch = chapters[i-1] if i > 0 else None
        next_ch = chapters[i+1] if i < len(chapters)-1 else None
        
        prev_btn = f'<a href="{prev_ch["filename"]}">← {prev_ch["title"][:15]}...</a>' if prev_ch else '<span></span>'
        next_btn = f'<a href="{next_ch["filename"]}">{next_ch["title"][:15]}... →</a>' if next_ch else '<span></span>'
        
        # Mark active TOC item and insert local TOC
        active_marker = f'id="link-{ch["filename"]}"'
        active_replacement = f'class="active" {active_marker}'
        page_toc = toc_html.replace(active_marker, active_replacement)
        
        # Insert the sub-headings under the active chapter link
        if local_toc:
            insert_point = f'</a></li>'
            find_str = f'link-{ch["filename"]}">{ch["title"].split("：")[0] if "：" in ch["title"] else ch["title"]}</a></li>'
            page_toc = page_toc.replace(find_str, find_str.replace('</li>', local_toc + '</li>'))
        
        final_html = HTML_TEMPLATE.format(
            title=ch["title"],
            MATHJAX_CONFIG=MATHJAX_CONFIG,
            toc=page_toc,
            content=content_html,
            prev_button=prev_btn,
            next_button=next_btn
        )
        
        output_path = docs_dir / ch["filename"]
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"Generated {output_path}")

if __name__ == '__main__':
    main()
