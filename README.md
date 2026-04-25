# nabla-kaitai

『ナブラ解体新書』の執筆リポジトリ。

原稿の正本は Markdown math 形式の `.md` とし、全11章を日本語版・英訳版・note.com変換版・PDF/ゲラへ展開する。

## Directory Layout

| Path | Role |
| --- | --- |
| `manuscript/ja/` | 日本語原稿の正本。章ごとに Markdown math 形式の `.md` を置く。 |
| `manuscript/en/` | 英訳版原稿。日本語版と同じ章番号で管理する。 |
| `exports/pdf/` | 全章を結合してPDF化した成果物を置く。 |
| `exports/note/` | note.com投稿用に変換したMarkdownを置く。 |
| `galleys/` | 校正用ゲラ、入稿確認用PDF、外部確認版を置く。 |
| `references/pdfs/` | 論文・書籍PDFのローカル置き場。PDF本体は原則Git管理外。 |
| `references/ocr-md/` | 必要に応じてPDFからOCRしたMarkdownを置く。 |
| `tools/` | 結合、PDF化、note変換、OCR補助などのスクリプトを置く。 |
| `docs/` | プロジェクト運用、構成、執筆ルールを置く。 |

## Chapter Policy

- 全体は11章構成とする。
- 各章の原稿は `.md` とし、数式は Markdown math / LaTeX math を使う。
- 日本語版と英訳版は章番号を揃える。
- PDF、note.com形式、ゲラは派生成果物として扱い、原稿正本とは分離する。

## Reference Policy

- `references/pdfs/` はPDF原本の置き場。
- `references/ocr-md/` はOCR済みMarkdownの置き場。
- PDF本体は大容量かつライセンス制約がありうるため、デフォルトでは `.gitignore` で除外する。
- 引用・参照メモやOCR Markdownは、必要に応じてGit管理する。
