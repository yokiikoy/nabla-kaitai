#!/usr/bin/env python3
"""
Generate HTML from manuscript_combined.md with proper MathJax support.
Uses regex-based conversion to preserve LaTeX math content intact.
"""

import re
import sys
from pathlib import Path


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
<script id="MathJax-script" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</head>
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


class MathProtector:
    """Protect math content from markdown processing."""

    def __init__(self):
        self.math_blocks = []
        self.inline_math = []

    def protect(self, text):
        """Replace math with placeholders and store original content."""
        def replace_display(match):
            idx = len(self.math_blocks)
            content = match.group(0)
            self.math_blocks.append(content)
            # Use a unique class to ensure MathJax processes it
            return f'\n\n<div class="math-block tex2jax_process">MATH_BLOCK_{idx}_END</div>\n\n'

        def replace_inline(match):
            idx = len(self.inline_math)
            self.inline_math.append(match.group(0))
            return f'<span class="tex2jax_process">INLINE_MATH_{idx}_END</span>'

        text = re.sub(r'\$\$[\s\S]+?\$\$', replace_display, text)
        text = re.sub(r'(?<!\\)\$[^$\n]+?(?<!\\)\$', replace_inline, text)

        return text

    def restore(self, text):
        """Restore math content from stored placeholders."""
        for i, block in enumerate(self.math_blocks):
            text = text.replace(f'MATH_BLOCK_{i}_END', block)
        for i, math in enumerate(self.inline_math):
            text = text.replace(f'INLINE_MATH_{i}_END', math)
        return text


def slugify(text):
    """Convert text to a URL-safe slug for heading IDs."""
    text = re.sub(r'\$[^$]*\$', '', text)
    text = re.sub(r'\\[^\\]+', '', text)
    text = re.sub(r'[{}\\[\\]()（）——–—ー・。、,!?！？]', '', text)
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
        anchor = slugify(heading_text)
        if not anchor:
            anchor = 'section'
        toc_entries.append((level, heading_text, anchor))

    return toc_entries


def build_toc_html(toc_entries):
    """Build HTML TOC from extracted entries."""
    result = []
    stack = [result]

    for level, text, anchor in toc_entries:
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


def process_markdown(markdown_text, heading_anchors):
    """Convert markdown to HTML using regex-based processing.
    
    heading_anchors: dict mapping heading text (original, with math) to anchor slug
    """
    protector = MathProtector()
    text = protector.protect(markdown_text)

    lines = text.split('\n')
    result = []
    in_code_block = False
    in_blockquote = False
    in_list = False
    in_paragraph = False

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.strip().startswith('```'):
            if not in_code_block:
                result.append('<pre><code>')
                in_code_block = True
                i += 1
                continue
            else:
                result.append('</code></pre>')
                in_code_block = False
                i += 1
                continue

        if in_code_block:
            result.append(line)
            i += 1
            continue

        heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if heading_match:
            level = len(heading_match.group(1))
            content = heading_match.group(2).strip()
            restored_content = protector.restore(content)
            anchor = heading_anchors.get(restored_content, slugify(restored_content))
            if not anchor:
                anchor = 'section'
            result.append(f'<h{level} id="{anchor}">{restored_content}</h{level}>')
            in_paragraph = False
            in_list = False
            i += 1
            continue

        if line.strip() == '---':
            result.append('<hr />')
            in_paragraph = False
            in_list = False
            i += 1
            continue

        if line.strip().startswith('>'):
            content = protector.restore(line[1:].strip())
            if in_blockquote:
                result.append(content)
            else:
                result.append(f'<blockquote><p>{content}</p>')
                in_blockquote = True
            in_paragraph = False
            i += 1
            continue
        elif in_blockquote:
            result.append('</p></blockquote>')
            in_blockquote = False

        if line.strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')) and not in_list:
            num = re.match(r'^(\d+)\.\s*(.*)', line.strip())
            if num:
                if not in_list:
                    result.append('<ol>')
                    in_list = True
                result.append(f'<li>{protector.restore(num.group(2))}</li>')
                in_paragraph = False
                i += 1
                continue
        elif in_list:
            result.append('</ol>')
            in_list = False

        list_match = re.match(r'^[-*]\s+(.*)', line)
        if list_match:
            if not in_list:
                result.append('<ul>')
                in_list = True
            result.append(f'<li>{protector.restore(list_match.group(1))}</li>')
            in_paragraph = False
            i += 1
            continue
        elif in_list:
            result.append('</ul>')
            in_list = False

        if line.strip() == '':
            if in_paragraph:
                result.append('</p>')
                in_paragraph = False
            if in_blockquote:
                result.append('</p></blockquote>')
                in_blockquote = False
            i += 1
            continue

        inline_patterns = [
            (r'\*\*(.+?)\*\*', r'<strong>\1</strong>'),
            (r'\*(.+?)\*', r'<em>\1</em>'),
            (r'`(.+?)`', r'<code>\1</code>'),
        ]

        processed = line
        for pattern, replacement in inline_patterns:
            processed = re.sub(pattern, replacement, processed)

        restored_processed = protector.restore(processed)

        if not restored_processed.strip().startswith('<') and restored_processed.strip():
            if not in_paragraph:
                result.append(f'<p>{restored_processed}')
                in_paragraph = True
            else:
                result.append(restored_processed)
        else:
            if in_paragraph:
                result.append('</p>')
                in_paragraph = False
            result.append(restored_processed)

        i += 1

    if in_paragraph:
        result.append('</p>')
    if in_blockquote:
        result.append('</p></blockquote>')
    if in_list:
        result.append('</ul>' if not result or '</ol>' not in result[-1] else '</ol>')

    html = '\n'.join(result)

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

    heading_anchors = {text: anchor for level, text, anchor in toc_entries}

    print("Building TOC HTML...")
    toc_html = build_toc_html(toc_entries)

    print("Processing markdown to HTML...")
    content_html = process_markdown(markdown_text, heading_anchors)

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