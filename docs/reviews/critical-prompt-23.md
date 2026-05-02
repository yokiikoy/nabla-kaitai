# Critical Prompt 23 検証結果：標準理論への翻訳表

## 妥当性

Prompt 23 は非常に妥当。GitHub Issue としても、本文修正としても有用である。

## Issue 化候補

単独 Issue として「標準理論への翻訳表を追加する」を作る価値がある。

入れるべき最小表：

| 本書 | 標準理論 |
|---|---|
| `dx=(1 0 0)` | $dx^i|_p$ の標準双対基底表示 |
| `df` | $df\in\Omega^1(M)$ |
| `grad f` | $(df)^\sharp$ |
| `rot X` | $(*dX^\flat)^\sharp$ |
| `div X` | $*d*X^\flat$ |
| `2-form の行列` | 交代双線形形式の成分表示 |
| `*` | 計量・向き依存の Hodge star |
| 座標変換 | pullback / pushforward の区別 |

## 結論

Prompt 23 は Issue 化候補として採用。個別の `♭/♯` 修正と重複するため、親 Issue または付録追加 Issue として扱う。

