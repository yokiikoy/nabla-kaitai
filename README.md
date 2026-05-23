# ナブラ解体新書

『ナブラ解体新書 —— 行列表示の微分形式によるベクトル解析の抜け道 ——』の執筆リポジトリ。

3次元ユークリッド空間におけるベクトル解析を、微分形式の行列表示（横ベクトル＝一次形式）と有限小片・有限セルによる発見的導入で再構成する教科書。全12章構成。

## 構成

```
manuscript/
  ja/          日本語原稿（全12章 + 前付け・付録・参考文献・おわりに）
  en/          英訳版原稿（全12章 + 前付け・付録・参考文献・おわりに）
  README.md
  ch0*_note.md 章別注釈メモ
exports/
  manuscript.pdf           生成済みPDF
  manuscript_combined.md   結合済みMarkdown（参照用）
  README.md
tools/
  build_pdf.py     PDF生成スクリプト（Python 3 + XeLaTeX + Pandoc）
  build_html.py    GitHub Pages用HTML生成スクリプト（KaTeX）
  README.md
docs/             GitHub Pages公開用HTML
README.md
```

## 章構成

| 章 | 内容 |
|---|---|
| 前付け | 著者ノート、はじめに（$dx$とは何か／ナブラとは何か）、前提知識・ロードマップ、ポータルサイト |
| 第1章 | $dx$ とは何か —— ベクトルを食べる測定器、あるいは横ベクトル |
| 第2章 | 面積とは何か —— 平行多面体に潜む、符号のルール |
| 第3章 | 積分するとは何か —— 有限のマスを数え、最後に極限を取る |
| 第4章 | 変数変換とは何か —— 引き戻し $\Phi^*$：測定器のつじつま合わせ |
| 第5章 | 微分するとは何か —— 外微分 $d$：局所のズレとStokesの橋 |
| 第6章 | 計量 $g$ とホッジ・スター $\ast$ —— 内積の召喚と次数の反転 |
| 第7章 | ベクトル解析 —— ナブラの登場 |
| 第8章 | 二つの言語 —— 測定器の微分と、場の微分 |
| 第9章 | 実戦 —— 辞書を作り、難問を解く |
| 第10章 | マクスウェル方程式 —— 美しさのその先へ |
| 第11章 | 曲がった空間へ —— 本書の先にあるもの |
| 第12章 | 真のナブラ —— クリフォード・パウリ・ディラック・ハミルトン |
| 付録 | 本書で語らなかったもの |
| 参考文献 | と著者からのコメント |
| おわりに | 『ナブラ解体新書』はいかにして生まれたか |

## ビルド方法

### PDF
```bash
python3 tools/build_pdf.py
```
生成物：`exports/manuscript.pdf`

要環境：Python 3, XeLaTeX, Pandoc, IPAexフォント

### GitHub Pages HTML
```bash
python3 tools/build_html.py              # Japanese → docs/
python3 tools/build_html.py --lang en    # English → docs/en/
# or both:
python3 tools/build_release.py --html-only
```
生成物：`docs/*.html`（日本語）、`docs/en/*.html`（英語）

要環境：Python 3（KaTeXはCDN経由）

### Release build (v1.0.1+)
```bash
python3 tools/build_release.py
```
生成物：`exports/manuscript.pdf`、`exports/manuscript-en.pdf`、`docs/`、`docs/en/`、`manuscript.pdf`

## ライセンス

CC BY-NC 4.0（著作者：yokiikoy）