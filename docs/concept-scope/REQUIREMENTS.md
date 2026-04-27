# Concept Scope LSP Requirements

## 1. Background

本プロジェクトでは、物理数学の教科書を Markdown Math 形式で執筆する。執筆には LLM を補助的に用いるが、LLM は通常の文章生成において、教科書固有の教育的順序を十分に保持できない。

現在、特に次の 2 つの問題が発生している。

### 1.1 未来知識のフライング

まだ後の章で定義する予定の概念、定理、演算、記法を、LLM が先回りして使ってしまう。

例:

- 第4章で、まだ第5章で定義するホッジ・スターの具体式を書く
- ストークスの定理を構築する章で、ストークスの定理を既知として使う
- grad / rot / div の対応を、対応辞書を導入する前に断定する

これは単なる用語ミスではなく、教科書の教育的構成を破壊する。

### 1.2 過去知識の再説明

すでに前章までで十分に導入した概念を、LLM が再びゼロから説明してしまう。

例:

- 第4章で $1$-form / $2$-form の定義を長々と再説明する
- 第3章以降でウェッジ積の基礎を毎回説明する
- 章の主題ではない既習概念に紙幅を使い、本文の進行を遅くする

これは冗長性の問題であると同時に、章ごとの役割分担を曖昧にする。

## 2. Objective

本設計の目的は、教科書執筆における概念の使用可能範囲を静的に管理するカスタム Language Server を構築することである。

この Language Server は、Markdown の構文チェックではなく、次の教育的制約を扱う。

- 現在の章で使用可能な概念
- 現在の章では名前だけ出してよい概念
- 現在の章では具体式や計算に使ってはいけない概念
- すでに定義済みなので再定義すべきでない概念
- 章内で新たに導入され、以後使用可能になる概念

対象エディタは OpenCode を想定する。実装には Python の `pygls` を用い、LSP 通信は stdio を基本とする。

## 3. Core Principle

概念管理は、単純な `known / unknown` の二値では不十分である。

教科書では、ある概念を次のような段階で扱うことがある。

| Level | 意味 | 例 |
|---|---|---|
| `mention` | 名前だけ出す | 「次章でホッジ・スターを導入する」 |
| `intuition` | 直感的な説明をする | 「面と線を結ぶ辞書が後で出てくる」 |
| `definition` | 定義する | 「外微分 $d$ を次で定義する」 |
| `formula` | 具体式を書く | `$d\omega = ...$` |
| `computation` | 計算に使う | `d(P dx)` を展開する |
| `theorem_use` | 定理として使う | ストークスの定理で式変形する |

したがって、各概念は「現在章で許される最大使用レベル」を持つべきである。

## 4. Scope

### 4.1 In Scope

この LSP は以下を扱う。

- Markdown ファイル冒頭の YAML フロントマター解析
- 章ごとの概念スコープ管理
- 概念依存関係グラフの構築
- 未来概念の使用検出
- 既習概念の過剰再説明検出
- Diagnostics による警告・エラー表示
- Hover による概念定義位置と要約表示
- Completion による既知概念候補の提示
- LLM に渡すための章スコープ要約の生成

### 4.2 Out of Scope

初期段階では以下を扱わない。

- LaTeX / Markdown の完全な構文解析
- 数式意味論の完全な証明検査
- 自然言語の完全な意味理解
- 概念出現の完全自動分類
- PDF ビルドや note.com 変換

本ツールは証明支援系ではなく、教育的スコープの静的検査器である。

## 5. Data Model

### 5.1 Concept

概念は、表層語ではなく安定した ID で管理する。

```yaml
id: hodge_star
label: "ホッジ・スター"
aliases:
  - "Hodge star"
  - "ホッジスター"
  - "\\ast"
kind: operator
summary: "計量と向きに基づき、k-form と (n-k)-form を対応させる演算子。"
```

### 5.2 Chapter Scope

各章は、章開始時点で使用可能な概念と、その章で導入される概念を明示する。

```yaml
---
id: ch04
title: "外微分 d"
chapter: 4
order: 40

assumes:
  - differential_form
  - wedge_product
  - line_integral
  - surface_integral

introduces:
  exterior_derivative:
    from: intuition
    to: computation

previews:
  hodge_star:
    max_level: intuition
    note: "第5章で定義する。具体式や計算には使わない。"

recap_policy:
  differential_form:
    max_level: mention
    max_lines: 3
  wedge_product:
    max_level: mention
    max_lines: 3
---
```

### 5.3 Concept Usage

本文中の概念使用は、可能であれば次の属性に分類する。

```yaml
concept_id: hodge_star
surface: "\\ast(dx)"
level: formula
line: 123
column: 8
```

初期実装では、この分類は正規表現とキーワードルールで近似する。将来的には、Markdown AST、LaTeX AST、または LLM 補助の分類を併用してよい。

## 6. YAML Frontmatter Schema

### 6.1 Required Fields

各章ファイルは最低限、次を持つ。

```yaml
---
id: ch04
title: "外微分 d"
chapter: 4
order: 40
provides:
  - exterior_derivative
requires:
  - differential_form
  - wedge_product
---
```

### 6.2 Recommended Fields

実運用では、次の詳細スキーマを推奨する。

```yaml
---
id: ch04
title: "外微分 d"
part: 1
chapter: 4
order: 40
lang: ja

assumes:
  - differential_form
  - wedge_product
  - line_integral
  - surface_integral

introduces:
  exterior_derivative:
    label: "外微分"
    aliases: ["d", "外微分 d"]
    from: intuition
    to: computation
    summary: "k-form を (k+1)-form に送り、局所的なズレを測る演算子。"

develops:
  stokes_theorem:
    from: intuition
    to: formula

previews:
  hodge_star:
    max_level: intuition
    allowed_patterns:
      - "次章で.*ホッジ"
    forbidden_patterns:
      - "\\\\ast\\s*\\("
      - "\\\\ast\\s*dx"
      - "\\*dx"

recap_policy:
  differential_form:
    max_level: mention
    max_lines: 3
  wedge_product:
    max_level: mention
    max_lines: 3
---
```

## 7. Diagnostics Requirements

### 7.1 Future Concept Violation

現在章で許可されていない概念使用を検出する。

例:

```tex
\ast(dx) = dy \wedge dz
```

第4章で `hodge_star.max_level = intuition` の場合、これは `formula` 使用なので error とする。

Diagnostic:

- Severity: `Error`
- Source: `concept-scope`
- Code: `future-concept`
- Message: `ホッジ・スターの具体式は第5章で定義します。この章では名前だけの伏線に留めてください。`

### 7.2 Premature Theorem Use

定理を導入する前に、その定理を式変形の根拠として使った場合に検出する。

例:

- ストークスの定理を導出中に「ストークスの定理より」と書く

Diagnostic:

- Severity: `Error`
- Code: `premature-theorem-use`

### 7.3 Over-Explanation of Known Concept

既習概念を再定義・長文説明している可能性を検出する。

例:

- 第4章で「ウェッジ積とは、2つの $1$-form から...」と数段落説明する

Diagnostic:

- Severity: `Warning`
- Code: `over-explanation`
- Message: `ウェッジ積は前章までで定義済みです。この章では短い参照に留める方針です。`

### 7.4 Allowed Foreshadowing

未来概念の名前だけの予告は許可する。

例:

```markdown
次章では、ホッジ・スターという新しい辞書を導入する。
```

これは `mention` または `intuition` として許可する。

## 8. Hover Requirements

既知概念にカーソルを合わせると、次を表示する。

- 概念ラベル
- 定義された章
- 現在章での使用可能レベル
- 簡潔な説明
- 再説明すべきかどうか

例:

```markdown
外微分 d

Defined in: ch04
Current level: computation

k-form を (k+1)-form に送り、局所的なズレを測る演算子。
```

未来概念の場合:

```markdown
ホッジ・スター

Defined in: ch05
Current chapter: ch04
Allowed here: mention / intuition only

具体式や計算での使用は禁止。
```

## 9. Completion Requirements

Completion は、現在章で使用可能な概念を優先して提示する。

候補の分類:

- 使用可能な概念
- 伏線として名前だけ使用可能な概念
- 現在章では使用禁止の概念

使用禁止の概念は、補完候補から除外するか、明示的に deprecated として表示する。

## 10. LLM Context Export Requirements

LSP はエディタ診断だけでなく、LLM に渡すスコープ情報を生成できるべきである。

例:

```markdown
Current chapter: ch04

Allowed concepts:
- differential_form
- wedge_product
- line_integral
- surface_integral
- exterior_derivative: up to computation

Foreshadowing only:
- hodge_star: mention / intuition only. No formulas.
- grad_rot_div_dictionary: mention only.

Do not re-explain:
- differential_form
- wedge_product
- line_integral basics

Forbidden:
- \ast(dx) = ...
- grad / rot / div as established identities
- using Stokes before it is derived
```

この出力は、LLM 執筆プロンプトの先頭に挿入することを想定する。

## 11. Internal Architecture

### 11.1 Components

```text
concept-scope-lsp
├── frontmatter parser
├── workspace scanner
├── concept registry
├── chapter scope resolver
├── usage detector
├── diagnostic engine
├── hover provider
├── completion provider
└── LLM context exporter
```

### 11.2 Workspace Scan

保存時、または起動時にワークスペース内の Markdown ファイルを走査する。

収集する情報:

- file path
- document id
- chapter order
- provided concepts
- required concepts
- preview concepts
- recap policy

### 11.3 DAG Construction

概念依存関係は DAG として構築する。

```text
wedge_product -> differential_form_integration -> exterior_derivative -> stokes_theorem -> hodge_star_dictionary
```

ただし、章の教育的順序は DAG だけでは決まらない。必ず `order` を併用する。

### 11.4 Scope Resolution

あるファイルに対して、次を計算する。

- `available_concepts`: 現在章までに導入済み
- `introduced_here`: 現在章で導入中
- `preview_only`: 名前または直感だけ許可
- `future_concepts`: 現在章より後で導入
- `recap_limited`: 再説明を制限すべき既習概念

## 12. Implementation Phases

### Phase 0: Design Artifacts

作成するファイル:

```text
docs/concept-scope/REQUIREMENTS.md
docs/concept-scope/CONCEPTS.yaml
docs/concept-scope/CHAPTER_SCOPES.yaml
docs/concept-scope/VIOLATION_RULES.md
```

### Phase 1: Minimal Diagnostics Prototype

目的:

- LSP が OpenCode に接続できること
- 保存時に diagnostics を返せること

実装:

- `pygls`
- stdio
- ハードコードされた禁止キーワード検出

### Phase 2: YAML Frontmatter Integration

目的:

- 各章の frontmatter からスコープを読む
- `order` に基づき未来概念を判定する

実装:

- `pyyaml`
- Markdown ファイル走査
- concept registry 構築

### Phase 3: Concept Usage Levels

目的:

- `mention` と `formula` を区別する
- 伏線許可と具体式禁止を両立する

実装:

- 正規表現ルール
- `forbidden_patterns`
- `allowed_patterns`

### Phase 4: Hover and Completion

目的:

- 執筆中に概念の定義位置・使用可能範囲を確認できるようにする

実装:

- `textDocument/hover`
- `textDocument/completion`

### Phase 5: LLM Context Export

目的:

- 現在章の執筆制約を LLM に渡せる形式で出力する

実装:

- LSP command
- Markdown / JSON 形式のスコープ出力

## 13. Acceptance Criteria

### 13.1 Functional Criteria

- Markdown 保存時に diagnostics が更新される
- 未来概念の具体式使用が error になる
- 未来概念の名前だけの伏線は許可される
- 既習概念の再定義が warning になる
- Hover で概念の定義章と要約が表示される
- Completion で現在章に適した概念が優先表示される

### 13.2 Pedagogical Criteria

- 各章が「何を新しく教える章か」を明示できる
- 章の主題でない既習概念の再説明を抑制できる
- 後の章の定理や演算を先に使う事故を検出できる
- LLM に渡す執筆制約を機械的に生成できる

### 13.3 Non-Goals

- 数学的証明の完全な正しさを保証しない
- 自然言語の意味を完全には理解しない
- すべての誤用を自動検出することを目標にしない

## 14. Initial Design Decision

初期実装では、概念スコープ管理を次の方針で進める。

1. 概念は stable ID で管理する
2. 表層語は `aliases` として扱う
3. 使用可能性は `known / unknown` ではなく level で管理する
4. 章順序は DAG ではなく `order` で判定する
5. DAG は依存関係の検査に使う
6. 未来概念の禁止と、既習概念の再説明抑制は別ルールとして扱う
7. LSP は最終目的ではなく、LLM 執筆制約をリアルタイムに可視化する UI として扱う

