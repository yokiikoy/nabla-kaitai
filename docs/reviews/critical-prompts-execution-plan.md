# 批判的読解プロンプト実行計画

作成日: 2026-05-03

## 目的

`nabla_kaitai_critical_prompts.md` の25個のプロンプトを、現行原稿の章構成に合わせて補正したうえで順に実行する。実行結果は、そのまま GitHub issue にせず、まず本文根拠つきの issue 候補として整理する。

## 基本方針

- プロンプト番号順に実行する。
- 章番号はプロンプト文面ではなく、現行原稿のファイル構成を優先する。
- 「査読レポート」と「GitHub issue」は分ける。
- issue 候補は、該当箇所、誤読リスク、修正方針が具体化できるものだけに絞る。
- 著者の人格・動機・文体への批判は issue 化しない。
- 「標準理論ではこうだ」という一般論だけでは issue 化しない。本文の実際の記述と結びつける。
- 既存の注・付録・第11章で十分に回収済みの論点は、原則として issue にしない。

## 現行原稿への補正マップ

| Prompt | 元の対象 | 現行原稿での主対象 | 実行上の補正 |
|---|---|---|---|
| 1 | 全体地図化 | `manuscript/ja/**/*.md`, `toc.md`, `appendix.md`, `afterword.md`, `references.md` | 全体の中心主張と危険論点を抽出する。 |
| 2 | 第1章 dx, dy, dz, df | `manuscript/ja/ch01/ch01.md` | 章対応はそのまま。第11章の回収記述も参照する。 |
| 3 | 第2章 2-form, 3-form, wedge | `manuscript/ja/ch02/ch02.md` | 章対応はそのまま。付録Aも対象。 |
| 4 | 第3章 引き戻し等 | `manuscript/ja/ch03/ch03.md`, `manuscript/ja/ch04/ch04.md`, `manuscript/ja/ch01/ch01.md` §1.4-1.5 | 「線積分・面積分」はch03、「引き戻し・座標変換」はch04中心に分割して読む。 |
| 5 | 第4章 外微分 | `manuscript/ja/ch05/ch05.md` | 現行では外微分は第5章。Prompt 5はch05へ読み替える。 |
| 6 | 第5章 Stokes型定理 | `manuscript/ja/ch05/ch05.md`, `manuscript/ja/ch07/ch07.md`, `manuscript/ja/ch08/ch08.md` | ch05のStokes/Gauss導入、ch07-ch08のベクトル解析翻訳を横断する。 |
| 7 | 第6章 計量・Hodge star | `manuscript/ja/ch06/ch06.md` | 章対応はそのまま。付録Dも対象。 |
| 8 | 第7章 grad/curl/div | `manuscript/ja/ch06/ch06.md`, `manuscript/ja/ch07/ch07.md`, `manuscript/ja/ch08/ch08.md` | grad/curl/divはch06で微分形式接続、ch07で伝統記法、ch08で翻訳辞書として読む。 |
| 9 | 第8章 物理応用 | `manuscript/ja/ch03/ch03.md`, `manuscript/ja/ch05/ch05.md`, `manuscript/ja/ch09/ch09.md`, `manuscript/ja/ch10/ch10.md`, `manuscript/ja/ch12/ch12.md` | 物理応用は分散しているため横断監査に変更する。 |
| 10 | 第9章 曲線座標 | `manuscript/ja/ch01/ch01.md` §1.4-1.5, `manuscript/ja/ch08/ch08.md` §8.6, `manuscript/ja/ch09/ch09.md` | ch09だけでなく、早期の円柱座標導入とch08の辞書も対象。 |
| 11 | 第10章 高次元化 | `manuscript/ja/ch10/ch10.md`, `manuscript/ja/ch11/ch11.md`, `manuscript/ja/ch12/ch12.md` | 現行ch10は4次元マクスウェル、一般化はch11、クリフォード接続はch12として読む。 |
| 12 | 第11章 標準微分幾何 | `manuscript/ja/ch11/ch11.md` | 章対応はそのまま。前半の回収可否を評価する。 |
| 13 | 第12章 結論・射程 | `manuscript/ja/ch12/ch12.md`, `manuscript/ja/afterword.md`, `manuscript/ja/appendix.md`, `manuscript/ja/references.md` | 現行ch12は発展章なので、結論・射程監査は後書き・付録・参考文献コメントも含める。 |
| 14 | 付録・予防線 | `manuscript/ja/preface.md`, `manuscript/ja/appendix.md`, 各章の注 | 予防線は本文全体に分散しているため、検索語ベースで横断する。 |
| 15 | 等号監査 | 全体 | 重要な等号だけを抽出し、issue候補は誤読リスクが高いものに限定する。 |
| 16 | 係数・符号・向き | 全体 | wedge, Hodge star, curl/div, Stokes/Gauss を重点に見る。 |
| 17 | 計量依存性 | 全体 | d/wedge/pullback と metric/Hodge/grad/curl/div の境界を重点に見る。 |
| 18 | LLMが納得しやすい言説構造 | 全体 | issue化は慎重に行い、本文改善に結びつく表現だけを候補にする。 |
| 19 | 専門家向け査読レポート | 1-18の結果 | 個別issue生成ではなく総括成果物として使う。 |
| 20 | 一般向け短評 | 1-18の結果 | 公開文案であり、issue生成フェーズでは補助扱い。 |
| 21 | 最終判定・反論耐性 | 1-18の結果 | 重複排除と優先順位付けに使う。 |
| 22 | 安全な読解ガイド | 1-18の結果 | まとまった読者注釈 issue または docs 追加案に変換する。 |
| 23 | 標準理論への翻訳表 | 1-18の結果 | まとまった翻訳表 docs 追加案に変換する。 |
| 24 | 章別レッドフラッグ | 1-18の結果 | issue候補一覧の章別索引として使う。 |
| 25 | LLM用メタプロンプト | 1-18の結果 | 今後の監査ルールとして保存するか判断する。 |

## Issue候補の採用基準

採用する:

- 本文の具体行に根拠がある。
- 読者が誤読しうる対象・表示・計量・向き・次数などが明確である。
- 小さな注記、定義追加、記号変更、対応表追加など、修正方針が具体化できる。
- 同じ論点が複数章に現れる場合、代表箇所と横断 issue に整理できる。

採用しない:

- 「厳密な教科書ではない」という一般批判だけのもの。
- 既存注記で十分に限定済みのもの。
- 本書の教育方針そのものへの好悪。
- 修正不能な総評だけのもの。
- 著者の動機・属性・文体への批判。

## 実行成果物

各プロンプトについて、`docs/reviews/critical-prompt-XX.md` を作る。

各ファイルには以下を含める。

1. 補正後の対象ファイル
2. 本文根拠
3. 監査結果
4. issue候補
5. 次回以降へ引き継ぐ論点

GitHub issue 作成は、全候補の一覧化と確認後に別フェーズで行う。
