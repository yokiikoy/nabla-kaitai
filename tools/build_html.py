#!/usr/bin/env python3
"""
Generate HTML from manuscript_combined.md with proper MathJax support.
This script replaces the manually-edited docs/index.html approach with
an automated pipeline that correctly handles math in both body and sidebar TOC.
"""

import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    print("Error: markdown package not found. Install with: pip install markdown")
    sys.exit(1)


MATHJAX_CONFIG = '''window.MathJax = {
  loader: { load: ['[tex]/bm'] },
  tex: {
    inlineMath: [['$', '$']],
    displayMath: [['$$', '$$']],
    processEscapes: false,
    packages: { '[+]': ['bm'] }
  },
  options: { skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'] }
};
'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ナブラ解体新書</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5/github-markdown.min.css">
<style>
  :root {{ --sidebar-width: 320px; }}
  body {{ margin: 0; display: flex; background: #fff; line-height: 1.7; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
  .sidebar {{ width: var(--sidebar-width); height: 100vh; position: sticky; top: 0; background: #f8f9fa; border-right: 1px solid #d0d7de; overflow-y: auto; padding: 1.5rem; box-sizing: border-box; flex-shrink: 0; }}
  .sidebar h2 {{ font-size: 1.2rem; border: none; margin-bottom: 1rem; color: #24292f; }}
  .sidebar .toc {{ font-size: 0.85rem; }}
  .sidebar .toc ul {{ list-style: none; padding-left: 1rem; }}
  .sidebar a {{ text-decoration: none; color: #0969da; }}
  .main-content {{ flex: 1; min-width: 0; padding: 2rem 4rem; overflow-x: hidden; }}
  .markdown-body {{ max-width: 850px; margin: 0 auto; }}
  @media (max-width: 900px) {{ body {{ flex-direction: column; }} .sidebar {{ width: 100%; height: auto; position: static; }} .main-content {{ padding: 1.5rem; }} }}
  blockquote {{ border-left: 4px solid #d0d7de; color: #57606a; background: #f6f8fa; padding: 0.5em 1.2em; margin: 1.5em 0; border-radius: 0 6px 6px 0; }}
  .mjx-container {{ overflow-x: auto !important; padding: 0.8em 0; max-width: 100%; }}
</style>
<script>
{MATHJAX_CONFIG}
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
  <nav class="sidebar">
    <h2>ナブラ解体新書</h2>
    <div class="toc">{toc}</div>
    <hr style="border:none; border-top:1px solid #d0d7de; margin: 1.5rem 0;">
    <p style="font-size:0.8rem; color:#666;">著者: yokiikoy<br>License: CC BY-NC 4.0</p>
  </nav>
  <main class="main-content">
    <article class="markdown-body">{content}</article>
  </main>
</body>
</html>'''


def slugify(text):
    """Convert text to a URL-safe slug for heading IDs."""
    text = text.replace('$', '')
    text = re.sub(r'\$[^$]+\$', '', text)
    text = re.sub(r'\\[^\\]+', '', text)
    text = re.sub(r'[{}\\[\\]()（）——–—ー・。、,!?！?]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    text = re.sub(r'[^a-zA-Z0-9\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF-]', '', text)
    if not text:
        text = 'section'
    return text


def extract_toc(markdown_text):
    """Extract table of contents from markdown headings."""
    toc_entries = []
    heading_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)

    for match in heading_pattern.finditer(markdown_text):
        level = len(match.group(1))
        heading_text = match.group(2).strip()

        heading_text_clean = re.sub(r'^(\d+(?:\.\d+)*\s*)', '', heading_text)
        numbered = heading_text != heading_text_clean

        anchor = slugify(heading_text)
        if not anchor:
            anchor = 'section'

        indent = '  ' * (level - 1)
        toc_entries.append((level, heading_text, anchor, numbered))

    return toc_entries


def build_toc_html(toc_entries):
    """Build HTML TOC from extracted entries."""
    result = []
    stack = [result]

    for level, text, anchor, numbered in toc_entries:
        if level == 1:
            continue

        while len(stack) > level:
            stack.pop()

        while len(stack) < level:
            current = stack[-1]
            current.append('<ul>')
            new_list = []
            current.append(new_list)
            stack.append(new_list)

        href = f'#{anchor}'
        display_text = text.strip()
        stack[-1].append(f'<li><a href="{href}">{display_text}</a>')

    while len(stack) > 1:
        stack.pop()

    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    flat_result = flatten(result)
    flat_result.append('</ul>')
    flat_result.append('</div>')

    return '\n'.join(flat_result)


def process_markdown(markdown_text):
    """Process markdown to HTML with proper handling."""
    md = markdown.Markdown(extensions=['extra'], extension_configs={
        'extra': {' BREAK_ON_BLANKLINE': False, 'ENABLE_ATTRIBUTES': True}
    })

    html = md.convert(markdown_text)

    html = add_heading_ids(html)

    return html


def add_heading_ids(html):
    """Add IDs to headings to match TOC anchors."""
    def replace_heading(match):
        tag = match.group(1)
        content = match.group(2)
        anchor = slugify(content)
        if not anchor:
            anchor = 'section'
        return f'<h{tag} id="{anchor}">{content}</h{tag}>'

    html = re.sub(r'<h([1-6])>(.+?)</h[1-6]>', replace_heading, html)
    return html


def main():
    md_path = Path('exports/manuscript_combined.md')
    output_path = Path('docs/index.html')

    if not md_path.exists():
        print(f"Error: {md_path} not found")
        sys.exit(1)

    print(f"Reading {md_path}...")
    with open(md_path, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    print("Extracting TOC...")
    toc_entries = extract_toc(markdown_text)
    print(f"  Found {len(toc_entries)} headings")

    print("Building TOC HTML...")
    toc_html = build_toc_html(toc_entries)

    print("Processing markdown to HTML...")
    content_html = process_markdown(markdown_text)

    print("Generating final HTML...")
    final_html = HTML_TEMPLATE.format(
        MATHJAX_CONFIG=MATHJAX_CONFIG,
        toc=toc_html,
        content=content_html
    )

    print(f"Writing {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"Done! Generated {output_path}")


if __name__ == '__main__':
    main()