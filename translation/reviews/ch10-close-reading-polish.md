# Close-Reading Polish: Chapter 10

Review date: 2026-05-23
Branch: `ai/english-translation-ch10`
File: `manuscript/en/ch10/ch10.md`
GitHub issue: #188
PR context: #171

Scope: publication polish after Pass 3 — explicit metric notation in §10.5, Markdown cleanup, English smoothing, preservation of component-expansion / “beyond beauty” arc.

---

## Applied

### B items

- **B1** Removed duplicate horizontal rule between §10.2/§10.3; added blank line before §10.6 heading
- **B2** §10.5: replaced `\ast_3B` / `\ast_3E` shorthand with `\mathbf B^Tg_3` and `\ast_3(\mathbf E^Tg_3)`; added optional `\flat` notation note; updated `d_4(\ast_4F)` comparison formulas

### C items (straightforward)

- **C1/C2** §10.0 comma splice; `——` → `—` in §10.0/§10.1
- **C3** §10.1: length-dimension / magnetic-field rescaling wording
- **C4** §10.1: aligned time/space derivative wording with coordinate $w$
- **C5** §10.5: “Reading these forms back through the Chapter 8 spatial dictionary…”
- **C6** §10.6: gauge freedom component sign note
- **C7** §10.6: `\mathrm{div}\,\mathrm{curl}\equiv0` wording
- **C8** Appendix F.4: $B$ as spatial magnetic $2$-form clarification
- **C9** §10.6: normalized potential units note
- **C10** §10.5: `\ast_3(\rho_{\mathrm e}/\varepsilon_0)` as charge-density $3$-form

### Intentionally unchanged (D items / optional C)

- §10.0 caveat / not an EM textbook framing
- $w=ct$, $B'=cB$, rename-back convention
- $d_4,\ast_4$ vs $d_3,\ast_3$ split
- $F$ sign conventions, Minkowski metric, full §10.4–§10.5 expansions
- RHS current $3$-form, Chapter 12 foreshadow, “gritty computation”
- $F=-d\mathcal{A}$, component $d\mathcal{A}$ expansion
- Appendix E slice matrices, Appendix F Chapter 5/10 split, Hehl–Obukhov note
- Appendix F.4 retains `\ast_3B=B_x\,dx+\cdots` with $2$-form $B$ clarified

---

## Verification

Post-edit searches (expected: no matches in main-text §10.5):

- duplicate `---` blocks — none
- `——` — none
- `convert everything to the dimension of "length"` — none
- `\ast_3B=B_x\,dx+B_y\,dy+B_z\,dz` in §10.5 main text — none (remains in Appendix F.4)
- `dt\wedge(\ast_3B)+\ast_3E` in §10.5 main text — none (remains in Appendix F.4)
- `Applying $\ast_3$ to both sides as needed` — none
- `That $\mathrm{div}\,\mathrm{curl}\equiv0$` — none
- `B^\flat` / `E^\flat` / `^\sharp` as main notation — none ( `\mathbf B^\flat` only in explanatory note)
- `rot` — none

`git diff --check` passes.
