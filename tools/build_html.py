#!/usr/bin/env python3
"""
Generate multi-page HTML from manuscript using KaTeX.
Profile-driven build system separating content scope and toc scope.
"""

import re
import sys
import argparse
from pathlib import Path

# Add tools directory to path so we can import core
sys.path.append(str(Path(__file__).parent))
from core.profile import get_profile
from core.manuscript import ManuscriptModel

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
  .sidebar .disabled-link {{ color: #8c959f; cursor: not-allowed; text-decoration: none; }}
  .main-content {{ flex: 1; min-width: 0; padding: 2rem 4rem; overflow-x: hidden; }}
  .markdown-body {{ max-width: 850px; margin: 0 auto; min-height: 100vh; }}
  @media (max-width: 900px) {{ 
    body {{ flex-direction: column; }} 
    .sidebar {{ width: 100%; height: auto; position: static; padding: 1rem; border-right: none; border-bottom: 1px solid #d0d7de; }} 
    .main-content {{ padding: 1rem; }} 
    .markdown-body {{ padding: 0.5rem; }}
  }}
  blockquote {{ border-left: 4px solid #d0d7de; color: #57606a; background: #f6f8fa; padding: 0.5em 1.2em; margin: 1.5em 0; border-radius: 0 6px 6px 0; }}
  .table-wrapper {{ overflow-x: auto; margin: 1.5em 0; }}
  table {{ border-collapse: collapse; width: 100%; font-size: 0.9em; }}
  th, td {{ border: 1px solid #d0d7de; padding: 6px 13px; }}
  tr:nth-child(even) {{ background-color: #f6f8fa; }}
  th {{ font-weight: 600; background-color: #f6f8fa; }}
  .nav-buttons {{ display: flex; justify-content: space-between; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #eee; }}
  .nav-buttons a {{ padding: 0.5rem 1rem; border: 1px solid #d0d7de; border-radius: 6px; color: #0969da; text-decoration: none; font-size: 0.9rem; }}
  .nav-buttons a:hover {{ background: #f6f8fa; }}
  strong {{ font-weight: 800 !important; color: #000; }}
  blockquote strong {{ color: #24292f !important; }}
  /* KaTeX responsiveness */
  .katex-display {{ overflow-x: auto; overflow-y: hidden; padding: 0.5em 0; }}
  .full-toc h2 {{ font-size: 1.1rem; margin: 1.5em 0 0.3em; padding-bottom: 2px; border-bottom: 1px solid #d0d7de; }}
  .full-toc h2 a {{ color: #24292f; text-decoration: none; }}
  .full-toc h2 a:hover {{ color: #0969da; }}
  .full-toc h2 .disabled-link {{ color: #8c959f; cursor: not-allowed; }}
  .full-toc ul {{ list-style: none; padding-left: 1.5rem; margin: 0.3em 0 0; }}
  .full-toc li {{ margin-bottom: 0.2rem; font-size: 0.9rem; }}
  .full-toc .level-3 {{ padding-left: 1rem; font-size: 0.8rem; color: #57606a; }}
  .full-toc a {{ color: #0969da; text-decoration: none; }}
  .full-toc a:hover {{ text-decoration: underline; }}
  .full-toc .disabled-link {{ color: #8c959f; cursor: not-allowed; text-decoration: none; }}
  .full-toc .part-header {{ font-size: 1.1rem; margin: 2em 0 0.5em; padding: 0.3em 0.8em; background: #f6f8fa; border-left: 4px solid #0969da; color: #24292f; }}
  .full-toc .toc-part-chapters {{ padding-left: 1.5rem; }}
  .full-toc .toc-part-chapters h3 {{ font-size: 0.95rem; margin: 0.5em 0 0.2em; }}
  .full-toc .toc-part-chapters h3 a {{ color: #24292f; }}
  .full-toc .toc-part-chapters ul {{ padding-left: 1.5rem; }}
  .site-footer {{ margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #d0d7de; font-size: 0.8rem; color: #57606a; }}
  .site-footer a {{ color: #0969da; text-decoration: none; }}
  .site-footer a:hover {{ text-decoration: underline; }}
</style>
{KATEX_CDN}
</head>
<body>
  <nav class="sidebar">
    <h2><a href="index.html">ナブラ解体新書</a></h2>
    <div class="author">
      著者: yokiikoy<br>
      <a href="http://covectorspace.xyz/jp/" style="font-size: 0.75rem; color: #666; text-decoration: none;">Project Co-Vector Space</a>
    </div>
    <div class="toc">
      {toc}
    </div>
  </nav>
  <main class="main-content">
    <article class="markdown-body">
{content}
      <div class="nav-buttons">
        {prev_button}
        {next_button}
      </div>
    </article>
    <footer class="site-footer">
      <p>&copy; 2024- yokiikoy. CC BY-NC 4.0.</p>
    </footer>
  </main>
</body>
</html>
'''

# --- Markdown Processing Utils ---
class MathProtector:
    def __init__(self):
        self.math_blocks = {}
        self.counter = 0

    def protect(self, text):
        def repl(match):
            key = f"__MATH_BLOCK_{self.counter}__"
            self.math_blocks[key] = match.group(0)
            self.counter += 1
            return key
        text = re.sub(r'\$\$(.*?)\$\$', repl, text, flags=re.DOTALL)
        text = re.sub(r'\$(.*?)\$', repl, text)
        return text

    def restore(self, text):
        for key, val in self.math_blocks.items():
            text = text.replace(key, val)
        return text

def apply_inline_formatting(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text

def process_markdown(md_text):
    protector = MathProtector()
    md_text = protector.protect(md_text)
    
    lines = md_text.split('\n')
    result = []
    in_list = False
    in_para = False
    in_quote = False
    in_table = False
    table_lines = []
    footnotes = {}

    def close_para():
        nonlocal in_para
        if in_para:
            result.append('</p>')
            in_para = False
            
    def close_list():
        nonlocal in_list
        if in_list == 'ul':
            result.append('</ul>')
            in_list = False
        elif in_list == 'ol':
            result.append('</ol>')
            in_list = False

    def close_quote():
        nonlocal in_quote
        if in_quote:
            result.append('</blockquote>')
            in_quote = False

    def flush_table():
        nonlocal in_table, table_lines
        if not in_table or not table_lines: return
        
        result.append('<div class="table-wrapper"><table>')
        
        header_cols = [c.strip() for c in table_lines[0].strip('|').split('|')]
        result.append('<thead><tr>')
        for col in header_cols:
            result.append(f'<th>{protector.restore(apply_inline_formatting(col))}</th>')
        result.append('</tr></thead>')
        
        if len(table_lines) > 2:
            result.append('<tbody>')
            for row in table_lines[2:]:
                cols = [c.strip() for c in row.strip('|').split('|')]
                result.append('<tr>')
                for col in cols:
                    result.append(f'<td>{protector.restore(apply_inline_formatting(col))}</td>')
                result.append('</tr>')
            result.append('</tbody>')
            
        result.append('</table></div>')
        in_table = False
        table_lines = []

    for i, line in enumerate(lines):
        if line.startswith('[^') and ']:' in line:
            fn_id = line[2:line.find(']')]
            fn_content = line[line.find(']:')+2:].strip()
            footnotes[fn_id] = fn_content
            continue

    for i, line in enumerate(lines):
        if line.strip().startswith('|'):
            if not in_table:
                close_para()
                close_quote()
                close_list()
                in_table = True
                table_lines = []
            table_lines.append(line.strip())
            continue
        elif in_table:
            flush_table()

        if line.strip() == '---':
            close_para()
            close_list()
            close_quote()
            result.append('<hr />')
            continue

        # Heading detection
        h_match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
        if h_match:
            close_para()
            close_list()
            close_quote()
            lv = len(h_match.group(1))
            heading_text = h_match.group(2).strip()
            slug = re.sub(r'[\s]+', '-', heading_text)  # matches ManuscriptModel._slugify
            processed = protector.restore(apply_inline_formatting(heading_text))
            processed = re.sub(r'\[\^(.+?)\]', r'<sup>[\1]</sup>', processed)
            result.append(f'<h{lv} id="{slug}">{processed}</h{lv}>')
            continue

        if line.strip().startswith('>'):
            content = line.strip()[1:].strip()
            if not in_quote:
                close_para()
                close_list()
                result.append('<blockquote>')
                in_quote = True
            processed_inner = protector.restore(apply_inline_formatting(content))
            processed_inner = re.sub(r'\[\^(.+?)\]', r'<sup>[\1]</sup>', processed_inner)
            result.append(f'<p>{processed_inner}</p>')
            continue
        elif in_quote:
            if line.strip() == '':
                close_quote()

        ol_match = re.match(r'^(\d+)\.\s*(.*)', line.strip())
        ul_match = re.match(r'^[-*]\s+(.*)', line)
        
        if ol_match:
            if in_list != 'ol':
                close_para()
                close_quote()
                if in_list == 'ul': result.append('</ul>')
                result.append('<ol>')
                in_list = 'ol'
            content = protector.restore(apply_inline_formatting(ol_match.group(2)))
            content = re.sub(r'\[\^(.+?)\]', r'<sup>[\1]</sup>', content)
            result.append(f'<li>{content}</li>')
            in_para = False
            continue
        elif ul_match:
            if in_list != 'ul':
                close_para()
                close_quote()
                if in_list == 'ol': result.append('</ol>')
                result.append('<ul>')
                in_list = 'ul'
            content = protector.restore(apply_inline_formatting(ul_match.group(1)))
            content = re.sub(r'\[\^(.+?)\]', r'<sup>[\1]</sup>', content)
            result.append(f'<li>{content}</li>')
            in_para = False
            continue

        if line.strip() == '':
            close_para()
            close_list()
            close_quote()
            continue
        
        processed = apply_inline_formatting(line)
        processed = protector.restore(processed)
        processed = re.sub(r'\[\^(.+?)\]', r'<sup>[\1]</sup>', processed)
        
        is_block = any(processed.strip().startswith(t) for t in ['<blockquote', '<ul', '<ol', '<pre', '<hr', '<div', '$$'])
        is_inline_tag = any(processed.strip().startswith(t) for t in ['<strong', '<em', '<code', '<a', '<span', '<img'])
        
        if (not is_block or is_inline_tag) and processed.strip():
            if not in_para:
                result.append(f'<p>{processed}')
                in_para = True
            else:
                result.append(' ' + processed)
        else:
            close_para()
            if processed.strip():
                result.append(processed)
    
    close_para()
    close_quote()
    close_list()
    flush_table()
    
    if footnotes:
        result.append('<hr><section class="footnotes">')
        for fn_id, content in footnotes.items():
            formatted_content = apply_inline_formatting(content)
            result.append(f'<p><small>[{fn_id}]: {formatted_content}</small></p>')
        result.append('</section>')
        
    return '\n'.join(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="full", choices=["full", "preview"])
    args = parser.parse_args()

    profile = get_profile(args.profile)
    model = ManuscriptModel(profile)

    docs_dir = Path('preview' if profile.is_preview else 'docs')
    docs_dir.mkdir(exist_ok=True)

    preview_notice = ""
    if profile.is_preview:
        preview_notice = '''<div class="preview-notice" style="background: #fff8c5; border: 1px solid #d4a72c; padding: 1rem; border-radius: 6px; margin-bottom: 2rem; font-size: 0.9rem;">
      <strong>先行公開版のお知らせ:</strong> このドキュメントは先行公開用であり、正式な公開範囲は前付け・第1章・後付類のみです。第2章以降の本文は、現在、誤字脱字、全体の整合性、数学的厳密性と教育的な断言のバランスを調整している最中です。GitHub リポジトリや作業中ブランチを探すと全12章分の草稿が見えてしまう可能性がありますが、それらは正式な公開版ではありません。どうしても読む場合は、こっそり作業場を覗き見たものとして扱い、現時点では批評・レビュー・拡散の対象にしないでください。最新版や正式な公開情報はポータルサイトをご確認ください。
    </div>'''

    all_chapters_for_nav = model.front_matter + model.get_full_toc_chapters()

    # --- Build Sidebar TOC ---
    toc_html_parts = ["<ul>"]
    toc_html_parts.append('<li class="level-1"><a href="toc.html" id="link-toc.html">目次</a></li>')
    for ch in all_chapters_for_nav:
        css_class = "" if ch.is_included_in_content else ' class="disabled-link" title="完結版に収録予定"'
        href = ch.filename if ch.is_included_in_content else '#'
        toc_html_parts.append(f'<li class="level-1"><a href="{href}" id="link-{ch.filename}"{css_class}>{ch.short_title}</a></li>')
    toc_html_parts.append("</ul>")
    base_toc_html = "\n".join(toc_html_parts)

    # --- Build Pages for Content Scope ---
    content_chapters = model.get_content_chapters()
    for i, ch in enumerate(content_chapters):
        # Build local sub-toc
        local_toc = ""
        if ch.toc_items:
            local_toc = '<ul class="sub-toc">'
            for item in ch.toc_items:
                local_toc += f'<li class="level-{item.level}"><a href="#{item.anchor}">{item.title}</a></li>'
            local_toc += '</ul>'

        # Prev/Next navigation within content scope
        prev_ch = content_chapters[i-1] if i > 0 else None
        next_ch = content_chapters[i+1] if i < len(content_chapters)-1 else None
        prev_btn = f'<a href="{prev_ch.filename}">← {prev_ch.short_title[:15]}...</a>' if prev_ch else '<span></span>'
        next_btn = f'<a href="{next_ch.filename}">{next_ch.short_title[:15]}... →</a>' if next_ch else '<span></span>'

        # Inject headings into markdown before processing
        # content_lines already contain the # Title as first line; do not duplicate
        md_text = "\n".join(ch.content_lines)

        content_html = process_markdown(md_text)

        # Highlight current page in sidebar
        active_marker = f'id="link-{ch.filename}"'
        page_toc = base_toc_html.replace(active_marker, f'class="active" {active_marker}')
        if local_toc:
            find_str = f'link-{ch.filename}">{ch.short_title}</a></li>'
            page_toc = page_toc.replace(find_str, find_str.replace('</li>', local_toc + '</li>'))

        final_html = HTML_TEMPLATE.format(
            title=(ch.title + " (先行公開版)" if profile.is_preview else ch.title),
            toc=page_toc,
            KATEX_CDN=KATEX_CDN,
            content=(preview_notice + "\n" + content_html if profile.is_preview and not ch.is_front_matter else content_html),
            prev_button=prev_btn,
            next_button=next_btn
        )
        with open(docs_dir / ch.filename, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"Generated {docs_dir / ch.filename}")

    # --- Build Full TOC Page (toc.html) ---
    toc_page_parts = []
    toc_page_parts.append('<h1>目次</h1>')
    if profile.is_preview:
        toc_page_parts.append('<p style="color: #666;">※ 先行公開版では第1章のみ公開しています。リンクのない章は完結版にて収録予定です。</p>')
    else:
        toc_page_parts.append('<p>各見出しはリンクになっており、クリックすると該当章の該当位置にジャンプします。</p>')
    
    toc_page_parts.append('<div class="full-toc">')

    part_info = {
        'I': ('ch01.html', 'ch05.html', '第I部：$\\mathbb{R}^3$ 上の微分形式（第1章〜第5章）'),
        'II': ('ch06.html', 'ch09.html', '第II部：ベクトル解析（第6章〜第9章）'),
        'III': ('ch10.html', 'ch12.html', '第III部：発展と統合（第10章〜第12章）'),
    }
    
    in_part = None
    for ch in model.get_full_toc_chapters():
        # Determine Part
        p = None
        for key, (start, end, label) in part_info.items():
            if start <= ch.filename <= end:
                p = key
                break

        if p and p != in_part:
            if in_part:
                toc_page_parts.append('</div></div>')
            _, _, label = part_info[p]
            toc_page_parts.append(f'<div class="toc-part"><h2 class="part-header">{label}</h2><div class="toc-part-chapters">')
            in_part = p
        elif not p and in_part:
            toc_page_parts.append('</div></div>')
            in_part = None

        heading_level = 'h3' if p else 'h2'
        
        if ch.is_included_in_content:
            toc_page_parts.append(f'<{heading_level}><a href="{ch.filename}">{ch.title}</a></{heading_level}>')
        else:
            toc_page_parts.append(f'<{heading_level}><span class="disabled-link">{ch.title}</span></{heading_level}>')

        if ch.toc_items:
            toc_page_parts.append('<ul>')
            for item in ch.toc_items:
                if ch.is_included_in_content:
                    toc_page_parts.append(f'<li class="level-{item.level}"><a href="{ch.filename}#{item.anchor}">{item.title}</a></li>')
                else:
                    toc_page_parts.append(f'<li class="level-{item.level}"><span class="disabled-link">{item.title}</span></li>')
            toc_page_parts.append('</ul>')

    if in_part:
        toc_page_parts.append('</div></div>')
    toc_page_parts.append('</div>')

    toc_page_toc = base_toc_html.replace('id="link-toc.html"', 'class="active" id="link-toc.html"')
    toc_page_html = HTML_TEMPLATE.format(
        title=('目次 (先行公開版)' if profile.is_preview else '目次'), 
        toc=toc_page_toc, 
        KATEX_CDN=KATEX_CDN,
        content='\n'.join(toc_page_parts), 
        prev_button='<span></span>', 
        next_button='<span></span>'
    )
    with open(docs_dir / 'toc.html', 'w', encoding='utf-8') as f:
        f.write(toc_page_html)
    print(f"Generated {docs_dir / 'toc.html'}")

    # For compatibility with legacy processes, output combined MD of content scope
    combined_md_path = Path('exports/manuscript_preview_combined.md' if profile.is_preview else 'exports/manuscript_combined.md')
    combined_md_path.parent.mkdir(exist_ok=True)
    with open(combined_md_path, 'w', encoding='utf-8') as f:
        for ch in content_chapters:
            if not ch.is_front_matter:
                f.write(f"# {ch.title}\n\n")
            f.write("\n".join(ch.content_lines) + "\n\n")

if __name__ == '__main__':
    main()
