"""Build locale configuration for Japanese and English editions."""

RELEASE_VERSION = 'v1.0.1'

LOCALES = {
    'ja': {
        'base_dir': 'manuscript/ja',
        'docs_dir': 'docs',
        'pdf_stem': 'manuscript',
        'combined_md': 'exports/manuscript_combined.md',
        'html_lang': 'ja',
        'site_title': 'ナブラ解体新書',
        'toc_label': '目次',
        'toc_page_title': '目次',
        'toc_intro': '各見出しはリンクになっており、クリックすると該当章の該当位置にジャンプします。',
        'book_link_text': 'ナブラ解体新書',
        'author_line': '著者：yokiikoy',
        'part_labels': {
            'I': ('ch01.html', 'ch05.html', '第I部：$\\mathbb{R}^3$ 上の微分形式（第1章〜第5章）'),
            'II': ('ch06.html', 'ch09.html', '第II部：ベクトル解析（第6章〜第9章）'),
            'III': ('ch10.html', 'ch12.html', '第III部：発展と統合（第10章〜第12章）'),
        },
        'title_page': {
            'main_title': r'{\fontsize{34}{42}\selectfont\bfseries ナブラ解体新書\par}',
            'subtitle': (
                r'{\Large 行列表示の微分形式による\par}'
                r'{\Large ベクトル解析の抜け道\par}'
            ),
            'version_note': (
                r'\textbf{v1.0.1} & 英語版初公開（ch00--ch12 + 後付け）・軽微な修正\\ \hline' '\n'
                r'\textbf{v1.0.0} & 全12章の内容確定・相互参照の整合性完了・手計算による検算完了\\ \hline' '\n'
            ),
            'policy_tail': (
                r'\textbf{v2.0.0} & 図表の作成と配置完了・組版完了・印刷用データの出力\\ \hline' '\n'
                r'v0.x.0         & 章の追加・章構成の変更・大幅な書き直し\\ \hline' '\n'
                r'v0.0.x         & 注釈の追加・誤字修正・軽微な推敲\\ \hline' '\n'
            ),
            'history_heading': r'\multicolumn{1}{|c|}{\textbf{直近の改定履歴}}\\ \hline',
            'author_suffix': r' --- 著者：',
        },
    },
    'en': {
        'base_dir': 'manuscript/en',
        'docs_dir': 'docs/en',
        'pdf_stem': 'manuscript-en',
        'combined_md': 'exports/manuscript-en_combined.md',
        'html_lang': 'en',
        'site_title': 'Unmasking Div, Grad, and Curl',
        'toc_label': 'Contents',
        'toc_page_title': 'Contents',
        'toc_intro': 'Each heading is a link to the corresponding section in its chapter.',
        'book_link_text': 'Unmasking Div, Grad, and Curl',
        'author_line': 'Author: yokiikoy',
        'part_labels': {
            'I': ('ch01.html', 'ch05.html', 'Part I: Differential Forms on $\\mathbb{R}^3$ (Chapters 1–5)'),
            'II': ('ch06.html', 'ch09.html', 'Part II: Vector Analysis (Chapters 6–9)'),
            'III': ('ch10.html', 'ch12.html', 'Part III: Extensions and Unification (Chapters 10–12)'),
        },
        'title_page': {
            'main_title': r'{\fontsize{30}{38}\selectfont\bfseries Unmasking Div, Grad, and Curl\par}',
            'subtitle': (
                r'{\Large A Shortcut to Vector Analysis\par}'
                r'{\Large through Matrix-Represented Differential Forms\par}'
            ),
            'version_note': (
                r'\textbf{v1.0.1} & First English release (ch00--ch12 + back matter)\\ \hline' '\n'
                r'\textbf{v1.0.0} & Japanese edition: content freeze and cross-reference consistency\\ \hline' '\n'
            ),
            'policy_tail': (
                r'\textbf{v2.0.0} & Figures/layout complete; print-ready output\\ \hline' '\n'
                r'v0.x.0         & New chapters or major restructuring\\ \hline' '\n'
                r'v0.0.x         & Notes, typos, light polish\\ \hline' '\n'
            ),
            'history_heading': r'\multicolumn{1}{|c|}{\textbf{Recent revision history}}\\ \hline',
            'author_suffix': r' --- Author: ',
        },
    },
}


def get_locale(name: str) -> dict:
    if name not in LOCALES:
        raise ValueError(f"Unknown locale: {name}. Choose from {', '.join(LOCALES)}")
    return LOCALES[name]
