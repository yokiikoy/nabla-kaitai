# nabla-kaitai（ナブラ解体新書シリーズ）

執筆リポジトリ。ABF（`/home/yokii/dev/knowledge/work/abf`）は**ツール**として別管理し、原稿の**正**は本リポで育てる。

## レイアウト（目安）

| パス | 用途 |
|------|------|
| `docs/abf-context/` | ABF 参照用メモ（`brief.md`・wishlist など）。Markdown |
| `reference/ocr/` | 種本のテキスト抽出チャンク（`fleisch/`・`schutz/`・`doran/`・`flanders/` など）。**`.gitignore` で除外**（手元生成・RAG 用） |
| `volumes/ch03/` | 第3章（vol03）— `main/`・`note/`・`handoff-prompt.md` を `differential-forms-notes` から複写済み |
| `volumes/` 他 | シリーズ拡張時に同様の慣習で追加 |

## ABF から参照させるには

`abf/abf.config.json` の `draft.referenceGlobs` に、少なくとも次を含める:

```json
"draft": {
  "referenceGlobs": [
    "../nabla-kaitai/docs/abf-context/**/*.md",
    "../nabla-kaitai/reference/ocr/**/*.md"
  ]
}
```

（他リポの参照コーパスを足す場合は同配列に glob を追加。）

## DevOrchestrator

プロジェクトキー: **`nabla-kaitai`**、チケット接頭辞: **`NKAI`**（`docs/tickets/` を置く場合）。
