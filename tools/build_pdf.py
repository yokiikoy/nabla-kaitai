#!/usr/bin/env python3
"""
Generate PDF from manuscript using Pandoc → XeLaTeX.
Profile-driven build system separating content scope and toc scope.
"""
import subprocess
import os
import re
import sys
import argparse
from pathlib import Path
from datetime import datetime

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

# Add tools directory to path so we can import core
sys.path.append(str(Path(__file__).parent))
from core.profile import get_profile
from core.manuscript import ManuscriptModel

def strip_yaml(content):
    if content.startswith('---'):
        end = content.find('---', 3)
        if end > 0:
            return content[end+3:].lstrip()
    return content

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="full", choices=["full", "preview"])
    args = parser.parse_args()

    profile = get_profile(args.profile)
    model = ManuscriptModel(profile)

    # Git metadata for title page
    build_datetime = datetime.now().strftime('%Y-%m-%d %H:%M JST')
    author_name = 'yokiikoy'
    git_log = git_text(['log', '-3', '--format=%h (%ad)  %s', '--date=short'], '未取得')
    log_lines = [l.strip() for l in git_log.split('\n') if l.strip()]
    while len(log_lines) < 3:
        log_lines.append('')

    os.makedirs('exports', exist_ok=True)
    os.makedirs('preview', exist_ok=True)

    # 1. Build Markdown for Pandoc
    # We only pass content_chapters to Pandoc. The TOC stubs will be added in LaTeX.
    content_chapters = model.get_content_chapters()
    combined = []
    
    for ch in content_chapters:
        raw_text = "\n".join(ch.content_lines)
        if ch.is_front_matter:
            raw_text = strip_yaml(raw_text)
        
        # Ensure chapter title is present for main matter
        if not ch.is_front_matter and ch.id.isdigit() and not raw_text.lstrip().startswith('# '):
            raw_text = f"# {ch.title}\n\n" + raw_text
             
        combined.append(raw_text)

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

    def ensure_blank_lines_before_structures(text):
        lines = text.split('\n')
        result = []
        list_markers = ('* ', '- ', '+ ')
        for i, line in enumerate(lines):
            stripped = line.lstrip()
            prev = lines[i - 1] if i > 0 else ''
            prev_stripped = prev.lstrip()

            if (stripped.startswith(list_markers)
                    and prev_stripped != ''
                    and not prev_stripped.startswith('```')
                    and not prev_stripped.endswith('>')):
                result.append('')

            if (line.startswith('> ') and line[2:].startswith(list_markers)
                    and prev.startswith('>')
                    and prev.strip() != '>'):
                result.append('>')

            if stripped.startswith(('# ', '## ', '### ')) and prev_stripped != '':
                result.append('')

            result.append(line)
        return '\n'.join(result)

    md_text = ensure_blank_lines_before_structures(md_text)

    tmp_md = 'exports/tmp_for_pandoc.md'
    with open(tmp_md, 'w') as f:
        f.write(md_text)

    print('Converting Markdown to LaTeX via Pandoc...')
    try:
        r = subprocess.run([
            'pandoc',
            tmp_md,
            '-f', 'markdown+tex_math_dollars+raw_tex+multiline_tables',
            '-t', 'latex',
            '--top-level-division=chapter',
            '-o', 'exports/body.tex'
        ], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Pandoc failed: {e.stderr}")
        sys.exit(1)

    with open('exports/body.tex', 'r') as f:
        latex_body = f.read()

    # --- Post-process LaTeX ---
    def process_footnotes(text):
        matches = re.finditer(r'\[\^([^\]]+)\]', text)
        for m in reversed(list(matches)):
            fn_id = m.group(1)
            fn_block_start = text.find(f'\\hypertarget{{{fn_id}}}{{%')
            if fn_block_start == -1:
                fn_block_start = text.find(f'\\hypertarget{{{fn_id}}}')
            
            if fn_block_start > -1:
                end_marker = '\n\n'
                fn_block_end = text.find(end_marker, fn_block_start)
                if fn_block_end == -1:
                    fn_block_end = len(text)
                
                fn_content = text[fn_block_start:fn_block_end]
                fn_content = re.sub(r'\\hypertarget{[^}]+}{%?\s*', '', fn_content)
                fn_content = re.sub(r'\\label{[^}]+}\\}?\s*', '', fn_content)
                fn_content = fn_content.strip()
                
                if fn_content.startswith('}'):
                    fn_content = fn_content[1:].strip()
                
                replacement = f'\\footnote{{{fn_content}}}'
                text = text[:m.start()] + replacement + text[m.end():]
                text = text[:fn_block_start] + text[fn_block_end:]
        return text

    latex_body = process_footnotes(latex_body)

    def soften_horizontal_rules(text):
        return text.replace(
            r'\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}',
            r'\par\vspace{0.35em}\par'
        )

    latex_body = soften_horizontal_rules(latex_body)

    def add_matter_divisions(text):
        """Insert frontmatter, mainmatter, backmatter before appropriate chapters."""
        chapter_positions = [m.start() for m in re.finditer(r'\\chapter\{', text)]
        if not chapter_positions:
            return text
        
        fm_count = len(model.front_matter)
        bm_count = sum(1 for ch in content_chapters if ch.id in ('afterword', 'references', 'appendix'))
        main_start = fm_count
        back_start = len(chapter_positions) - bm_count
        
        insertions = [(chapter_positions[0], '\n\\frontmatter\n')]
        if main_start < len(chapter_positions):
            insertions.append((chapter_positions[main_start], '\n\\mainmatter\n'))
        if 0 < back_start < len(chapter_positions) and back_start != main_start:
            insertions.append((chapter_positions[back_start], '\n\\backmatter\n'))
        
        for pos, cmd in reversed(insertions):
            text = text[:pos] + cmd + text[pos:]
        return text
    
    latex_body = add_matter_divisions(latex_body)

    def hide_appendix_from_toc(text):
        for cmd in ('subsection', 'subsubsection', 'paragraph'):
            for letter in 'ABCDE':
                text = re.sub(rf'\\{cmd}\{{({letter}\.)', rf'\\{cmd}*{{\1', text)
                text = re.sub(rf'\\{cmd}\{{(\\\\texorpdfstring\{{{letter}\.)', rf'\\{cmd}*{{\1', text)
        return text

    latex_body = hide_appendix_from_toc(latex_body)

    def fix_dashes(text):
        em = '\u2014'
        en = '\u2013'
        text = text.replace('------', em + em)
        text = text.replace('---', em)
        text = text.replace('--', en)
        return text

    latex_body = fix_dashes(latex_body)

    # --- Preamble ---
    preamble = (
        r'\documentclass[a4paper,12pt,openany]{book}' '\n'
        r'\usepackage{amsmath,amssymb,bm}' '\n'
        r'\usepackage{esint,cancel}' '\n'
        r'\usepackage[no-math]{fontspec}' '\n'
        r'\setmainfont{IPAexMincho}[AutoFakeBold=1.5, Ligatures=TeX]' '\n'
        r'\setsansfont{IPAexGothic}[Ligatures=TeX]' '\n'
        r'\setmonofont{IPAexGothic}[Ligatures=TeX]' '\n'
        r'\newfontface\strongface{IPAexGothic}[AutoFakeBold=4.0]' '\n'
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
        r'\mdfdefinestyle{annotation}{' '\n'
        r'    linecolor=gray!40,' '\n'
        r'    backgroundcolor=gray!5,' '\n'
        r'    linewidth=1pt,' '\n'
        r'    topline=false,' '\n'
        r'    rightline=false,' '\n'
        r'    bottomline=false,' '\n'
        r'    leftmargin=10pt,' '\n'
        r'    innerleftmargin=10pt,' '\n'
        r'    innerrightmargin=10pt,' '\n'
        r'    innertopmargin=5pt,' '\n'
        r'    innerbottommargin=5pt' '\n'
        r'}' '\n'
        r'\BeforeBeginEnvironment{quote}{\begin{mdframed}[style=annotation]}' '\n'
        r'\AfterEndEnvironment{quote}{\end{mdframed}}' '\n'
        r'\makeatletter' '\n'
        r'\def\maxwidth{\ifdim\Gin@nat@width>\linewidth\linewidth\else\Gin@nat@width\fi}' '\n'
        r'\def\maxheight{\ifdim\Gin@nat@height>\textheight\textheight\else\Gin@nat@height\fi}' '\n'
        r'\makeatother' '\n'
        r'\setkeys{Gin}{width=\maxwidth,height=\maxheight,keepaspectratio}' '\n'
        r'\providecommand{\tightlist}{%' '\n'
        r'  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}' '\n'
        '% Tolerate slight overfull boxes in math-heavy text\n'
        r'\setlength{\emergencystretch}{2em}' '\n'
        r'\tolerance=2000' '\n'
        r'\hbadness=5000' '\n'
        r'\begin{document}' '\n'
    )

    title_page = (
        r'\begin{titlepage}' '\n'
        r'\newgeometry{top=35mm,bottom=30mm,left=40mm,right=40mm}' '\n'
        r'\pagestyle{empty}' '\n'
        r'\centering' '\n'
        r'\vspace*{25mm}' '\n'
        r'{\includegraphics[width=4cm]{exports/icons/nabla_icon_inflate_65.png}\par}' '\n'
        r'\vspace{10mm}' '\n'
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
        r'\multicolumn{1}{|c|}{\textbf{直近の改定履歴}}\\ \hline' '\n'
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
    
    # PDF TOC Scope: Inject virtual TOC entries for chapters that are in toc_scope but not in content_scope
    # This allows the PDF to display the full TOC even in preview mode.
    toc_stubs = []
    if profile.is_preview:
        # Full build page numbers for chapters 2-12
        FULL_PAGE_NUMBERS = {
            '02': 24, '03': 45, '04': 59, '05': 72, '06': 92,
            '07': 112, '08': 122, '09': 132, '10': 140, '11': 152, '12': 162,
        }
        
        toc_stubs.append(r'\chapter*{完結版の収録予定について}')
        toc_stubs.append(r'\addcontentsline{toc}{chapter}{完結版の収録予定について}')
        toc_stubs.append(r'以下の章および節は、先行公開版（本PDF）には本文が含まれていません。')
        toc_stubs.append(r'')
        toc_stubs.append(r'本書の全12章分の草稿はすでに書き上がっていますが、現在は誤字脱字、全体の整合性、数学的厳密性と教育的な断言のバランスを調整している最中です。GitHub リポジトリや作業中ブランチを探すと、第2章以降の草稿が見えてしまう可能性があります。ただし、それらは正式な公開版ではありません。')
        toc_stubs.append(r'')
        toc_stubs.append(r'どうしても続きを読む場合は、こっそり作業場を覗き見たものとして扱い、現時点では批評・レビュー・拡散の対象にしないでください。正式な完結版は、ポータルサイトで案内します。')
        toc_stubs.append(r'\vspace{2em}')
        toc_stubs.append(r'{\small ページ番号は完全版のものです。この先行公開版では対応する本文はありません。}')
        toc_stubs.append(r'\vspace{1em}')

        # Custom mini-TOC with full build page numbers
        for ch in model.chapters:
            if not ch.is_included_in_content:
                page_num = FULL_PAGE_NUMBERS.get(ch.id, '??')
                # Escape LaTeX special chars in title (but preserve $ math)
                safe_title = ch.title.replace('_', r'\_').replace('&', r'\&').replace('#', r'\#')
                toc_stubs.append(r'\noindent\textbf{' + safe_title + r'}\dotfill ' + str(page_num) + r'\par')
                for item in ch.toc_items:
                    indent = r'\hspace{1em}' if item.level == 2 else r'\hspace{2em}'
                    safe_item = item.title.replace('_', r'\_').replace('&', r'\&').replace('#', r'\#')
                    if item.level == 2:
                        toc_stubs.append(r'\noindent' + indent + safe_item + r'\dotfill ' + str(page_num) + r'\par')
                    else:
                        toc_stubs.append(r'\noindent' + indent + r'{\footnotesize ' + safe_item + r'}\dotfill ' + str(page_num) + r'\par')
        
        toc_stubs.append(r'\newpage')

    latex_stubs = "\n".join(toc_stubs) if profile.is_preview else ""

    # Insert stubs before back matter (afterword), not at the very end
    if profile.is_preview and latex_stubs:
        back_matter_pattern = re.compile(r'(\\chapter\*?\{おわりに|\\chapter\*?\{\\texorpdfstring\{おわりに)')
        bm_match = back_matter_pattern.search(latex_body)
        if bm_match:
            latex_body = latex_body[:bm_match.start()] + latex_stubs + "\n" + latex_body[bm_match.start():]

    latex_doc = preamble + title_page + latex_body + '\n' + r'\end{document}' + '\n'

    tex_filename = 'manuscript-preview.tex' if profile.is_preview else 'manuscript.tex'
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
    
    with open(f'exports/{tex_filename}', 'w') as f:
        f.writelines(new_lines)

    # Compile with xelatex
    pdf_path = 'preview/manuscript-preview.pdf' if profile.is_preview else 'exports/manuscript.pdf'
    
    # Remove old PDF to avoid false success on xelatex failure
    if os.path.exists(pdf_path):
        os.remove(pdf_path)
    
    print('\nCompiling with XeLaTeX...')
    for run in [1, 2]:
        print(f'  Run {run}...')
        r = subprocess.run(
            ['xelatex', '-interaction=nonstopmode',
             f'-output-directory={"preview" if profile.is_preview else "exports"}', f'exports/{tex_filename}'],
            capture_output=True, text=True, timeout=300
        )
    
    if os.path.exists(pdf_path):
        size_mb = os.path.getsize(pdf_path) / (1024*1024)
        print(f'\nPDF generated: {pdf_path} ({size_mb:.1f} MB)')
        if r.returncode != 0:
            print('(XeLaTeX reported errors but PDF was produced - check log for details)')
    else:
        print(f'\nERROR: PDF not generated!')
        print(r.stdout[-3000:])
        print(r.stderr[-3000:])
        sys.exit(1)

if __name__ == '__main__':
    main()
