# Close-Reading Polish: Chapter 6

Review date: 2026-05-22
Branch: `ai/english-translation-ch06`
File: `manuscript/en/ch06/ch06.md`
GitHub issue: #184
PR context: #167

Scope: publication polish after Pass 3 — inner-product grammar, Route ①/② consistency, Hodge-star array safety, Markdown cleanup, preservation of $g$ / $\ast$ discovery arc.

---

## Applied

### B items

- **B1** §6.1.1: inner-product definition grammar
- **B2** Removed duplicate horizontal rules between §6.2/§6.3 and §6.6/Appendix D
- **B3** Normalized `Method ①/②` → `Route ①/②` throughout Chapter 6 (§6.3–checkpoint)

### C items (straightforward)

- **C2** §6.0: `……` → `...`
- **C3** §6.1: spherical $\mathbf{g}$ — `with $\theta$ taken as the polar angle`
- **C4** §6.2.2: $k=0$ size sentence
- **C6** §6.3: metric-induced inner product of forms
- **C7** §6.4.1: Route ② display clarification for $E\cdot J$
- **C8** §6.4.1: `Route ② display of $J$`
- **C10** §6.6: `Gauss' theorem` (matches Chapter 5)
- **C12** Appendix D.2: $A\cdot B$ vs $\operatorname{tr}(A^T B)$ factor convention
- **C13** Appendix D.3: row-vector display for $\ast_{2\to1}(\ast_{1\to2}(\omega))$
- **C14** Appendix D.4: $\eta_{ijk}$ as components, not $\eta=\eta_{ijk}$

### Intentionally unchanged (D items / optional C)

- **C1** §6.0 opening long sentence — preserved rhythm
- **C5** §6.3 `same kind of arrow` — preserved authorial phrase
- **C9** §6.5 divergence input reminder — defer language sufficient
- **C11** §6.6 relativity aside — kept light
- **C16** §6.11 Hodge dictionary sentence — kept approachable wording
- “The End of Excuses”, row/column insistence, Chapter 2 smuggled note, arc-length avoidance, Route framing, Hodge basis dictionary, $\ast\ast=\mathrm{id}$, Joule/helicity examples, `grad=d` / `curl=*d` / `div=*d*`, nabla defer, relativity aside, Appendix D expansions, $\widehat{\epsilon}$ / $E_k$, normalized Frobenius $1/2$, $1/3!$ normalization

---

## Verification

Post-edit searches (expected: no matches):

- duplicate `---` blocks — none
- `Method ①`, `Method ②` — none
- `rot` — none
- `Gauss' divergence theorem` — none
- `\eta = \eta_{ijk}` display — none
- `Because it is equivalent to $\frac{1}{2}\sum` — none
- old inner-product definition fragment — none

`git diff --check` passes.
