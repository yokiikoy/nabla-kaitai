# vol03-dx-as-matrix（仮）

1次元の微積分を「行列・一次形式」として読み替え、続けて面積・体積を 2-form / 3-form として組み立て、線・面・体の積分と引き戻しまでを統一する系統。

## 正本と変換

| 用途 | パス |
|------|------|
| 第1章（執筆正） | `main/ch01_matrix_calculus_main.md` |
| 第1章（note 表示用） | `note/ch01_matrix_calculus_note.md` |
| 第2章（執筆正） | `main/ch02_area_volume_main.md` |
| 第2章（note 表示用） | `note/ch02_area_volume_note.md` |
| 第3章（執筆正） | `main/ch03_integration_forms_main.md` |
| 第3章（note 表示用） | `note/ch03_integration_forms_note.md` |
| 第4章（執筆正・ドラフト） | `main/ch04_exterior_derivative_main.md` |
| 第4章（レビュー通過稿） | `main/ch04_exterior_derivative_main-reviewed.md` |

リポジトリ直下で:

```bash
./transform-note.sh volumes/note/vol03-dx-as-matrix/main/ch01_matrix_calculus_main.md volumes/note/vol03-dx-as-matrix/note/ch01_matrix_calculus_note.md
./transform-note.sh volumes/note/vol03-dx-as-matrix/main/ch02_area_volume_main.md volumes/note/vol03-dx-as-matrix/note/ch02_area_volume_note.md
./transform-note.sh volumes/note/vol03-dx-as-matrix/main/ch03_integration_forms_main.md volumes/note/vol03-dx-as-matrix/note/ch03_integration_forms_note.md
```

## 連続稿（第1章〜第3章・main）

エージェントや通読用に、**章別の `main/` を1ファイルに連結した生成物**を Git 管理する。

- **出力:** `main/full_through_ch03_main.md`（**手編集しない**。再生成で上書きされる）
- **生成:** `./scripts/concat-main-through-ch03.sh`

```bash
./volumes/note/vol03-dx-as-matrix/scripts/concat-main-through-ch03.sh
```

`ch01` / `ch02` / `ch03` を直したあと、上記を実行してからコミットする。

## 区切り線 `---`（horizontal rule）

- ファイル先頭の `---` … `---` は **YAML フロントマター専用**。
- 本文では **大節**（`### §N.M` または `# §N.M` 相当）の**直前**に `---` を入れる（前後は空行推奨）。`####` 小節の前には原則入れない。
- チェックポイント（`> **【ここまでのチェックポイント】**`）の前後は現状どおり `---` で区切ってよい。

詳細・トンマナ監査は巻内 [`handoff-prompt.md`](handoff-prompt.md) を参照。

## 引継ぎ

外部 LLM 向けの章立て・進捗・操作手順は [`handoff-prompt.md`](handoff-prompt.md)。
