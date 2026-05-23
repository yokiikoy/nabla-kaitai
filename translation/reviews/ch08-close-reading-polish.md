# Close-Reading Polish: Chapter 8

Review date: 2026-05-23
Branch: `ai/english-translation-ch08`
File: `manuscript/en/ch08/ch08.md`
GitHub issue: #186
PR context: #169

Scope: publication polish after Pass 3 — Route ①/② consistency with Chapter 6, Markdown cleanup, $d$ vs $\nabla$ safety, Gauss terminology alignment, preservation of highlight / translation-dictionary arc.

---

## Applied

### B items

- **B1** Removed duplicate horizontal rules between §8.1/§8.2, §8.3/§8.4, and §8.5/§8.6
- **B2** Normalized named `Method ①/②` → `Route ①/②` throughout Chapter 8 (§8.5–§8.6)
- **B3** §8.1.1: `$d$ does not produce a new arrow field…` (replacing “field stays as it is”)

### C items (straightforward)

- **C1** §8.1.1: `$d$` differentiates coefficients and produces the next measuring device
- **C2** §8.2.2: metric read-back $g^{-1}(\ast d\omega)^T$ for curl comparison
- **C3** §8.2.4: `dirtier` → `messy` (consistent with checkpoint)
- **C4** §8.3.1: `Start with Stokes' theorem…`
- **C5** §8.4: `Gauss' theorem` (matches Chapters 5–7)
- **C6** §8.4: scalar-to-3-form step clarified for Gauss translation
- **C8** §8.5.1: measuring-device degree wording
- **C9** §8.5.2: “One changes the measuring-device side…”
- **C10** §8.5.2: metric identification note after $\int_C df = \int_C \nabla f\cdot d\mathbf r$
- **C11** §8.5.2: `guarantees` → softer agreement wording
- **C12** §8.6 heading: `Two Routes`
- **C13** §8.6: 3D cylindrical → 2D polar transition sentence
- **C14** §8.6.2: `$d$` vs metric factors division of labor
- **C15** §8.6.2: Route ① subtitle (pullback / form side)

### Intentionally unchanged (D items / optional C)

- **C7** §8.3.2 “public line for the reader” — preserved authorial voice
- §8.0 highlight framing, two-worldview structure, full dictionary table
- $\omega=\mathbf F^T g$, Stokes via $\ast(\ast d\omega)=d\omega$, Gauss via $\eta=\ast\omega$
- Three Theorems One Formula, “Neither is superior”, polar walkthrough
- Orthonormal vs form-coefficient note, cylindrical results, Chapter 9 foreshadow

---

## Verification

Post-edit searches (expected: no matches):

- duplicate `---` blocks — none
- `Method ①`, `Method ②`, `Methods ①` — none
- `the field stays as it is` — none
- `Gauss' divergence theorem` — none
- `Take the Stokes' theorem` — none
- `what kind of measuring device is being measured` — none
- `replaces measuring devices` — none
- `insert factors such as $\frac{1}{r}$` — none
- `rot` (as curl synonym) — none

`git diff --check` passes.
