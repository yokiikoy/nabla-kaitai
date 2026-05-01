#!/usr/bin/env python3
"""Generate PDF from manuscript using Pandoc → XeLaTeX."""
import subprocess, os, re, glob
from datetime import datetime

# Build combined markdown
files = []
for prefix in ['preface']:
    f = f'manuscript/ja/{prefix}.md'
    if os.path.exists(f):
        files.append(f)
for i in range(1, 13):
    f = f'manuscript/ja/ch{i:02d}/ch{i:02d}.md'
    if os.path.exists(f):
        files.append(f)
for suffix in ['afterword', 'references', 'appendix']:
    f = f'manuscript/ja/{suffix}.md'
    if os.path.exists(f):
        files.append(f)


def strip_yaml(content):
    if content.startswith('---'):
        end = content.find('---', 3)
        if end > 0:
            return content[end+3:].lstrip()
    return content


os.makedirs('exports', exist_ok=True)

combined = []
for f in files:
    with open(f) as fh:
        content = fh.read()
    content = strip_yaml(content)
    combined.append(content)
    combined.append('\n\n\\newpage\n\n')

md_text = '\n'.join(combined)

# Convert HTML <strong> tags to Pandoc-native **bold** syntax.
# Pandoc with format=markdown (raw_html enabled by default) passes raw HTML
# through to LaTeX output literally, which renders as text, not bold.
# Stripping raw_html would discard the tags entirely.  Pre-processing to
# the native syntax ensures Pandoc emits \textbf{...} in LaTeX.
md_text = re.sub(r'<strong>\s*(.*?)\s*</strong>', r'**\1**', md_text, flags=re.DOTALL)

with open('exports/manuscript_combined.md', 'w') as f:
    f.write(md_text)

print(f'Combined {len(files)} chapters → exports/manuscript_combined.md')

# Pandoc's markdown parser often requires a blank line before a list or
# heading when it follows certain constructs (HTML tags, blockquotes, etc.).
# Ensure blank lines before headings and list items.
def ensure_blank_lines_before_structures(text):
    lines = text.split('\n')
    result = []
    list_markers = ('* ', '- ', '+ ')
    heading_markers = ('# ', '## ', '### ', '#### ', '##### ', '###### ')

    for i, line in enumerate(lines):
        stripped = line.lstrip()
        prev = lines[i - 1] if i > 0 else ''
        prev_stripped = prev.lstrip()

        # Normal list: blank line before the first item
        if (stripped.startswith(list_markers)
                and prev_stripped != ''
                and not prev_stripped.startswith('```')
                and not prev_stripped.endswith('>')):
            result.append('')

        # Blockquote list: ">"-only line before the first item
        if (line.startswith('> ') and line[2:].startswith(list_markers)
                and prev.startswith('>')
                and prev.strip() != '>'):
            result.append('>')

        # Headings: blank line before when previous line is non-empty
        # and ends with an HTML tag (which confuses Pandoc's parser)
        if (stripped.startswith(heading_markers)
                and prev_stripped != ''
                and not prev_stripped.startswith('```')):
            result.append('')

        result.append(line)
    return '\n'.join(result)

md_text = ensure_blank_lines_before_structures(md_text)


def git_text(args, default=''):
    result = subprocess.run(
        ['git'] + args,
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return default
    return result.stdout.strip() or default


def latex_escape(value):
    replacements = {
        '\\': r'\textbackslash{}',
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
    }
    return ''.join(replacements.get(char, char) for char in value)


build_datetime = datetime.now().strftime('%Y-%m-%d %H:%M JST')
author_name = 'yokiikoy'
last_commit = git_text(['log', '-1', '--format=%h (%ad)', '--date=short'], '未取得')
dirty_status = git_text(['status', '--short'])
working_tree_note = '未コミット変更あり' if dirty_status else 'クリーン'
git_log = git_text(['log', '-3', '--format=%h (%ad)  %s', '--date=short'], '未取得')
log_lines = [l.strip() for l in git_log.split('\n') if l.strip()]
# Pad to exactly 3 lines
while len(log_lines) < 3:
    log_lines.append('')

# Generate LaTeX via Pandoc
try:
    from pypandoc import convert_text

    latex_body = convert_text(
        md_text, 'latex',
        format='markdown+tex_math_dollars',
        extra_args=[
            '--to=latex',
            '--top-level-division=chapter',
            '--variable=documentclass=article',
            '--wrap=none',
        ]
    )

    def rewrite_front_back_matter_chapters(text):
        """Keep preface/toc/afterword/references from incrementing chapter numbers."""
        result = []
        cursor = 0
        chapter_index = 0
        unnumbered = {0, len(files) - 2, len(files) - 1}
        # Identify chapter titles by their text for part insertion
        insert_before = {
            '第1章': r'\part{第I部：$\mathbb{R}^3$ 上の微分形式}' '\n',
            '第6章': r'\part{第II部：ベクトル解析}' '\n',
            '第10章': r'\part{第III部：発展と統合}' '\n',
        }

        while True:
            start = text.find(r'\chapter', cursor)
            if start == -1:
                result.append(text[cursor:])
                break

            brace_start = text.find('{', start)
            if brace_start == -1:
                result.append(text[cursor:])
                break

            depth = 1
            pos = brace_start + 1
            while pos < len(text) and depth > 0:
                if text[pos] == '\\':
                    pos += 2
                    continue
                if text[pos] == '{':
                    depth += 1
                elif text[pos] == '}':
                    depth -= 1
                pos += 1

            command = text[start:pos]
            title = text[brace_start + 1:pos - 1]

            # Insert part command before chapter if title matches
            part_cmd = None
            for key, value in insert_before.items():
                ch_num = key[1:-1]
                if re.search(r'第' + ch_num + r'章[^0-9]', title):
                    part_cmd = value
                    break

            result.append(text[cursor:start])
            if part_cmd:
                result.append(part_cmd)

            if chapter_index in unnumbered:
                result.append(r'\chapter*{' + title + '}' '\n')
                result.append(r'\addcontentsline{toc}{chapter}{' + title + '}' '\n')
            else:
                result.append(command)

            chapter_index += 1
            cursor = pos

        return ''.join(result)

    latex_body = rewrite_front_back_matter_chapters(latex_body)

    def fit_wide_display_math(text):
        """Shrink display-math matrix blocks only when they exceed the text width."""
        def repl(match):
            body = match.group(1).strip()
            is_wide_matrix = 'pmatrix' in body
            is_many_matrices = body.count(r'\begin{pmatrix}') >= 2
            if not (is_wide_matrix or is_many_matrices):
                return match.group(0)
            return (
                r'\begin{center}' '\n'
                r'\adjustbox{max width=0.98\linewidth}{\(\displaystyle '
                + body +
                r'\)}' '\n'
                r'\end{center}'
            )

        return re.sub(r'\\\[(.*?)\\\]', repl, text, flags=re.DOTALL)

    latex_body = fit_wide_display_math(latex_body)

    def soften_horizontal_rules(text):
        """Make Markdown --- separators nearly invisible in the PDF."""
        return text.replace(
            r'\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}',
            r'\par\vspace{0.35em}\par'
        )

    latex_body = soften_horizontal_rules(latex_body)

    def hide_appendix_from_toc(text):
        """Appendix subsections (A.x–E.x) should not appear in the TOC."""
        # \subsection{A.1 ...} -> \subsection*{A.1 ...}
        # \subsection{\texorpdfstring{A.1 ...} -> \subsection*{\texorpdfstring{A.1 ...}
        # \subsubsection{A.1 ...} -> \subsubsection*{A.1 ...}
        for cmd in ('subsection', 'subsubsection', 'paragraph'):
            for letter in 'ABCDE':
                # Direct: \cmd{X. ...}
                text = re.sub(
                    rf'\\{cmd}\{{({letter}\.)',
                    rf'\\{cmd}*{{\1',
                    text
                )
                # Wrapped in \texorpdfstring: \cmd{\texorpdfstring{X. ...}
                text = re.sub(
                    rf'\\{cmd}\{{(\\\\texorpdfstring\{{{letter}\.)',
                    rf'\\{cmd}*{{\1',
                    text
                )
        return text

    latex_body = hide_appendix_from_toc(latex_body)

    def fix_dashes(text):
        """Pandoc converts U+2014 em dashes to ASCII '------'.
        XeLaTeX does not reliably form ligatures inside CJK fonts,
        so we restore the original Unicode em dash characters."""
        em = '\u2014'
        en = '\u2013'
        text = text.replace('------', em + em)
        text = text.replace('---', em)
        text = text.replace('--', en)
        return text

    latex_body = fix_dashes(latex_body)

    # --- Build final LaTeX document ---
    preamble = (
        r'\documentclass[a4paper,12pt,openany]{book}' '\n'
        r'\usepackage{amsmath,amssymb,bm}' '\n'
        r'\usepackage{esint,cancel}' '\n'
        r'\usepackage[no-math]{fontspec}' '\n'
        r'\setmainfont{IPAexMincho}[AutoFakeBold=1.5, Ligatures=TeX]' '\n'
        r'\setsansfont{IPAexGothic}[Ligatures=TeX]' '\n'
        r'\setmonofont{IPAexGothic}[Ligatures=TeX]' '\n'
        '% IPAex on this machine only exposes Regular faces, so strong text needs\n'
        '% an explicit fake-bold face instead of relying on generic bfseries.\n'
        r'\newfontface\strongface{IPAexGothic}[AutoFakeBold=4.0]' '\n'
        '% Enable Japanese line breaking with XeTeX primitives.  This keeps the\n'
        '% build independent of xeCJK/luatexja, which are not always installed.\n'
        r'\XeTeXlinebreaklocale "ja"' '\n'
        r'\XeTeXlinebreakskip=0pt plus 1pt minus 0.1pt' '\n'
        r'\usepackage{geometry}' '\n'
        r'\geometry{margin=25mm}' '\n'
        r'\usepackage{fancyhdr}' '\n'
        r'\pagestyle{fancy}' '\n'
        r'\fancyhf{}' '\n'
        r'\fancyfoot[L]{\tiny CC BY-NC 4.0 \textcopyright\ yokiikoy}' '\n'
        r'\fancyfoot[C]{\thepage}' '\n'
        r'\fancypagestyle{plain}{\fancyhf{}\fancyfoot[L]{\tiny CC BY-NC 4.0 \textcopyright\ yokiikoy}\fancyfoot[C]{\thepage}\renewcommand{\headrulewidth}{0pt}}' '\n'
        r'\renewcommand{\headrulewidth}{0pt}' '\n'
        r'\usepackage{hyperref}' '\n'
        r'\hypersetup{colorlinks=true,linkcolor=blue}' '\n'
        r'\renewcommand{\contentsname}{目次}' '\n'
        r'\usepackage{longtable,booktabs,array,calc,multirow,colortbl}' '\n'
        r'\usepackage{graphicx}' '\n'
        r'\usepackage{adjustbox}' '\n'
        r'\usepackage{xcolor}' '\n'
        r'\usepackage{mdframed}' '\n'
        r'\usepackage{needspace}' '\n'
        r'\usepackage{etoolbox}' '\n'
        r'\usepackage{tocloft}' '\n'
        r'\usepackage{indentfirst}' '\n'
        r'\renewcommand{\cftchapdotsep}{\cftdotsep}' '\n'
        r'\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}' '\n'
        r'\renewcommand{\cftsubsecleader}{\cftdotfill{\cftdotsep}}' '\n'
        '\n'
        '% Pandoc fixes\n'
        r'\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}'
        '\n'
        r'\renewcommand{\textbf}[1]{{\strongface #1}}'
        '\n'
        '% Reduce awkward page breaks in prose-heavy output.\n'
        r'\clubpenalty=10000' '\n'
        r'\widowpenalty=10000' '\n'
        r'\displaywidowpenalty=10000' '\n'
        r'\brokenpenalty=10000' '\n'
        '\n'
        '% Render Markdown blockquotes/notes as subtle shaded callouts.\n'
        r'\definecolor{notebackground}{gray}{0.96}' '\n'
        r'\renewenvironment{quote}{%' '\n'
        r'  \Needspace{8\baselineskip}%' '\n'
        r'  \begin{mdframed}[' '\n'
        r'    backgroundcolor=notebackground,' '\n'
        r'    linecolor=notebackground,' '\n'
        r'    linewidth=0pt,' '\n'
        r'    leftmargin=0pt,rightmargin=0pt,' '\n'
        r'    innerleftmargin=1em,innerrightmargin=1em,' '\n'
        r'    innertopmargin=0.6em,innerbottommargin=0.6em,' '\n'
        r'    skipabove=0.8em,skipbelow=0.8em' '\n'
        r'  ]\small' '\n'
        r'}{\end{mdframed}}' '\n'
        '\n'
        '% Manuscript headings already include 第n章 and §n.n labels.\n'
        r'\setcounter{secnumdepth}{0}' '\n'
        r'\pretocmd{\section}{\Needspace{10\baselineskip}}{}{}' '\n'
        r'\pretocmd{\subsection}{\Needspace{12\baselineskip}}{}{}' '\n'
        r'\pretocmd{\subsubsection}{\Needspace{12\baselineskip}}{}{}' '\n'
        r'\pretocmd{\paragraph}{\Needspace{7\baselineskip}}{}{}' '\n'
        r'\makeatletter' '\n'
        r'\def\@makechapterhead#1{%' '\n'
        r'  \vspace*{50\p@}%' '\n'
        r'  {\parindent \z@ \raggedright \normalfont' '\n'
        r'    \interlinepenalty\@M' '\n'
        r'    \Huge \bfseries #1\par\nobreak' '\n'
        r'    \vskip 40\p@' '\n'
        r'  }}' '\n'
        r'\makeatother' '\n'
        '\n'
        '% Tolerate slight overfull boxes in math-heavy text\n'
        r'\setlength{\emergencystretch}{2em}' '\n'
        r'\tolerance=2000' '\n'
        r'\hbadness=5000' '\n'
        '\n'
        r'\begin{document}' '\n'
        r'\begin{titlepage}' '\n'
        r'\newgeometry{top=35mm,bottom=30mm,left=40mm,right=40mm}' '\n'
        r'\pagestyle{empty}' '\n'
        r'\centering' '\n'
        r'\vspace*{35mm}' '\n'
        r'{\fontsize{34}{42}\selectfont\bfseries ナブラ解体新書\par}' '\n'
        r'\vspace{12mm}' '\n'
        r'{\Large 行列表示の微分形式による\par}' '\n'
        r'{\Large ベクトル解析の抜け道\par}' '\n'
        r'\vspace{4mm}' '\n'
        r'{\normalsize v0.1.0-alpha\par}' '\n'
        r'\vspace{6mm}' '\n'
        r'\begin{minipage}{0.78\textwidth}' '\n'
        r'\centering' '\n'
        r'\small' '\n'
        r'\begin{tabular}{|l|p{0.6\textwidth}|}\hline' '\n'
        r'\multicolumn{2}{|c|}{\textbf{Versioning Policy}}\\ \hline' '\n'
        r'\textbf{v1.0.0} & 全12章の内容確定・相互参照の整合性完了・手計算による検算完了\\ \hline' '\n'
        r'\textbf{v2.0.0} & 図表の作成と配置完了・組版完了・印刷用データの出力\\ \hline' '\n'
        r'v0.x.0         & 章の追加・章構成の変更・大幅な書き直し\\ \hline' '\n'
        r'v0.0.x         & 注釈の追加・誤字修正・軽微な推敲\\ \hline' '\n'
        r'\end{tabular}\par\bigskip\bigskip\bigskip' '\n'
        r'\begin{tabular}{|p{\textwidth}|}\hline' '\n'
        + r'\multicolumn{1}{|c|}{\textbf{直近の改定履歴}}\\ \hline' '\n'
        + ''.join(
            r'{\small ' + latex_escape(line) + r'}\\ \hline' '\n'
            for line in log_lines if line
        )
        + r'\end{tabular}' '\n'
        r'\end{minipage}\par' '\n'
        r'\vfill' '\n'
        r'{\footnotesize ' + latex_escape(build_datetime) + r' --- 著者：' + latex_escape(author_name) + r'\par}' '\n'
        r'\restoregeometry' '\n'
        r'\end{titlepage}' '\n'
        r'\tableofcontents' '\n'
        r'\newpage' '\n'
    )
    latex_doc = preamble + latex_body + '\n' + r'\end{document}' + '\n'

    with open('exports/manuscript.tex', 'w') as f:
        f.write(latex_doc)
    print('LaTeX source → exports/manuscript.tex')

    # Post-process: hide appendix subsections from TOC
    with open('exports/manuscript.tex', 'r') as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        for cmd in ('subsection', 'subsubsection'):
            marker = rf'\{cmd}' + '{'
            idx = line.find(marker)
            if idx >= 0:
                rest = line[idx + len(marker):]
                m = re.search(rf'(\\\\texorpdfstring' + '{' + r')?[A-E]\.\d', rest)
                if m:
                    line = line.replace(marker, rf'\{cmd}*' + '{', 1)
        new_lines.append(line)
    with open('exports/manuscript.tex', 'w') as f:
        f.writelines(new_lines)

except Exception as e:
    print(f'LaTeX generation failed: {e}')
    import traceback
    traceback.print_exc()
    exit(1)

# Compile with xelatex (twice for TOC and cross-references)
print('\nCompiling with XeLaTeX...')
for run in [1, 2]:
    print(f'  Run {run}...')
    r = subprocess.run(
        ['xelatex', '-interaction=nonstopmode',
         '-output-directory=exports', 'exports/manuscript.tex'],
        capture_output=True, text=True, timeout=300
    )
    # Count warnings/errors
    warnings = r.stdout.count('Warning') + r.stderr.count('Warning')
    errors = r.stdout.count('Error') + r.stderr.count('Error')
    overfull = r.stdout.count('Overfull') + r.stderr.count('Overfull')
    print(f'    Warnings: {warnings}, Errors: {errors}, Overfull: {overfull}')
    if r.returncode != 0:
        print(r.stdout[-3000:])
        print(r.stderr[-3000:])
        raise SystemExit(r.returncode)

# Check output
pdf_path = 'exports/manuscript.pdf'
if os.path.exists(pdf_path):
    import os as _os
    size_mb = _os.path.getsize(pdf_path) / (1024*1024)
    print(f'\nPDF generated: {pdf_path} ({size_mb:.1f} MB)')
else:
    print('\nERROR: PDF not generated! Check exports/manuscript.log')
