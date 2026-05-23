# Close-Reading Polish: Back Matter

Review date: 2026-05-23
Branch: `ai/english-translation-backmatter`
Files: `manuscript/en/appendix.md`, `afterword.md`, `references.md`
GitHub issue: #191
PR context: #175

Scope: publication polish after Pass 3 — reference fixes, chapter-structure consistency, typography, light wording safety, preservation of FAQ tone and authorial narrative.

---

## Applied

### B items

- **B1** `appendix.md`: `Chapter 5 §8.8` → `Chapter 5 §5.8` ($d^2=0$)
- **B2** `references.md`: Burke comment updated to delayed metric/Hodge star in Chapter 6
- **B3** `references.md`: Susskind/Friedman — "lay column vectors on their sides as row vectors"

### C items

- **C1** `——` → `—` across appendix, afterword, references
- **C2** Appendix: universal-property claim → "more standard abstract viewpoint is signposted in Chapter 11"
- **C3** Appendix: "most concrete practice" → "concrete entry point toward the axiomatic approach"
- **C4** Appendix: connection wording conditional ("When connections are mentioned...")
- **C5** Afterword: "derived in a discovery-style way"
- **C6** Afterword: "uncommon in the Western books I have seen"
- **C7** Afterword: East Asian entrance-exam remark made self-including
- **C8** Afterword: "gone through serious entrance-exam mathematics"
- **C9** Chapter 1–5 / Chapter 6 metric references verified — no change needed

### Intentionally unchanged (D items)

- Appendix FAQ tone, anger/compensation/gatekeeping notes, scope defense
- `dx` as row vector defense; `d` vs covariant `\nabla` separation
- Chapter 10 sign/normalization defense; Bourbaki Easter egg
- Afterword Dirac/Burke/LLM narrative; dual vs inner product distinction
- "This is not an inner product" / "metric should come later"
- Coordinate change as demon gate; no mathematical novelty claim
- Algebraic hands / entrance-exam note; LLM responsibility disclaimer
- Six references and author-comment style; Doran & Lasenby closing role
- `curl` unchanged (not `rot`)

---

## Verification

Post-edit searches (expected: no matches):

- `——` — none
- `Chapter 5 §8.8` — none
- `through Chapter 5 of this book` — none
- `lay row vectors on their sides` — none
- `Definition via universal properties is introduced in Chapter 11` — none
- `connections are implicitly always` — none
- `discovery-style derived` — none
- `East Asian students are oddly trained` — none
- `passed entrance-exam mathematics` — none
- `rot` — none

`git diff --check` passes.
