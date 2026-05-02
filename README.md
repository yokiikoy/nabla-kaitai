# ナブラ解体新書

『ナブラ解体新書 —— 行列表示の微分形式によるベクトル解析の抜け道 ——』の執筆リポジトリ。

3次元ユークリッド空間におけるベクトル解析を、微分形式の行列表示（横ベクトル＝一次形式）を通して再構成する教科書。全12章構成。

## 構成

```
manuscript/
  ja/           日本語原稿（全12章 + 序章・付録・参考文献）
  en/           英訳版原稿
  README.md
exports/
  manuscript.pdf    生成済みPDF
  manuscript_combined.md  結合済みMarkdown（参照用）
  README.md
tools/
  build_pdf.py      PDF生成スクリプト（Python 3 + XeLaTeX）
  README.md
docs/              プロジェクト運用・構成・執筆ルール
README.md
```

## 章構成

| 章 | 内容 |
|---|---|
| 序章（ preface） | はじめに |
| 第1章 | $dx$ とは何か — 横ベクトルとしての一次形式 |
| 第2章 | 面積と体積 — $2$-form と $3$-form |
| 第3章 | 線積分・面積分 — 引き戻し |
| 第4章 | 外微分 $d$ — 微小ループのズレ |
| 第5章 | $d^2=0$ — 閉形式と完全形式 |
| 第6章 | 計量とホッジ・スター $\ast$ |
| 第7章 | 勾配・発散・回転の $\ast$ 辞書 |
| 第8章 | ガウスの定理・ストークスの定理 |
| 第9章 | 曲線座標での $\ast$ |
| 第10章 | 电磁気学への応用 |
| 第11章 | 多様体論との接続 |
| 第12章 | 今後の展望 |
| 付録 | 本書で語らなかったもの |
| 参考文献 | と著者からのコメント |

## PDF 生成

```bash
python3 tools/build_pdf.py
```

生成物：`exports/manuscript.pdf`

要環境：Python 3、 XeLaTeX（XeLaTeX 2回コンパイルで目次・相互参照解決）、IPAex フォント

## ライセンス

CC BY-NC 4.0（著作者：yokiikoy）