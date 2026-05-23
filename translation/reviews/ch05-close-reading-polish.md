# Close-Reading Polish: Chapter 5

Review date: 2026-05-22
Branch: `ai/english-translation-ch05`
File: `manuscript/en/ch05/ch05.md`
GitHub issue: #183
PR context: #166

Scope: publication polish after Pass 3 — Markdown cleanup, mathematical safety in Appendix B.4.1, English naturalness, preservation of mismatch → $d$ → local law arc.

---

## Applied

### B items

- **B1** Removed duplicate horizontal rules between §5.3/§5.4, §5.6/§5.7, and §5.9/§5.10.
- **B2** §5.9.1: fixed sentence fragment (`Place Stokes' theorem … side by side`).
- **B3** Appendix B.4.1: `raw derivative components` before antisymmetrization (not misread as final $d\eta$ components).
- **B4** Appendix B.4.1: matrix/form factor convention wording (no implied visible missing `1/2`).

### C items (straightforward)

- **C1** §5.1.2: `To first order on each interval`
- **C2** §5.1.3: closed-curve exact form `xy(\gamma(2\pi))-xy(\gamma(0))=0`
- **C3** §5.2: measuring device applied along a line
- **C4** §5.3: higher-order terms sentence after tiny-loop sum
- **C5** §5.5.2: `we take $d$ to act linearly`
- **C6** §5.5.3: `guide rail` → `guidepost`
- **C7** §5.6: matrix $\mathbf{J}$ identified as Jacobian of $(P,Q,R)$
- **C8** §5.6 checkpoint: $\oint_{\partial S} \omega = \iint_S d\omega$
- **C9** §5.7.1: measuring device for flux through a surface
- **C11** §5.9.1: oriented boundary for $k=0$ Stokes case
- **C13** §5.9.1: `All fit into this single line`
- **C14** §5.10: note heading capitalization
- **C17** Appendix B.3: Chapter 2 convention sentence
- **C18** Appendix B.4.1: `combine into the trace`
- **C19** Appendix B.4.1: `reduces to a scalar coefficient`
- **C20** §5.10 / Appendix C: `\int_S J` spacing

### Intentionally unchanged (D items / optional C)

- **C10** §5.8 $d^2=0$ axiomatic note — kept concrete-calculation narrative
- **C12** §5.9 `does no harm` — preserved looser voice
- **C15** `Stokes's` — none found; already `Stokes'`
- **C16** §5.11 Hodge dictionary sentence — kept approachable wording
- optional §5.4 wedge-compatibility wording — kept as-is
- `mismatch`, `balance the books`, tiny-loop derivation, tiling/cancellation, Kelvin–Stokes naming, full $d(d\omega)$ calculation, general $k$-form formula, pullback commutation note, EM examples / Appendix C, Hodge foreshadow, Appendix B expansions, same-symbol $\rho$, EM current $J$ vs matrix $\mathbf{J}$

---

## Verification

Post-edit searches (expected: no matches):

- duplicate `---` blocks — none
- `Stokes's`, `guide rail`, `measuring device for measuring` — none
- `Write the components of $d\eta$ as $(d\eta)_{abc} = \partial_a \eta_{bc}` — none
- `factor of $\frac{1}{2}$ enters`, `converge to the trace`, `degenerates to a scalar coefficient` — none
- `\int_SJ` — none

`git diff --check` passes.
