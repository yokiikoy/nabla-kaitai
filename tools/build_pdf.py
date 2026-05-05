#!/usr/bin/env python3
"""Generate PDF from manuscript using Pandoc → XeLaTeX."""
import subprocess, os, re, glob, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--profile", default="full", choices=["full", "preview"])
args = parser.parse_args()
is_preview = args.profile == "preview"

from datetime import datetime

# Build combined markdown
files = []
# Front matter
front_matter = glob.glob('manuscript/ja/ch00/*.md')
front_matter.sort()
files.extend(front_matter)
front_matter_count = len(front_matter)

max_chapter = 1 if is_preview else 12
for i in range(1, max_chapter + 1):
    f = f'manuscript/ja/ch{i:02d}/ch{i:02d}.md'
    if os.path.exists(f):
        files.append(f)
back_matter_count = 0
for suffix in ['afterword', 'references', 'appendix']:
    f = f'manuscript/ja/{suffix}.md'
    if os.path.exists(f):
        files.append(f)
        back_matter_count += 1


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

# Clean version for HTML and combined preview
clean_md_text = '\n\n'.join(combined)
combined_md_filename = 'manuscript_preview_combined.md' if is_preview else 'manuscript_combined.md'
with open(f'exports/{combined_md_filename}', 'w') as f:
    f.write(clean_md_text)

print(f'Combined {len(files)} chapters → exports/{combined_md_filename}')

# Version with page breaks for PDF
md_text = '\n\n\\newpage\n\n'.join(combined)

# --- Process marker tags for PDF ONLY ---
md_text = md_text.replace('<!-- pagebreak -->', '\\clearpage')
md_text = re.sub(
    r'<!-- scalebox -->\s*\n\$\$(.*?)\$\$\s*\n\s*<!-- endscalebox -->',
    r'\\begin{center}\\scalebox{1.8}{$\\displaystyle \1$}\\end{center}',
    md_text,
    flags=re.DOTALL
)

# Convert HTML <strong> tags to Pandoc-native **bold** syntax for LaTeX
md_text = re.sub(r'<strong>\s*(.*?)\s*</strong>', r'**\1**', md_text, flags=re.DOTALL)

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
        """Keep HTML-style front/back matter from incrementing chapter numbers."""
        result = []
        cursor = 0
        chapter_index = 0
        unnumbered = set(range(front_matter_count))
        unnumbered.update(range(len(files) - back_matter_count, len(files)))
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
        r'\fancyfoot[L]{%' '\n'
        r'  \tiny' '\n'
        r'  \parbox{\textwidth}{%' '\n'
        r'    \raggedright' '\n'
        r'    \textcopyright\ yokiikoy (CC BY-NC 4.0). 本書の最新版・PDF・改訂履歴・関連情報・本書以外のコンテンツはポータルサイト \href{https://covectorspace.xyz/jp/}{Project Co-Vector Space} をご確認ください。\\[2pt]' '\n'
        r'    \centering\thepage' '\n'
        r'  }%' '\n'
        r'}' '\n'
        r'\fancyfoot[C]{}' '\n'
        r'\fancypagestyle{plain}{\fancyhf{}\fancyfoot[L]{%' '\n'
        r'  \tiny' '\n'
        r'  \parbox{\textwidth}{%' '\n'
        r'    \raggedright' '\n'
        r'    \textcopyright\ yokiikoy (CC BY-NC 4.0). 本書の最新版・PDF・改訂履歴・関連情報・本書以外のコンテンツはポータルサイト \href{https://covectorspace.xyz/jp/}{Project Co-Vector Space} をご確認ください。\\[2pt]' '\n'
        r'    \centering\thepage' '\n'
        r'  }%' '\n'
        r'}\renewcommand{\headrulewidth}{0pt}}' '\n'
        r'\renewcommand{\headrulewidth}{0pt}' '\n'
        r'\usepackage{hyperref}' '\n'
        r'\usepackage{bookmark}' '\n'
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
        r'% IPAexMincho has no real Bold face; \bfseries in headings falls back to'
        '\n'
        r'% incorrect glyphs.  Redirect \bfseries to \strongface in text mode while'
        '\n'
        r'% keeping the original behaviour for math (so \boldmatter etc. still work).'
        '\n'
        r'\makeatletter' '\n'
        r'\let\oldbfseries\bfseries' '\n'
        r'\DeclareRobustCommand{\bfseries}{\ifmmode\oldbfseries\else\strongface\fi}' '\n'
        r'\makeatother' '\n'
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
        + (r'\vspace{6mm}{\Large (先行公開版)\par}' '\n' if is_preview else '') +
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

    if is_preview:
        detailed_latex_toc = r'''
\chapter*{完全版の目次（予告）}
\addcontentsline{toc}{chapter}{完全版の目次（予告）}
\begin{flushleft}
{\small ※ 先行公開版では第1章のみ公開しています。第2章以降は完結版にて収録予定です。}
\end{flushleft}
\vspace{1em}

\newcommand{\plannedchapter}[2]{{\bfseries #1 #2}\dotfill ??\par}
\newcommand{\plannedsection}[1]{\hspace{1em}#1\dotfill ??\par}
\newcommand{\plannedsubsection}[1]{\hspace{2em}{\footnotesize #1}\dotfill ??\par}

\plannedchapter{第2章}{面積とは何か —— 平行多面体に潜む、符号のルール}
\plannedsubsection{§2.0 測定器と面積・体積、そして長さ}
\plannedsubsection{§2.1 小学校の面積の限界}
\plannedsubsection{§2.2 面積測定器が満たすべき「3つのルール」}
\plannedsubsection{§2.3 面積測定器の正体は「反対称行列」である}
\plannedsubsection{§2.4 面積測定器の内部構造}
\plannedsubsection{§2.5 体積測定器と行列式}
\plannedsubsection{§2.6 本章のまとめと第3章への展望}
\plannedsection{第2章 付録A：体積測定器のテンソル積表現 — 全成分の計算}

\plannedchapter{第3章}{積分するとは何か —— 有限のマスを数え、最後に極限を取る}
\plannedsubsection{§3.0 曲がったものを測る——小学校以来の借りを返す}
\plannedsubsection{§3.1 体積——3次元、係数1}
\plannedsubsection{§3.2 表面積——2次元、係数1}
\plannedsubsection{§3.3 曲線——1次元、係数1（限界があらわになる）}
\plannedsubsection{§3.4 係数をつける——密度と幾何の積}
\plannedsubsection{§3.5 本章のまとめと次章への展望}

\plannedchapter{第4章}{変数変換とは何か —— 引き戻し $\Phi^*$：測定器のつじつま合わせ}
\plannedsubsection{§4.0 物理は曲がる、計算は四角}
\plannedsubsection{§4.1 1-form の引き戻し——仕事と運動エネルギー定理}
\plannedsubsection{§4.2 2-form の引き戻し——角運動量保存と面積速度}
\plannedsubsection{§4.3 3-form の引き戻し——質量保存と体積分}
\plannedsubsection{§4.4 引き戻しの性質 —— ここまでに確立したこと}
\plannedsubsection{§4.5 本章のまとめと第5章（外微分）への展望}

\plannedchapter{第5章}{微分するとは何か —— 外微分 $d$：局所のズレとStokesの橋}
\plannedsubsection{§5.0 第II部の扉——観測は積分、法則は微分}
\plannedsubsection{§5.1 $df$ 再訪——微分と積分は逆演算か}
\plannedsubsection{§5.2 閉ループで姿を現す「ズレ」}
\plannedsubsection{§5.3 微小ループの解体——ズレは面積に比例する}
\plannedsubsection{§5.4 $d$ の誕生——面積あたりのズレを測る新しい測定器}
\plannedsubsection{§5.5 一般の $1$-form の外微分——3次元への拡張}
\plannedsubsection{§5.6 集積すれば境界だけが残る——ストークスの定理}
\plannedsubsection{§5.7 同じことをもう一段——$2$-form の外微分と発散}
\plannedsubsection{§5.8 $d^2 = 0$——二度測れば必ずゼロ}
\plannedsubsection{§5.9 外微分の統合——一つの式、一つのルール}
\plannedsubsection{§5.10 積分から微分方程式へ——物理法則の局所化}
\plannedsubsection{§5.11 第II部への展望——ホッジ・スターへの伏線}
\plannedsection{付録C：外微分の行列表示}
\plannedsubsection{C.1 $0$-form：$df$ の $1 \times 3$ 行ベクトル}
\plannedsubsection{C.2 $1$-form：係数のヤコビ行列 $\mathbf{J}$}
\plannedsubsection{C.3 $d\omega = \mathbf{J}^T - \mathbf{J}$}
\plannedsubsection{C.4 $2$-form：$d\eta$ とヤコビ行列のトレース}
\plannedsubsection{C.5 $d^2 f = 0$ とヘッセ行列}

\plannedchapter{第6章}{計量 $g$ とホッジ・スター $\ast$ — 内積の召喚と次数の反転}
\plannedsubsection{§6.0 言い訳の終焉——内積を解放する}
\plannedsubsection{§6.1 パラメータ空間の内積——計量 $g$ の正体}
\plannedsubsection{§6.2 $g$ による縦ベクトルと横ベクトルの変換}
\plannedsubsection{§6.3 ホッジ・スター $\ast$ ——二つの方法を繫ぐ対応}
\plannedsubsection{§6.4 対応の実例——微分形式とベクトル解析}
\plannedsubsection{§6.5 ナブラの三兄弟を解体する}
\plannedsubsection{§6.6 第II部の結び —— 第III部へ}
\plannedsection{付録D：フロベニウス積とホッジ・スターの完全な行列表現}
\plannedsubsection{D.1 行列の内積——フロベニウス積}
\plannedsubsection{D.2 $\ast_{1\to2}$ ——行列の縦ベクトル}
\plannedsubsection{D.3 $\ast_{2\to1}$ ——フロベニウス積による係数抽出}
\plannedsubsection{D.4 転置関係}
\plannedsubsection{D.5 $E_k \cdot M$ の成分}
\plannedsubsection{D.6 $\ast$ の二回作用}

\plannedchapter{第7章}{ベクトル解析 —— ナブラの登場}
\plannedsubsection{§7.0 ナブラの登場}
\plannedsubsection{§7.1 ドット積とクロス積}
\plannedsubsection{§7.2 $\nabla$ と勾配}
\plannedsubsection{§7.3 発散}
\plannedsubsection{§7.4 回転}
\plannedsubsection{§7.5 ラプラシアン}
\plannedsubsection{§7.6 恒等式}
\plannedsubsection{§7.7 ナブラの公式集}
\plannedsubsection{§7.8 積分定理——ストークス・ガウス・グリーン}
\plannedsubsection{§7.9 第III部へ —— 矢印を見るな、測定器を見ろ}

\plannedchapter{第8章}{二つの言語 —— 測定器の微分と、場の微分}
\plannedsubsection{§8.0 本書のハイライト}
\plannedsubsection{§8.1 二つの微分、二つの世界}
\plannedsubsection{§8.2 翻訳辞書の完成}
\plannedsubsection{§8.3 ストークスの定理を翻訳する}
\plannedsubsection{§8.4 ガウスの定理を翻訳する}
\plannedsubsection{§8.5 二つの方法論——場はそのままか、測定器はそのままか}
\plannedsubsection{§8.6 曲線座標と二つの方法}

\plannedchapter{第9章}{実戦 —— 辞書を作り、難問を解く}
\plannedsubsection{§9.0 本書の中心的な道具は揃った}
\plannedsubsection{§9.1 辞書をその場で作る——機械的手順}
\plannedsubsection{§9.2 円柱座標 $(r,\theta,z)$}
\plannedsubsection{§9.3 球座標 $(\rho,\theta,\phi)$}
\plannedsubsection{§9.4 微積分の難問——球座標でのベクトルラプラシアン}
\plannedsubsection{§9.5 電磁気学の難問——点電荷の電場と発散}
\plannedsubsection{§9.6 辞書は終わり、旅は続く}

\plannedchapter{第10章}{マクスウェル方程式 —— 美しさのその先へ}
\plannedsubsection{§10.0 お約束}
\plannedsubsection{§10.1 マクスウェル方程式——2本で書く}
\plannedsubsection{§10.2 電磁場 $F$ と符号規約の固定}
\plannedsubsection{§10.3 ミンコフスキー計量——$\mathbb{R}^3$ から4次元へ}
\plannedsubsection{§10.4 $dF=0$ を全部書き下す}
\plannedsubsection{§10.5 $\ast F$ と残りの2本}
\plannedsubsection{§10.6 ポテンシャル構成——$F=-d\mathcal{A}$ から始める}
\plannedsection{付録E：$dF$ と $d(\ast F)$ のスライス行列表示 —— $4\times4\times4$ 配列で見るマクスウェル方程式}
\plannedsubsection{E.1 基底 $3$-form とそのスライス行列 —— 全16枚}
\plannedsubsection{E.2 $dF$ をスライス行列で書く}
\plannedsubsection{E.3 フロベニウス積で係数を抜き出す}
\plannedsubsection{E.4 $dF=0$ をスライスで読む}
\plannedsubsection{E.5 $d(\ast F) = \mu_0(\ast\mathcal{J})$ のスライス表示}

\plannedchapter{第11章}{曲がった空間へ —— 本書の先にあるもの}
\plannedsubsection{§11.0 この章の立ち位置 —— さらに先を見たい読者のための道標}
\plannedsubsection{§11.1 多様体 —— $\mathbf{g}(x)$ から始める}
\plannedsubsection{§11.2 リーマン幾何学 —— テンソル解析のスタイル}
\plannedsubsection{§11.3 その先へ}

\plannedchapter{第12章}{真のナブラ —— クリフォード・パウリ・ディラック・ハミルトン}
\plannedsubsection{§12.0 2本を1本に}
\plannedsubsection{§12.1 虚数で一本に —— マクスウェル方程式の統合}
\plannedsubsection{§12.2 パウリ行列 —— 異なる次数を足す魔法}
\plannedsubsection{§12.3 ディラック演算子と「真のナブラ」}
\plannedsubsection{§12.4 演算子$\nabla$}

\newpage
'''
        latex_body += detailed_latex_toc

    latex_doc = preamble + latex_body + '\n' + r'\end{document}' + '\n'

    tex_filename = 'manuscript-preview.tex' if is_preview else 'manuscript.tex'
    with open(f'exports/{tex_filename}', 'w') as f:
        f.write(latex_doc)
    print(f'LaTeX source → exports/{tex_filename}')

    # Post-process: hide appendix subsections from TOC
    with open(f'exports/{tex_filename}', 'r') as f:
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
    tex_filename = 'manuscript-preview.tex' if is_preview else 'manuscript.tex'
    with open(f'exports/{tex_filename}', 'w') as f:
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
         f'-output-directory={"preview" if is_preview else "exports"}', f'exports/{tex_filename}'],
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
pdf_path = 'preview/manuscript-preview.pdf' if is_preview else 'exports/manuscript.pdf'
if os.path.exists(pdf_path):
    import os as _os
    size_mb = _os.path.getsize(pdf_path) / (1024*1024)
    print(f'\nPDF generated: {pdf_path} ({size_mb:.1f} MB)')
else:
    print('\nERROR: PDF not generated! Check exports/manuscript.log')
