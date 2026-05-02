# ch04 Revision Plan

Date: 2026-04-27

Status: executed on 2026-04-27

Target:

- `manuscript/ja/ch04/ch04.md`

Purpose:

- Keep chapter 4 as the bottom-up construction of exterior derivative `d`.
- Fix mathematical precision issues before doing prose-level polish.
- Preserve the educational route: `df` -> closed-loop mismatch -> micro-loop density -> `d` -> Stokes/Gauss structure -> local laws.

## Summary Judgment

The chapter has a strong core. The local-loop derivation of `(Q_x-P_y)` is the right pedagogical engine, and the chapter succeeds at making `d` feel like a measurement operator rather than a formal symbol.

The main fixes are:

1. Separate "infinitesimal leading term" from exact finite-loop statements.
2. Correct the matrix sign convention in appendix B.3 and every reference to it.
3. Remove or soften pre-ch05 Hodge-star / grad-rot-div operational formulas.
4. Clean up Stokes/Gauss notation and orientation language.
5. Decide whether electromagnetic examples belong here or should be deferred.

## Revision Order

### Pass 1: Mathematical Corrections

#### 1. Fix B.3 sign convention

Locations:

- `ch04.md:617-645`
- `ch04.md:324`
- `ch04.md:675`

Current claim:

```tex
\mathbf{M}(d\omega) = \mathbf{J} - \mathbf{J}^T
```

Under the chapter 2 convention

```tex
(dx\wedge dy)(v_1,v_2)=v_1^T M v_2
```

the compatible matrix is:

```tex
\mathbf{M}(d\omega)=\mathbf{J}^T-\mathbf{J}
```

with

```tex
\mathbf{M}(d\omega)=
\begin{pmatrix}
0 & C & -B \\
-C & 0 & A \\
B & -A & 0
\end{pmatrix}
```

where:

```tex
A=R_y-Q_z,\quad B=P_z-R_x,\quad C=Q_x-P_y.
```

Action:

- Rename B.3 heading to `M = J^T - J`.
- Replace the matrix and boxed formula.
- Replace `J - J^T` references in §4.6 and B.5. B.5 remains zero either way, but the wording should match the corrected convention.

#### 2. Replace "exactly proportional" with "leading term / limit" language

Locations:

- `ch04.md:127-161`
- `ch04.md:181-185`
- `ch04.md:198`
- `ch04.md:213`
- `ch04.md:298-316`
- `ch04.md:349-362`

Problem:

The micro-loop calculation is first-order. For finite small rectangles, the expression is:

```tex
\oint \omega = (Q_x-P_y)\Delta x\Delta y + higher-order terms
```

It becomes exact only in the limit defining the local density, or after integration over a region using Stokes' theorem.

Action:

- At §4.3, explicitly define the local coefficient as:

```tex
\lim_{\Delta x,\Delta y\to 0}
\frac{1}{\Delta x\Delta y}\oint_{\partial R}\omega
= Q_x-P_y.
```

- Change "正確に比例する" to "主項として面積に比例する".
- Change "`d\omega` returns the loop integral around the parallelogram" to "`d\omega(v_1,v_2)` returns the infinitesimal circulation density on the parallelogram spanned by `v_1,v_2`."

#### 3. Avoid deriving `d(dx)=0` by assuming `d^2=0` too early

Locations:

- `ch04.md:239-249`
- `ch04.md:484`

Problem:

The chapter says `d(dx)=0` by provisionally assuming `d^2=0`, then later derives `d^2=0`. This is pedagogically understandable, but it creates a mild circularity.

Better route:

- Explain `d(dx)=0` as the fact that the coordinate measurement `dx` has constant coefficients in Cartesian coordinates, so it has no local loop mismatch.
- Or state it as a temporary algebra rule justified by the geometric computation and later generalized by `d^2=0`.

Action:

- Replace "もし外微分を2回続けてゼロになるよう設計すれば" with a geometry-first explanation.
- In the rule summary, say `d(dx)=d(dy)=d(dz)=0` is the coordinate-basis no-mismatch rule, later consistent with `d^2=0`.

#### 4. Fix Leibniz wording with 0-forms

Locations:

- `ch04.md:239-243`
- `ch04.md:376`
- `ch04.md:481`

Problem:

`P \wedge d(dx)` and `f \wedge d\omega` are technically interpretable if 0-forms wedge by multiplication, but they obscure the reader's type model.

Action:

- Prefer:

```tex
d(P\,dx)=dP\wedge dx + P\,d(dx)
```

and

```tex
d(f\,\omega)=df\wedge\omega + f\,d\omega.
```

#### 5. Correct closed-surface integral notation

Locations:

- `ch04.md:360`
- `ch04.md:398`
- `ch04.md:404`

Problem:

`\oint` is used for the boundary of a volume, where the domain is a closed surface. Earlier chapter 3 uses `\iint` for 2-form surface integration.

Action:

- Replace:

```tex
\oint_{\partial V}\eta
```

with:

```tex
\iint_{\partial V}\eta
```

- Keep `\oint` only for closed curves.

#### 6. Clarify the general Stokes argument

Locations:

- `ch04.md:294-328`
- `ch04.md:396-404`

Problem:

The derivation moves from an `xy` rectangle to a general surface `S`. This is the right intuition but too broad as stated.

Action:

- State that the argument is first for a small coordinate patch, then assembled patch-by-patch.
- Replace "xy平面への射影を介して" with "パラメータ平面上の小区画を通じて" or equivalent.
- Keep the cancellation of internal edges as the core image.
- In §4.6 note, avoid saying chapter 3 surface integrals "暗に Stokes を使っていた"; say instead that they used the same local patch/edge bookkeeping.

### Pass 2: Pedagogical Restructuring

#### 7. Reduce premature vector-analysis reveal

Locations:

- `ch04.md:285`
- `ch04.md:406`
- `ch04.md:443`
- `ch04.md:558-572`
- `ch04.md:585`

Problem:

Chapter 4 should build `d`; ch05/ch06 should name the vector-analysis dictionary. The current chapter gives too much of the reveal.

Action:

- Keep brief "既習者には見覚えがあるだろう" notes if useful.
- Remove explicit `rot(grad)` / `div(rot)` formulas from the chapter checkpoint.
- Replace §4.11 with a non-operational preview:

  - `d` raises degree.
  - The pattern `1,3,3,1` suggests a later dictionary.
  - That dictionary will be introduced in chapter 5.

- Do not write `\ast(dx)=...` or `\ast df` in chapter 4.

#### 8. Rework the electromagnetic subsection

Location:

- `ch04.md:527-545`

Problem:

The examples are motivating but currently too compressed and notation-heavy:

- `\oint_{\partial S}\mathbf{E}` suppresses the path pairing.
- `\iint_S\mathbf{B}` suppresses form degree and orientation.
- Constants/units are omitted.
- Maxwell in form notation is expected later in ch09.

Options:

1. Remove §4.10.2 and leave only a schematic "physical laws often have this shape" paragraph.
2. Keep it as a preview but explicitly label it schematic and defer precise electromagnetic form notation to ch09.

Recommended action:

- Use option 2 only if the chapter needs a physical payoff.
- Otherwise move the detailed examples to ch09 and keep ch04 focused.

#### 9. Remove source/sink imagery from closed-loop 1-form discussion

Locations:

- `ch04.md:103-105`

Problem:

For a 1-form closed-loop integral, "渦" and "循環" are the right images. "湧き出し" belongs to 2-form -> 3-form.

Action:

- In §4.2 use "渦", "循環", "帳尻のずれ".
- Save "湧き出し" for §4.7.

### Pass 3: Style / Contract Cleanup

#### 10. Match updated STYLE.md on Hodge and metric

Locations:

- `ch04.md:554-574`

Action:

- Since `STYLE.md` now permits non-operational foreshadowing, keep "後で導入する辞書" language.
- Remove concrete formulas and computation claims before ch05.

#### 11. Normalize `$1$-form` style

Locations:

- many lines, including `ch04.md:21`, `35`, `87`, `181`, `189`, etc.

Action:

- Use `$1$-form`, `$2$-form`, `$3$-form`, `$0$-form` in prose.
- Leave YAML title plain if needed.

#### 12. Normalize emphasis style

Locations:

- ch04 uses Markdown `**...**` heavily.

Action:

- If `STYLE.md` remains authoritative, convert source emphasis to `<strong>...</strong>`.
- This can be done after mathematical edits to avoid noisy diffs.

## Proposed Patch Sequence

1. **Patch A: math-critical**
   - B.3 sign.
   - §4.6 reference to the matrix.
   - `\oint_{\partial V}` -> `\iint_{\partial V}`.
   - `P \wedge d(dx)` / `f \wedge d\omega` cleanup.

2. **Patch B: micro/finite precision**
   - §4.3 leading-term and limit wording.
   - §4.4/§4.5 finite-loop wording.
   - §4.6/§4.7 tiling arguments with limit/patch caveats.

3. **Patch C: chapter-boundary discipline**
   - Rewrite §4.11 as a non-operational bridge to ch05.
   - Remove or soften vector-analysis formula reveals in checkpoints/notes.

4. **Patch D: physical examples**
   - Either simplify §4.10.2 into schematic preview or move it out.

5. **Patch E: style pass**
   - `$1$-form` notation.
   - `<strong>` emphasis if still required.
   - Heading/checkpoint polish.

## Acceptance Criteria

- [x] `d\omega` matrix convention matches chapter 2.
- [x] No chapter 4 text states that pointwise `d\omega(v_1,v_2)` equals a finite loop integral.
- [x] Closed surface integrals use 2D integration notation.
- [x] Hodge star appears only as a future non-operational dictionary in chapter 4.
- [x] ch04 remains understandable without knowing grad/rot/div.
- [x] The final paragraph clearly hands off to chapter 5 without pre-solving chapter 5.

## Execution Notes

- Updated `manuscript/ja/ch04/ch04.md`.
- Regenerated `manuscript/ja/ch04_note.md` from the updated main manuscript.
- Kept the note converter fix for align-like `\\[dim]` row breaks so regenerated note output does not retain unsupported spacing commands.
