# ch01-ch04 Review

Date: 2026-04-27

Scope:

- `manuscript/ja/ch01/ch01.md`
- `manuscript/ja/ch02/ch02.md`
- `manuscript/ja/ch03/ch03.md`
- `manuscript/ja/ch04/ch04.md`

Review axes:

- `docs/REQUIREMENTS.md` compliance
- `docs/STYLE.md` compliance
- mathematical correctness
- pedagogical sequencing
- manuscript-to-note/PDF conversion risk

## Overall Assessment

Chapters 1-4 have a coherent main route: `dx` as a row-vector measurement operator, wedge products as algebraic area/volume meters, integration by Riemann-sum accumulation, and exterior derivative as the local operator behind boundary integrals. The educational spine is strong.

The main risks are not small wording issues. They are:

1. The `ds` passage exposes a deliberate terminology tension: `STYLE.md` says "`ds` は `$1$-form` である", while the displayed map is not linear in the input vector.
2. Some chapter-5 concepts are foreshadowed in chapters 1-4. Most of this is contextually acceptable, but ch04 §4.11 goes beyond foreshadowing into explicit formulas.
3. The matrix representation of `d\omega` in chapter 4 appendix B.3 has the opposite sign under the chapter 2 matrix convention.

## Critical Findings

### C1. `ds` terminology needs an explicit project decision

Location: `manuscript/ja/ch03/ch03.md:298-304`

The text defines:

```tex
ds(\mathbf{v}) = \sqrt{dx(\mathbf{v})^2 + dy(\mathbf{v})^2}
```

and then says this is a `$1$-form`. Under the book's own prior contract, a `$1$-form` is a linear measurement operator. This `ds` is homogeneous but not linear:

```tex
ds(\mathbf{v}_1+\mathbf{v}_2) \ne ds(\mathbf{v}_1)+ds(\mathbf{v}_2)
```

The text itself says it cannot be written as a linear combination of `dx` and `dy`, which confirms the issue.

However, this is not a simple manuscript slip: `docs/STYLE.md` explicitly lists the following as the "correct" position:

```text
「弧長は $1$-form の積分で書けない」 | 嘘。$ds$ は $1$-form である
```

So the real issue is a terminology-policy conflict:

- In standard differential-forms terminology, the displayed `ds` is not a differential `$1$-form` because it is not linear on tangent vectors.
- In the book's educational language, `ds` is being treated as a "one-dimensional measurement object" obtained from `dx,dy` plus a metric-like length rule.

Recommended fix:

- Decide whether the book intentionally uses `$1$-form` in a broader pedagogical sense here.
- If mathematical orthodoxy is preferred, change the manuscript to "line element" or "metric-derived length measurement", and update `STYLE.md`.
- If the current educational usage is retained, add one sentence making the convention explicit, for example: "`ds` は線形な微分形式ではないが、ここでは曲線に沿って1次元量を測る計量由来の測定器として扱う." This avoids silently breaking the earlier linearity contract.

### C2. Chapter 4 appendix B.3 has a sign error in the matrix representation of `d\omega`

Location: `manuscript/ja/ch04/ch04.md:621-645`

Chapter 2 uses the convention:

```tex
(dx \wedge dy)(\mathbf{v}_1,\mathbf{v}_2)
= \mathbf{v}_1^T
\begin{pmatrix}
0 & 1 & 0 \\
-1 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}
\mathbf{v}_2
```

For

```tex
d\omega =
A\,dy\wedge dz + B\,dz\wedge dx + C\,dx\wedge dy
```

with

```tex
A=R_y-Q_z,\quad B=P_z-R_x,\quad C=Q_x-P_y,
```

the matrix compatible with chapter 2 is:

```tex
\begin{pmatrix}
0 & C & -B \\
-C & 0 & A \\
B & -A & 0
\end{pmatrix}
```

The manuscript currently gives:

```tex
\begin{pmatrix}
0 & -C & B \\
C & 0 & -A \\
-B & A & 0
\end{pmatrix}
= \mathbf{J} - \mathbf{J}^T
```

That is the negative of the required matrix. With the current definition of `J`, the compatible statement is:

```tex
\mathbf{M}(d\omega) = \mathbf{J}^T - \mathbf{J}
```

or else the chapter 2 matrix convention must be changed, which would be much more invasive.

### C3. ch04 §4.11 goes beyond harmless foreshadowing of Hodge star

Locations:

- `manuscript/ja/ch01/ch01.md:437-442`
- `manuscript/ja/ch02/ch02.md:386`
- `manuscript/ja/ch02/ch02.md:603`
- `manuscript/ja/ch04/ch04.md:566-572`

`REQUIREMENTS.md` says chapter 5 is where the Hodge star first summons the metric. `STYLE.md` also says the Hodge star must not be used before chapter 5.

Reconsidered judgment:

- ch01 and ch02 mentions are mostly roadmap/foreshadowing. These are not major mathematical problems if the reader is not expected to use the concept yet.
- ch04 §4.11 is different. It gives an explicit mini-dictionary:

```tex
\ast(dx)=dy\wedge dz
```

and then states grad/rot/div combinations. This effectively defines and uses `\ast` before chapter 5.

There is also a mathematical precision issue in the sentence that grad/rot/div become `\ast d f`, `\ast d\omega`, `\ast d\ast\omega`. In the usual forms dictionary on Euclidean 3-space:

- `df` is the gradient as a `$1$-form` / covector.
- `\ast df` is a `$2$-form`, not the gradient vector itself.
- For a vector field represented by a `$1$-form` `\omega`, curl corresponds to `\ast d\omega`.
- Divergence corresponds to `\ast d\ast\omega` after the vector field has been represented as a `$1$-form`.

So the issue is not merely "too early"; the explicit formula risks teaching the wrong dictionary before ch05 has established exactly what is being identified.

Recommended fix:

- In ch01/ch02: roadmap mentions may stay if desired, but avoid operational formulas.
- In ch04 §4.11: keep the dimensional symmetry `1,3,3,1` and the promise of a later dictionary.
- Move explicit `\ast(...)` formulas and grad/rot/div compositions to ch05/ch06, where the metric and identification conventions can be stated carefully.
- If a preview sentence remains, phrase it non-operationally: "次章で導入する辞書により、これらはベクトル解析の見慣れた演算と結びつく."

## Major Findings

### M1. Metric and inner product are named repeatedly before the metric is supposed to be sealed

Locations:

- `manuscript/ja/ch02/ch02.md:37`
- `manuscript/ja/ch02/ch02.md:140`
- `manuscript/ja/ch02/ch02.md:500`
- `manuscript/ja/ch02/ch02.md:548`
- `manuscript/ja/ch02/ch02.md:578`
- `manuscript/ja/ch03/ch03.md:306`
- `manuscript/ja/ch03/ch03.md:391`

Some of these are framed as "not yet defined" notes, but `STYLE.md` explicitly warns against naming undefined concepts, even in negative form.

Recommended fix:

- Replace most pre-ch05 occurrences of "計量" and "内積" with "成分の二乗和の組み合わせ方" or "長さ・大きさを取り出す追加の規則".
- Keep at most one carefully placed "later dictionary" sentence if needed for motivation.

### M2. ch04 uses vector-analysis vocabulary too early for the stated chapter-II experience

Locations:

- `manuscript/ja/ch04/ch04.md:285`
- `manuscript/ja/ch04/ch04.md:406`
- `manuscript/ja/ch04/ch04.md:443`
- `manuscript/ja/ch04/ch04.md:558-572`

`REQUIREMENTS.md` says chapter II should build the tools from zero and only later reveal "that was grad/rot/div." The current text gives that reveal inside chapter 4. This weakens the intended drama of ch05/ch06.

Recommended fix:

- In ch04, use "既習者への脚注" sparingly.
- Prefer "この係数列は、後に見慣れた演算子の正体として再登場する" without naming all operators.
- Reserve full grad/rot/div identification for ch06.

### M3. ch04's electromagnetic examples are too early and technically under-specified

Location: `manuscript/ja/ch04/ch04.md:527-545`

The examples are useful but risky at this point:

- They use bold vector notation inside integral formulas, then switch to forms.
- Constants and units are omitted.
- `B`, `D`, and `rho` require careful degree and unit handling.
- The project requirements place Maxwell-form discussion mainly in ch09.

Recommended fix:

- Either remove this subsection from ch04 and defer to ch09, or turn it into a short non-formal preview.
- If retained, state explicitly that constants/orientations/units are suppressed and this is a schematic example.

### M4. "Closed loop nonzero" is associated with both rotation and source-like language

Location: `manuscript/ja/ch04/ch04.md:103-105`

For a 1-form, nonzero closed-loop integral detects circulation/curl-like behavior. "湧き出し" is a divergence/source image and belongs more naturally to the 2-form-to-3-form discussion in §4.7.

Recommended fix:

- In §4.2, keep the image to "渦" or "循環".
- Save "湧き出し" for §4.7.

### M5. The Stokes derivation over general surfaces is pedagogically useful but mathematically too broad as stated

Location: `manuscript/ja/ch04/ch04.md:294-328`

The derivation starts from `xy`-plane rectangles and then speaks about a general surface `S`. This is the right intuition, but the transition from planar tiling to arbitrary oriented surfaces needs either a caveat or a pullback-based explanation.

Recommended fix:

- Say this is first shown for surfaces parametrized by small coordinate patches.
- Mention that the general surface is assembled from such patches, with orientations matched on shared edges.

### M6. The chapter 3 transformation formula mixes signed form integration and positive-volume convention

Location: `manuscript/ja/ch03/ch03.md:627-631`

The text writes a `3`-form pullback formula but inserts `|J|` in the integral. For oriented form integration, the signed Jacobian `J` is the natural object. `|J|` belongs to positive scalar volume integration after choosing to ignore orientation.

The text does partly explain this, but the displayed formula may teach the wrong default.

Recommended fix:

- Display the signed-form version first.
- Then add a second sentence/formula for positive volume using `|J|`.

## Minor / Style Findings

### S1. `**` and `<strong>` are mixed in source manuscripts

Examples:

- ch04 uses many `**...**`
- earlier chapters use many `<strong>...</strong>`

`STYLE.md` says source emphasis should use `<strong>`.

Recommended fix:

- Decide whether source manuscripts now prefer `<strong>` or Markdown `**`.
- If `<strong>` remains the source rule, convert ch04 and scattered `**` usages.

### S2. Heading depth is inconsistent

Examples:

- `manuscript/ja/ch01/ch01.md:9` uses `#### §1.1`
- Other major sections usually use `###`.

Recommended fix:

- Normalize major sections to `### §x.y`.
- Use `#### x.y.z` for subsections.

### S3. `1-form` formatting is not fully aligned with the stated `$1$-form` rule

Examples:

- ch04 front matter and prose contain `1-form`, `2-form`, `3-form` without math-wrapped numerals.

Recommended fix:

- Use `$1$-form`, `$2$-form`, `$3$-form` in prose, except in YAML front matter if plain text is desired.

### S4. The ch03 appendix explicitly says it violates the book's policy

Location: `manuscript/ja/ch03/ch03.md:643-665`

This is honest, but it may weaken reader trust. If the appendix is needed, frame it as an intentionally lower-dimensional analogy rather than "契約に反する".

Recommended fix:

- Replace "本書のポリシーに反する" / "記法契約に反する" with "ここだけは補助図として2次元断面を見る".

## Positive Findings

- ch01 repeatedly reinforces the core `dx` contract and the distinction between `dx` and `dx(v)`.
- ch02's wedge-product construction from tensor products is pedagogically effective and mostly internally consistent.
- ch03 correctly defines `\iiint`, `\iint`, and `\int_\gamma` via Riemann-sum accumulation before using them operationally.
- ch04's local-loop derivation of `Q_x-P_y` is a strong bottom-up route to exterior derivative.
- The ch04 derivation of `d\eta=(A_x+B_y+C_z)dx\wedge dy\wedge dz` is educationally clear and aligns well with the later divergence interpretation.

## Suggested Fix Order

1. Fix ch04 appendix B.3 sign convention.
2. Resolve `ds`: either stop calling it a `$1$-form`, or explicitly change the book's definition of "form" to include metric-derived nonlinear line elements. The latter is not recommended.
3. Move explicit Hodge-star formulas and grad/rot/div identifications out of ch01-ch04.
4. Remove or soften pre-ch05 metric/inner-product mentions.
5. Decide whether ch04 should keep the electromagnetic preview.
6. Normalize emphasis and heading depth.
7. Re-run note/PDF conversion checks after source cleanup.

## Follow-up Review Passes

After the above fixes, rerun:

- a notation scan for `\ast`, `ホッジ`, `計量`, `内積`, `grad`, `rot`, `div`, `ヤコビアン`
- a math scan for matrix signs in all wedge/matrix correspondence tables
- a conversion scan over `*_note.md` to ensure note output matches source content
