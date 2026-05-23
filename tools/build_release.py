#!/usr/bin/env python3
"""Build Japanese and English release artifacts for GitHub Pages and GitHub Releases."""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd):
    print(f"\n$ {' '.join(cmd)}")
    subprocess.run(cmd, cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--html-only', action='store_true', help='Skip PDF builds')
    parser.add_argument('--pdf-only', action='store_true', help='Skip HTML builds')
    args = parser.parse_args()

    py = sys.executable
    if not args.pdf_only:
        run([py, 'tools/build_html.py', '--lang', 'ja'])
        run([py, 'tools/build_html.py', '--lang', 'en'])
    if not args.html_only:
        run([py, 'tools/build_pdf.py', '--lang', 'ja'])
        run([py, 'tools/build_pdf.py', '--lang', 'en'])

    ja_pdf = ROOT / 'exports' / 'manuscript.pdf'
    if ja_pdf.exists():
        shutil.copy2(ja_pdf, ROOT / 'manuscript.pdf')
        print(f'Copied {ja_pdf} → manuscript.pdf')

    print('\nRelease artifacts ready.')


if __name__ == '__main__':
    main()
