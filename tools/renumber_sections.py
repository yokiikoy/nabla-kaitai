#!/usr/bin/env python3
"""Renumber sections: ch01 §1.1→§1.0, ch03 §3.1→§3.0 (single-pass, no cascade)."""

import re, os

MANUSCRIPT_DIR = 'manuscript/ja'
FILES = (
    [f'{MANUSCRIPT_DIR}/preface.md'] +
    [f'{MANUSCRIPT_DIR}/ch{i:02d}/ch{i:02d}.md' for i in range(1, 13)] +
    [f'{MANUSCRIPT_DIR}/{s}.md' for s in ('afterword', 'references', 'appendix')] +
    [f'{MANUSCRIPT_DIR}/toc.md']
)

def decrement_section(text, chapter, lo, hi):
    """Replace §{chapter}.{n} → §{chapter}.{n-1} for n in lo..hi, single pass."""
    def repl(m):
        n = int(m.group(1))
        return f'§{chapter}.{n - 1}'
    pattern = rf'§{chapter}\.([{lo}-{hi}])(?!\d)'
    return re.sub(pattern, repl, text)

total = 0
for f in FILES:
    if not os.path.exists(f):
        continue
    with open(f, encoding='utf-8') as fh:
        text = fh.read()
    original = text

    # ch01: §1.1..§1.7 → §1.0..§1.6
    text = decrement_section(text, 1, 1, 7)
    # ch03: §3.1..§3.6 → §3.0..§3.5
    text = decrement_section(text, 3, 1, 6)

    if text != original:
        count = sum(1 for a, b in zip(original, text) if a != b)
        # rough count; good enough
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(text)
        total += 1
        print(f'  MODIFIED {f}')
    else:
        print(f'  (no change) {f}')

print(f'\nFiles modified: {total}')
