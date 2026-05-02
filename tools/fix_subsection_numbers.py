#!/usr/bin/env python3
"""Fix #### X.Y.Z subsection numbering that lags behind section/chapter renumbering."""

import re, os

MANUSCRIPT_DIR = 'manuscript/ja'

# Mapping: file -> (old_X, new_X) or (chapter, old_Y_minus, new_Y_minus)
# ch03: Y off by +1 (3.2.x → 3.1.x etc.)
# ch05..ch09, ch11..ch12: X off by -1 (4.y.z → 5.y.z etc.)
FIXES = [
    ('ch03/ch03.md', 'chapter', 3, -1),   # decrement Y by 1
    ('ch05/ch05.md', 'chapter_x', 4, 5),  # change X from 4 to 5
    ('ch06/ch06.md', 'chapter_x', 5, 6),
    ('ch07/ch07.md', 'chapter_x', 6, 7),
    ('ch08/ch08.md', 'chapter_x', 7, 8),
    ('ch09/ch09.md', 'chapter_x', 8, 9),
    ('ch11/ch11.md', 'chapter_x', 10, 11),
    ('ch12/ch12.md', 'chapter_x', 11, 12),
]

total = 0
for rel_path, fix_type, old_val, new_val in FIXES:
    filepath = f'{MANUSCRIPT_DIR}/{rel_path}'
    if not os.path.exists(filepath):
        print(f'  SKIP {filepath} (not found)')
        continue

    with open(filepath, encoding='utf-8') as f:
        text = f.read()

    original = text

    if fix_type == 'chapter':
        # ch03: decrement Y in #### 3.Y.Z → #### 3.(Y-1).Z
        def dec_y(m):
            y = int(m.group(1)) + new_val  # new_val is -1
            return f'#### {old_val}.{y}.{m.group(2)} '
        text = re.sub(
            rf'^#### {old_val}\.(\d+)\.(\d+) ',
            dec_y, text, flags=re.MULTILINE
        )
    elif fix_type == 'chapter_x':
        # Replace X in #### X.Y.Z
        text = re.sub(
            rf'^#### {old_val}\.(\d+)\.(\d+) ',
            rf'#### {new_val}.\1.\2 ', text, flags=re.MULTILINE
        )

    if text != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        changes = len(re.findall(r'^#### ', text, re.MULTILINE)) - len(re.findall(r'^#### ', original, re.MULTILINE))
        total += 1
        print(f'  FIXED {rel_path}')
    else:
        print(f'  (no change) {rel_path}')

print(f'\nFiles fixed: {total}')
