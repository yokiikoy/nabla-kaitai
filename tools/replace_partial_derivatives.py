#!/usr/bin/env python3
"""
Replace subscript partial derivative notation (P_x) with explicit \frac{\partial P}{\partial x}
in source and note files for chapters 03, 04, 05.

Usage: python3 replace_partial_derivatives.py [--dry-run]
"""

import re
import sys
from pathlib import Path

MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript" / "ja"

def mk_repl(repl_str):
    """Return a callable that always returns repl_str (avoids re.sub escape processing)."""
    return lambda m: repl_str

# Replacement mapping: (pattern, replacement)
# Use function callables to avoid re.sub escape interpretation of backslashes.
REPLACEMENTS = {
    re.compile(r'\bP_x\b'): mk_repl(r'\frac{\partial P}{\partial x}'),
    re.compile(r'\bP_y\b'): mk_repl(r'\frac{\partial P}{\partial y}'),
    re.compile(r'\bP_z\b'): mk_repl(r'\frac{\partial P}{\partial z}'),
    re.compile(r'\bQ_x\b'): mk_repl(r'\frac{\partial Q}{\partial x}'),
    re.compile(r'\bQ_y\b'): mk_repl(r'\frac{\partial Q}{\partial y}'),
    re.compile(r'\bQ_z\b'): mk_repl(r'\frac{\partial Q}{\partial z}'),
    re.compile(r'\bR_x\b'): mk_repl(r'\frac{\partial R}{\partial x}'),
    re.compile(r'\bR_y\b'): mk_repl(r'\frac{\partial R}{\partial y}'),
    re.compile(r'\bR_z\b'): mk_repl(r'\frac{\partial R}{\partial z}'),
    re.compile(r'\bf_x\b'): mk_repl(r'\frac{\partial f}{\partial x}'),
    re.compile(r'\bf_y\b'): mk_repl(r'\frac{\partial f}{\partial y}'),
    re.compile(r'\bf_z\b'): mk_repl(r'\frac{\partial f}{\partial z}'),
    re.compile(r'\bA_x\b'): mk_repl(r'\frac{\partial A}{\partial x}'),
    re.compile(r'\bA_y\b'): mk_repl(r'\frac{\partial A}{\partial y}'),
    re.compile(r'\bA_z\b'): mk_repl(r'\frac{\partial A}{\partial z}'),
    re.compile(r'\bB_x\b'): mk_repl(r'\frac{\partial B}{\partial x}'),
    re.compile(r'\bB_y\b'): mk_repl(r'\frac{\partial B}{\partial y}'),
    re.compile(r'\bB_z\b'): mk_repl(r'\frac{\partial B}{\partial z}'),
    re.compile(r'\bC_x\b'): mk_repl(r'\frac{\partial C}{\partial x}'),
    re.compile(r'\bC_y\b'): mk_repl(r'\frac{\partial C}{\partial y}'),
    re.compile(r'\bC_z\b'): mk_repl(r'\frac{\partial C}{\partial z}'),
}

PARAM_REPLACEMENTS = {
    re.compile(r'\bx_u\b'): mk_repl(r'\frac{\partial x}{\partial u}'),
    re.compile(r'\bx_v\b'): mk_repl(r'\frac{\partial x}{\partial v}'),
    re.compile(r'\by_u\b'): mk_repl(r'\frac{\partial y}{\partial u}'),
    re.compile(r'\by_v\b'): mk_repl(r'\frac{\partial y}{\partial v}'),
    re.compile(r'\bz_u\b'): mk_repl(r'\frac{\partial z}{\partial u}'),
    re.compile(r'\bz_v\b'): mk_repl(r'\frac{\partial z}{\partial v}'),
}


def apply_replacements(text: str, replacements: dict) -> str:
    for pattern, repl_fn in replacements.items():
        text = pattern.sub(repl_fn, text)
    return text


def process_file(filepath: Path, dry_run: bool = False) -> int:
    if not filepath.exists():
        print(f"  SKIP (not found): {filepath}")
        return 0

    content = filepath.read_text(encoding='utf-8')
    original = content

    content = apply_replacements(content, REPLACEMENTS)
    content = apply_replacements(content, PARAM_REPLACEMENTS)

    changes = (content != original)
    if changes:
        count = content.count(r'\frac{\partial')
        if dry_run:
            print(f"  Would change: {filepath} ({count} replacements)")
        else:
            filepath.write_text(content, encoding='utf-8')
            print(f"  CHANGED: {filepath} ({count} replacements)")
        return count
    else:
        print(f"  No changes: {filepath}")
        return 0


def main():
    dry_run = '--dry-run' in sys.argv

    files = []
    for ch in ['ch03', 'ch04', 'ch05']:
        source = MANUSCRIPT / ch / f"{ch}.md"
        note = MANUSCRIPT / f"{ch}_note.md"
        files.append(source)
        files.append(note)

    print("Dry run" if dry_run else "Applying replacements...")
    print("=" * 60)

    total = 0
    for f in files:
        total += process_file(f, dry_run)

    print("=" * 60)
    print(f"Total replacements: {total}" if not dry_run else f"Would make {total} replacements")


if __name__ == '__main__':
    main()
