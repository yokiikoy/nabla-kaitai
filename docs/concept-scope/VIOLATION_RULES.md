# Concept Scope Violation Rules

## 1. Purpose

この文書は Concept Scope LSP が返す diagnostics の基準を定義する。

目的は、Markdown 原稿の構文検査ではなく、教科書の教育的順序を守ることである。

対象とする違反は大きく 2 種類である。

1. 未来概念のフライング
2. 既習概念の過剰再説明

## 2. Severity Levels

| Severity | 用途 |
|---|---|
| `Error` | 教育的順序を壊す。原稿に残すべきでない |
| `Warning` | 冗長、または章の役割を曖昧にする |
| `Information` | 許可範囲内だが注意が必要 |
| `Hint` | 執筆補助の提案 |

## 3. Usage Levels

| Level | 説明 | 代表的な表現 |
|---|---|---|
| `mention` | 名前だけ出す | 「次章でホッジ・スターを導入する」 |
| `intuition` | 直感・比喩として説明する | 「後で出てくる辞書」 |
| `definition` | 定義する | 「X を次で定義する」 |
| `formula` | 具体式を書く | `\ast dx = dy \wedge dz` |
| `computation` | 計算に使う | `\ast d\omega` を展開する |
| `theorem_use` | 定理として使う | 「ストークスの定理より」 |

## 4. Rule: Future Concept Formula

### 4.1 Description

現在章で `mention` または `intuition` までしか許可されていない概念について、具体式が出現した場合は `Error` とする。

### 4.2 Examples

第4章で禁止:

```tex
\ast dx = dy \wedge dz
```

```tex
\ast(df)
```

```tex
\ast d\omega
```

### 4.3 Diagnostic

```yaml
code: future-concept-formula
severity: Error
message: "この概念の具体式は現在章では未定義です。名前だけの伏線に留めてください。"
```

## 5. Rule: Future Concept Computation

### 5.1 Description

現在章で導入されていない概念を、式変形・計算・証明の根拠として使った場合は `Error` とする。

### 5.2 Examples

第4章で禁止:

```markdown
ホッジ・スターを作用させると...
```

```markdown
grad, rot, div はそれぞれ次のように表される。
```

```tex
\operatorname{rot}(\operatorname{grad} f)=0
```

### 5.3 Diagnostic

```yaml
code: future-concept-computation
severity: Error
message: "この章ではまだ計算に使えない概念です。導入章以降へ移動してください。"
```

## 6. Rule: Premature Theorem Use

### 6.1 Description

定理を導入・構築している章で、その定理を既知のものとして使った場合は `Error` とする。

### 6.2 Examples

ストークスの定理を導出する前の節で禁止:

```markdown
ストークスの定理より、左辺は...
```

```tex
\int_{\partial M}\omega = \int_M d\omega
```

ただし、その式を「これから得たい形」「導出結果」として提示する場合は許可される。

### 6.3 Diagnostic

```yaml
code: premature-theorem-use
severity: Error
message: "この定理を既知として使っている可能性があります。導出前なら根拠を局所計算に戻してください。"
```

## 7. Rule: Over-Explanation of Known Concept

### 7.1 Description

すでに前章で定義済みの概念を、現在章で再び定義レベルで長く説明した場合は `Warning` とする。

### 7.2 Examples

第4章で警告:

```markdown
ウェッジ積とは、2つの $1$-form から...
```

```markdown
$1$-form とは、ベクトルを1つ食べて...
```

短い復習・参照は許可する。

### 7.3 Diagnostic

```yaml
code: over-explanation
severity: Warning
message: "この概念は既に定義済みです。この章では短い参照に留める方針です。"
```

## 8. Rule: Forbidden Notation Before Contract

### 8.1 Description

本書の記号契約に反する表記は、導入順序とは独立に `Error` とする。

### 8.2 Examples

常に禁止:

```tex
dx^2
```

```tex
dx²
```

計量導入前に禁止:

```tex
\sqrt{dx^2 + dy^2}
```

### 8.3 Diagnostic

```yaml
code: notation-contract
severity: Error
message: "本書では dx は横ベクトルです。二乗する場合は dx(v)^2 のように作用後のスカラーを二乗してください。"
```

## 9. Rule: Integral Notation Mismatch

### 9.1 Description

積分対象の次数と積分記号の次元が合わない場合は `Warning` または `Error` とする。

### 9.2 Examples

閉曲面上の $2$-form に `\oint` を使う:

```tex
\oint_{\partial V}\eta
```

推奨:

```tex
\iint_{\partial V}\eta
```

### 9.3 Diagnostic

```yaml
code: integral-dimension-mismatch
severity: Warning
message: "閉曲面上の $2$-form 積分には \\iint を使う方針です。"
```

## 10. Rule: Allowed Foreshadowing

### 10.1 Description

未来概念でも、章スコープで `previews` に登録され、許可レベル以内で使われている場合は diagnostics を出さない。

### 10.2 Examples

第4章で許可:

```markdown
次章では、ホッジ・スターという辞書を導入する。
```

```markdown
長さや大きさを取り出す追加の規則は、次章で正式に扱う。
```

### 10.3 Non-Examples

第4章で禁止:

```tex
\ast(dx)=dy\wedge dz
```

```markdown
ホッジ・スターを使えば、回転は次のように書ける。
```

## 11. Initial Regex Rules

初期実装では、完全な意味解析ではなく正規表現で近似する。

### 11.1 Always Forbidden

```yaml
notation_contract:
  - pattern: "dx\\^2|dy\\^2|dz\\^2"
    code: notation-contract
    severity: Error
  - pattern: "dx²|dy²|dz²"
    code: notation-contract
    severity: Error
```

### 11.2 Forbidden Before ch05

```yaml
hodge_star_formula:
  chapter_before: 5
  patterns:
    - "\\\\ast\\s*\\("
    - "\\\\ast\\s*dx"
    - "\\\\ast\\s*dy"
    - "\\\\ast\\s*dz"
    - "\\*dx"
    - "\\*dy"
    - "\\*dz"
  code: future-concept-formula
  severity: Error
```

### 11.3 Restricted Before ch05

```yaml
nabla_dictionary:
  chapter_before: 5
  patterns:
    - "operatorname\\{rot\\}"
    - "operatorname\\{div\\}"
    - "operatorname\\{grad\\}"
    - "grad\\s*\\("
    - "rot\\s*\\("
    - "div\\s*\\("
  code: future-concept-computation
  severity: Error
```

### 11.4 Warning After Definition

```yaml
over_explanation:
  patterns:
    - "とは、.*を.*返す"
    - "とは何か"
    - "定義し直す"
  code: over-explanation
  severity: Warning
```

## 12. LLM Prompt Integration

Diagnostics は執筆者向けである。一方、LLM には診断結果だけでなく、現在章のスコープを事前に渡す。

LSP または補助 CLI は、次のような Markdown を生成する。

```markdown
Current chapter: ch04

Allowed:
- exterior_derivative: up to computation
- stokes_theorem: derive/formula only after local construction

Preview only:
- hodge_star: mention/intuitive preview only
- metric: intuitive preview only
- grad/rot/div: names only, no formulas

Do not re-explain:
- $1$-form
- $2$-form
- wedge product
- form integral

Forbidden:
- \ast dx = ...
- \ast d\omega
- operatorname{rot}(operatorname{grad})
- \oint_{\partial V}\eta
```

この出力を LLM への執筆プロンプトの先頭に挿入する。

