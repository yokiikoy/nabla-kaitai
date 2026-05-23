# Close-Reading Polish: Chapter 11

Review date: 2026-05-22
Branch: `ai/english-translation-ch11`
File: `manuscript/en/ch11/ch11.md`
GitHub issue: #189
PR context: #173

Scope: publication polish after Pass 3 — typography, terminology consistency with earlier chapters, and safety clarifications around curvature and `\nabla`, while preserving the guidepost / outlook character.

---

## Applied

### A / B items

- None required (issue found no merge-blocking errors).

### C items

- **C1** `——` → `—` throughout Chapter 11
- **C2** `Stokes's theorem` → `Stokes' theorem` (§11.1.6, §11.1.7)
- **C3** §11.1.2: curve-equivalence definition — chart-independence phrasing
- **C4** §11.0: softened “without particular regard for the reader”
- **C5** §11.1.2: tangent-vector component transformation / inverse Jacobian clarified
- **C6** §11.2.3: constant-metric / flat case — coordinate-safe wording
- **C7** §11.2.3: `\nabla` as covariant derivative (vs Chapter 7 vector-analysis nabla)
- **C8** §11.3: “if only as a hobby”
- **C9** §11.3: `geometric algebra (Geometric Algebra)` → `geometric algebra`

### Intentionally unchanged (D items)

- Guidepost framing (§11.0), not a full manifold textbook
- Authorial notes (pretense/sincerity, easy chapter, unexpected consequence)
- Pointwise `g(p)` → per-point `*` dictionary; `g(x)` ≠ curvature
- Curved spacetime note; charts/atlas/tangent/cotangent/forms definitions
- Chapter 1 `dx=[1 0 0]` connection; pullback; `d` metric-free vs `*` metric-dependent
- §11.1.8 correspondence table; tensor-analysis style §11.2
- Christoffel / covariant derivative / curvature sketch; Ch9 div/curl bridge
- Bianchi identity caution; Einstein equation warning; two styles §11.2.4
- Geometric algebra closing (wording only simplified in C9)
- `curl` unchanged (not `rot`)

---

## Verification

Post-edit searches (expected: no matches):

- `——` — none
- `Stokes's` — none
- `constant matrix then all $\Gamma$ vanish` — none
- `connection $\nabla$ that first appears` — none
- `geometric algebra (Geometric Algebra)` — none
- `rot` — none

`git diff --check` passes.
