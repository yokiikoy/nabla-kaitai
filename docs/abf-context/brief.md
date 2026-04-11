# ナブラ解体新書 — 執筆コンテキスト（ABF 参照用）

## シリーズ

**ナブラ解体新書**（リポジトリ `nabla-kaitai`）。∇（ナブラ）と周辺のベクトル解析・微分形式・幾何を、連載・書籍向けに再構成する。

## 第3章（本メモのフォーカス）

- **置き場**: `volumes/ch03/`（執筆正の Markdown はここから育てる）。
- **狙い（たたき台）**: 第3章で扱うトピック・読者レベル・前後章とのつなぎは、執筆しながら具体化する。本ファイルは ABF `draft` の参照コーパスとあわせて読ませる「方針メモ」として使う。

## 参照コーパス（`reference/ocr/`）

ABF の `draft.referenceGlobs` で読み込む。数式は OCR 誤りがありうる — **厳密な式は元 PDF・種本を正**とする。

| ソース | 役割 |
|--------|------|
| **Daniel A. Fleisch** — *A Student’s Guide to Vectors and Tensors* | ベクトル・テンソルの直観・入門的語り口 |
| **Bernard F. Schutz** — *Geometrical Methods of Mathematical Physics* | 幾何と物理のつなぎ、座標・多様体の基調 |
| **Chris Doran & Anthony Lasenby** — *Geometric Algebra for Physicists* | 幾何学的代数（GA）の語彙・表現 |
| **Harley Flanders** — *Differential Forms…*（OCR チャンク） | 微分形式まわりの用語・フレーズ整合（連載種本系） |

## まだ手元にない資料（メモのみ）

詳細は [wishlist-sources.md](wishlist-sources.md)。

- **Élie Cartan** の原論文・古典文献（外微分、Lie 群、移動標構など）
- **Andy Weir** の小説 — 数学参照ではないが、任意で文体・テンポの参考（合法入手のみ）

## ABF で下書きするときの例

プロンプトに「第3章」「参照コーパスに沿う／種本と矛盾しないよう注意」などを明示する。生成物は `abf/artifacts/` に出し、確定稿は `volumes/ch03/` へ移して本リポでコミットする。
