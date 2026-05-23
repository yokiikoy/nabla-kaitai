# Close-Reading Polish: Chapter 3

Review date: 2026-05-22  
Branch: `ai/english-translation-ch03`  
File: `manuscript/en/ch03/ch03.md`  
GitHub issue: #181  
PR context: #162

Scope: publication polish after Pass 3 — notational safety (`x'(t)` vs `dx/dt`), first-order wording for `dF(\mathbf{v})`, English naturalness, preservation of authorial voice.

---

## Applied

### B items

- **B1** §3.3.1–§3.4.1: replaced `dx/dt`, `dy/dt`, `dz/dt` with coordinate-function derivatives `x'(t)`, `y'(t)`, `z'(t)`; line-integral limit uses explicit evaluation `P(\gamma(t))x'(t)+\cdots`; Riemann-sum step uses `\omega_{\gamma(t_i)}` with coefficients at `\gamma(t_i)`.
- **B2** §3.2.2: `dF` reads off the **first-order change** in $F$ (aligned with Chapter 1 `df(\mathbf{v})` polish).

### C items (straightforward)

- **C2** §3.0: `apply them to curves, surfaces, and regions`
- **C3** §3.0: `returns the volume of a region directly`
- **C4** §3.1.2: inside-out summation order clarified (`x \to y \to z`)
- **C5** §3.2.1: `signed area … directly`
- **C6** §3.2.1: surface-element aggregate wording
- **C7** §3.2.2: tangent-displacement wording
- **C8** §3.2.2: `This tells us exactly what … measures`
- **C9** §3.2.3: `Taken together, these three components`
- **C10** §3.2.3: lower-hemisphere projected-area signs
- **C11** §3.2.4 checkpoint: `signed area of the shadow`
- **C12** §3.3.1: `small subintervals`
- **C13** §3.3.2: component displacements cancel over one full turn
- **C15** §3.3.3: geometric examples / coefficient-$1$ sentence
- **C16** §3.4.0: `oriented cross-section`
- **C17** §3.4.0: `gives a general $k$-form`
- **C18** §3.4.1: explicit evaluation in Riemann-sum formula (with B1)
- **C19** §3.4.2: `we call $\eta$ a general $2$-form`
- **C20** §3.4.2: `guide rail` → `guidepost`
- **C22** §3.5: `Across degrees … the picture remains the same`
- **C23** §3.5 checkpoint: work / vector-analysis correspondence wording
- **C24** §3.5 checkpoint: `coefficients … and basis $k$-forms`
- **C26** §3.5: `a matter of "moving points"`

### Intentionally unchanged (D items / optional C)

- **C1** §3.0 sphere-formulas opening rhythm (`"formulas of that kind"`) — preserved authorial voice
- **C14** §3.3.2 `"power to measure length"` — kept as-is
- **C21** §3.4.4 Riemann-sum `\omega_{p_i}` notation — optional; current text readable after §3.4.1
- **C25** §3.5 `cannot get away without` — preserved stronger voice
- Equator singularity, `messy` / `shadow` / `escape` vocabulary, `ds`/`dS` not-forms statements, full sphere derivations

---

## Verification

Post-edit searches (expected: no matches except intentional `\Delta x_i/\Delta t` finite ratios):

- `dx/dt`, `dy/dt`, `dz/dt` — none
- `reads off the change in $F$` — none
- `returns the volume of a region as-is` — none
- `returns the signed area of a small piece on the $xy$ plane as-is` — none
- `we call a general $2$-form` — none
- `Work is $\int_\gamma \omega$, the same quantity as` — none

`git diff --check` passes.
