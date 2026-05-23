# Close-Reading Polish: Chapter 4

Review date: 2026-05-22
Branch: `ai/english-translation-ch04`
File: `manuscript/en/ch04/ch04.md`
GitHub issue: #182
PR context: #163

Scope: publication polish after Pass 3 — derivative notation (`\gamma'(t)`, `\theta'(t)`), modern English for derivatives, `J` vs `|J|` clarity, preservation of finite-cell discovery arc.

---

## Applied

### B items

- **B1** §4.0, §4.4: `differential coefficient(s)` → `derivative` / `partial derivatives`
- **B2** §4.1–§4.5: coordinate-function derivatives use `\gamma'(t)`, `x'(t)`, `y'(t)`, `\theta'(t)`; removed `dx/dt`, `dy/dt`, `d\theta/dt`, `d\gamma/dt` from determinants, checkpoints, and summaries; **kept** `dv/dt` in work-energy derivation (§4.1)
- **B3** §4.3: clarified signed `J` (formal pullback) vs `|J|` (non-oriented volume/mass)

### C items (straightforward)

- **C1** §4.0: `using boxy computation`
- **C2** §4.0: chapter-order blockquote → bullet list
- **C3** §4.1: pullback of physical-space $1$-form to time side
- **C4** §4.1: `\frac{dv}{dt}\,dt` / `\gamma^*(dv)` wording
- **C7** §4.2: note heading capitalization
- **C8** §4.2: measuring device eats finite cell
- **C9** §4.2: folded standalone `appears.` into preceding sentence
- **C10** §4.2: limiting rebuild wording for $\Phi^*$
- **C11** §4.2: consistency factor comparison to §4.1
- **C12** §4.2: difference ratios converge to partial derivatives
- **C13** §4.2: finite-cell / limiting rebuild split
- **C14** §4.2: final conservation sentence
- **C15–C16** §4.3: finite-cell version / limiting rebuild wording
- **C17** §4.3: consistency coefficient carries over
- **C18** §4.3: difference ratios wording
- **C19** §4.3: measured value assigned to finite box
- **C20** §4.3: `This agrees with the correct value.`
- **C21** §4.3: cross-chapter conservation pattern sentence
- **C22–C23** §4.4: Jacobian determinant wording
- **C25–C26** §4.5: checkpoint and summary consistency-factor wording
- **C27** §4.5: exterior derivative closing sentence

### Intentionally unchanged (D items / optional C)

- **C5** §4.1 work integral chain (`\int F\,dx = \int_{\gamma} F\,dx = \cdots`) — kept pedagogical step
- **C6** §4.1 pullback Aside (`push forward` typography) — preserved authorial voice
- **C24** §4.4 wedge compatibility sentence — kept as-is
- `boxy`, `make things consistent`, `rebuild measuring devices`, steps ①–⑦, full pullback Aside, `\Phi_h^\square` vs `\Phi^*`, curved cell vs parallelogram distinction, vector-analysis bridge notes, cylindrical mass calculation, exterior-derivative foreshadow

---

## Verification

Post-edit searches (expected: no matches):

- `differential coefficient`, `differential coefficients` — none
- `dx/dt`, `dy/dt`, `d\theta/dt` — none
- `velocity $d\gamma/dt$` — none
- `Jacobi determinant` — none
- `finite cell pullback` — none
- `We agree with the correct value` — none

`dv/dt` retained in §4.1 work-energy derivation (intentional).

`git diff --check` passes.
