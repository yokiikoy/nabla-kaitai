# Close-Reading Polish: Chapter 7

Review date: 2026-05-23
Branch: `ai/english-translation-ch07`
File: `manuscript/en/ch07/ch07.md`
GitHub issue: #185
PR context: #168

Scope: publication polish after Pass 3 — cross-product terminology, Markdown cleanup, row-column safety, Gauss terminology alignment with Chapters 5–6, Chapter 8 bridge clarity, preservation of vector-analysis discomfort arc.

---

## Applied

### B items

- **B1** §7.1.2: removed `(outer product)` gloss from cross-product definition
- **B2** Removed duplicate horizontal rules between §7.2/§7.3, §7.4/§7.5, and §7.7/§7.8

### C items (straightforward)

- **C1** §7.1.1: dot product / row-column distinction — inner product from Chapter 6
- **C2** §7.3: divergence as operation $\nabla\cdot\mathbf F$
- **C3** §7.4: curl as operation $\nabla\times\mathbf F$
- **C4** §7.7: smoothness premise for product rules
- **C5** §7.6.2: Maxwell $\nabla\cdot\mathbf B=0$ / magnetic monopole sentence
- **C6** §7.7: formula-list note grammar (`typical of the ones`)
- **C7** §7.8: `Gauss' divergence theorem` → `Gauss' theorem` (matches Chapters 5–6)
- **C8** §7.8: Green's theorem — positive orientation on $\partial D$
- **C9** §7.8.3: common-structure sentence (curl/div, not grad list)
- **C10** §7.9: Chapter 8 bridge — explicit $1$-form $\omega$ for $\mathbf F$
- **C11** Final checkpoint: cross-product matrix wording

### Intentionally unchanged (D items / optional C)

- **C12** §7.0 title joke / nabla entry framing
- **C13** §7.7 `dirty and unnatural` note
- Chapter 6 preview → standard vector analysis transition
- Cross-product matrix and Chapter 2 / Chapter 6 back-links
- Chapter 6 back-links for div/curl ($\ast d\ast$, $\ast d$)
- Trace reading of divergence, BAC-CAB, physical examples
- Formula collection, “bundle of three-component arrows” theme
- “Just between us” note, standard theorem statements
- Chapter 5 unified Stokes recall, §7.9 measuring-devices transition

---

## Verification

Post-edit searches (expected: no matches):

- duplicate `---` blocks — none
- `outer product` — none
- `Gauss' divergence theorem` — none
- `typical of those students are forced to memorize` — none
- `Because Stokes and Gauss use different operators—grad, curl, and div` — none
- `exterior-product matrix representation` — none
- `rot` (as curl synonym) — none

`git diff --check` passes.
