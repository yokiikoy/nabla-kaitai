# nabla-kaitai（ナブラ解体新書シリーズ）

執筆リポジトリ。ABF（`/home/yokii/dev/knowledge/work/abf`）は**ツール**として別管理し、原稿の**正**は本リポで育てる。

## レイアウト（目安）

| パス | 用途 |
|------|------|
| `docs/abf-context/` | ABF 参照用メモ（章立て・問題背景・用語）。Markdown |
| `reference/ocr/` | 種本の OCR チャンク（`.md`）。必要に応じて `.gitignore` |
| `volumes/` など | 原稿本体（プロジェクトの慣習に合わせて後から追加） |

## ABF から参照させるには

`abf/abf.config.json` の `draft.referenceGlobs` に例:

```json
"referenceGlobs": [
  "../nabla-kaitai/docs/abf-context/**/*.md",
  "../nabla-kaitai/reference/ocr/**/*.md"
]
```

## DevOrchestrator

プロジェクトキー: **`nabla-kaitai`**、チケット接頭辞: **`NKAI`**（`docs/tickets/` を置く場合）。
