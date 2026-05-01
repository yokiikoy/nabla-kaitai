#!/usr/bin/env python3
"""Restore manuscript chapter files from the combined markdown export.

The combined file (exports/manuscript_combined.md) was generated from the
user's working tree before the git checkout regression.  This script
extracts each chapter's body content and merges it back with the YAML
frontmatter preserved in the git-committed files.
"""
import re, os, sys

COMBINED = 'exports/manuscript_combined.md'
MANUSCRIPT_DIR = 'manuscript/ja'

# ---- 1. Split combined file into named sections ----
with open(COMBINED, encoding='utf-8') as f:
    combined_text = f.read()

# Split by \newpage to get individual blocks
blocks = combined_text.split(r'\newpage')

# Identify each block by its first heading
chapter_map = {}  # heading text -> block content (stripped)
for block in blocks:
    block = block.strip()
    if not block:
        continue
    first_line = block.split('\n')[0].strip()
    chapter_map[first_line] = block

def find_block(prefix):
    """Find a block whose first line starts with the given prefix."""
    for heading, content in chapter_map.items():
        if heading.startswith(prefix):
            return content
    return None

# ---- 2. For each file in the manuscript, extract YAML and merge ----
files_to_restore = {
    'preface':       '# はじめに',
    'ch01/ch01':     '# 第1章：',
    'ch02/ch02':     '# 第2章：',
    'ch03/ch03':     '# 第3章：',
    'ch04/ch04':     '# 第4章：',
    'ch05/ch05':     '# 第5章：',
    'ch06/ch06':     '# 第6章：',
    'ch07/ch07':     '# 第7章：',
    'ch08/ch08':     '# 第8章：',
    'ch09/ch09':     '# 第9章：',
    'ch10/ch10':     '# 第10章：',
    'ch11/ch11':     '# 第11章：',
    'ch12/ch12':     '# 第12章：',
    'afterword':     '# おわりに',
    'references':    '# 参考文献',
    'appendix':      '# 付録',
}

for rel_path, prefix in files_to_restore.items():
    src_path = f'{MANUSCRIPT_DIR}/{rel_path}.md'
    if not os.path.exists(src_path):
        print(f'  SKIP {src_path} (not found)')
        continue

    # Read existing file to extract YAML frontmatter
    with open(src_path, encoding='utf-8') as f:
        old_text = f.read()

    yaml_end = 0
    if old_text.startswith('---'):
        end = old_text.find('---', 3)
        if end > 0:
            yaml_end = end + 3

    yaml_frontmatter = old_text[:yaml_end].strip()

    # Find the body content from the combined file
    body = find_block(prefix)
    if body is None:
        print(f'  FAIL {prefix} (not found in combined)')
        continue

    # Remove the first heading from body (it will be re-added as part of the content)
    # Actually the body starts with the heading, which is correct for the manuscript file
    # The YAML frontmatter is separate

    if yaml_frontmatter:
        new_text = yaml_frontmatter + '\n\n\n' + body + '\n'
    else:
        new_text = body + '\n'

    with open(src_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print(f'  RESTORED {src_path}')

print('\nDone.')
