# Close-Reading Polish: Chapter 2

Review date: 2026-05-22  
Branch: `ai/english-translation-ch02`  
File: `manuscript/en/ch02/ch02.md`  
GitHub issue: #172  
PR context: #165

Scope: publication polish after Pass 3 — mathematical safety (positive volume / $3$-form components), English naturalness, Markdown maintainability.

---

## Applied

### B items

- **B1** §2.4.4: outer product explanation for $dx \otimes dy$ matrix representation
- **B2** §2.4.9: removed duplicate horizontal rule before §2.5
- **B3** §2.5 opening: positive volume wording (one independent component in 3D)
- **B4** §2.5.5: Appendix A reference sentence rewritten
- **B5** fragmented `<strong>` around inline math cleaned (§2.1–Appendix A)

### C items (C1–C53)

- Wording, grammar, and markup polish across §2.0–Appendix A per issue #172

### Intentionally unchanged (D items)

- matrix vs form simplified language
- `biased glasses`, `magic black box`, `Weapons Gained`
- `elementary-school area/volume` motif (with C42/C43 safety edits)
- `0-form measures a point` metaphor (C27 safety edit applied)
- `epsilon_{ijk}` with $(x,y,z)$ indexing
- `collapse index` pedagogy

### Appendix A

- Intermediate $v_2^T M$ calculation checked; signs correct; no formula changes.

---

## Verification

- Post-edit searches: no `front vector`, `rear row`, `quadratic form above`, duplicate `---`, `elementary-school area ${=}$`
- `git diff --check` passes
