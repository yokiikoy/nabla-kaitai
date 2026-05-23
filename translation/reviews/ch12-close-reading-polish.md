# Close-Reading Polish: Chapter 12

Review date: 2026-05-22
Branch: `ai/english-translation-ch12`
File: `manuscript/en/ch12/ch12.md`
GitHub issue: #190
PR context: #174

Scope: publication polish after Pass 3 — typography, `\varepsilon_0` consistency, wedge/cross and `d`/1-form safety, Markdown cleanup, preservation of final-chapter arc.

---

## Applied

### A / B items

- None required (issue found no merge-blocking errors).

### C items

- **C1** `——` → `—` throughout Chapter 12
- **C2/C5** `\epsilon_0` → `\varepsilon_0` in Maxwell source-term prose (matches display)
- **C3** §12.2.2: wedge/cross identification — 3D orientation convention safety wording
- **C4** §12.3.1: `d\mathbf A` → applying `d` to corresponding 1-form
- **C7** Blank line after `---` before §12.3
- **C8** Removed trailing horizontal rule at file end (book ends on `\nabla`)
- **C9** Quaternion note: Maxwell used quaternionic language
- **C10** Matrix-algebra history note softened to physicists' working language

### Build verification (C6)

- `\cancel{\partial}` is supported: `tools/build_pdf.py` preamble includes `\usepackage{cancel}`.

### Intentionally unchanged (D items)

- Advanced supplement framing (§12.0)
- `F+i\ast F` trick and 4D limitation (§12.1)
- “Magic box” framing; Pauli multiplication table
- Symmetric/antisymmetric decomposition; Pauli identity `VW = (\mathbf v\!\cdot\!\mathbf w)I+i(\mathbf v\times\mathbf w)\!\cdot\!\bm\sigma`
- All-degree matching note (`I`, `\sigma_i`, `i\sigma_i`, `iI`)
- `D=\bm\sigma\cdot\nabla`; full `DA` expansion; `D\sim d+\delta`; `D^2=\nabla^2I`
- Riemann–Silberstein vector; Maxwell one-liner; `\cancel\partial F=J`
- Product-not-ordinary-matrix-multiplication note; Doran & Lasenby reference
- Final book-end return to `\nabla`
- `curl` unchanged (not `rot`)

---

## Verification

Post-edit searches (expected: no matches except intentional section `---`):

- `——` — none
- `\epsilon_0` — none
- `d\mathbf{A}` — none
- trailing `---` at EOF — none
- `---\n###` without blank line before §12.3 — fixed
- `rot` — none

`git diff --check` passes.
