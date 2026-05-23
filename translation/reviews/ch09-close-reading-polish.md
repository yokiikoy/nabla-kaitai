# Close-Reading Polish: Chapter 9

Review date: 2026-05-23
Branch: `ai/english-translation-ch09`
File: `manuscript/en/ch09/ch09.md`
GitHub issue: #187
PR context: #170

Scope: publication polish after Pass 3 — curvilinear dictionary safety, orthonormal vs form-coefficient read-back, Markdown cleanup, preservation of “build the dictionary on the spot” arc.

---

## Applied

### B items

- **B1** Removed duplicate horizontal rules between §9.1/§9.2, §9.2/§9.3, and §9.3/§9.4
- **B2** §9.2.4: cylindrical curl read-back — $d\theta$ coefficient divided by scale factor $r$ (not $1/r$)

### C items (straightforward)

- **C1** §9.0: Chapter 8 highlight referent (`that chapter` / `routes`)
- **C2** §9.0 note: `$d$`, `$\ast d$`, or `$\ast d\ast$` as appropriate
- **C3** §9.0 note: manually attaching factors to `$\nabla$` formulas
- **C4** §9.2.3: scale-factor convention sentence
- **C5** §9.3.1: Hodge-star coefficients from scale factors
- **C7** §9.4: vector Laplacian identity with explicit parentheses
- **C8** §9.4: `$\nabla^2 F_\rho$` as scalar Laplacian on component
- **C9** §9.4/§9.5: single horizontal rule between major sections
- **C10** §9.5: point-charge divergence correspondence wording
- **C11** §9.5/§9.6: extra blank lines cleaned

### Intentionally unchanged (D items / optional C)

- **C6** §9.3.3 “Similarly, from `$\ast d\omega$`” — kept for brevity
- Three-step `J -> g -> *` recipe, “no memorizing formulas”
- Vector components vs $1$-form coefficients, four-layer tables
- Cylindrical/spherical final formulas, vector Laplacian decomposition
- Point-charge calculation, origin note, `$\rho_{\mathrm e}$` foreshadow
- Non-orthogonal caveat, Chapter 10 Maxwell bridge

---

## Verification

Post-edit searches (expected: no matches):

- duplicate `---` blocks — none
- `this chapter is the highlight` — none
- `Substitute the dictionary into $\ast d\ast$` — none
- `divided by $\frac{1}{r}$` (curl read-back) — none
- `diagonal components $\sqrt{1}` — none
- `$\ast d\ast\omega = \nabla\cdot\mathbf{E} = 0$` — none
- `rot` — none

`git diff --check` passes.
