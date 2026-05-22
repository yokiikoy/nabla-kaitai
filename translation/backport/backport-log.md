# Backport Log

Branch series: `edit/ja-backport-wave*` · Japanese primary (`manuscript/ja/`)

Legend: `pending` | `done` | `wontfix` | `P2-hold` | `out-of-scope`

---

## Wave 1 — PR [#177](https://github.com/yokiikoy/nabla-kaitai/pull/177)

| ID | Pri | File | Issue | Source | Status |
|----|-----|------|-------|--------|--------|
| BP-001 | P0 | `ch12/ch12.md` §12.3.3 | $\rho_{\mathrm e}$, $\varepsilon_0$ | EN ch12-pass2 | done |
| BP-002 | P1 | `ch00/02_introduction.md` | Roadmap 1–4 / 5–9 | toc.md | done |
| BP-003 | — | `ch03_note.md` | Deprecated note draft | author | done (deleted; see BP-022) |
| BP-004 | Skip | `ch11/ch11.md` | rot vs curl | style-guide | wontfix |
| BP-005 | Skip | all | EN Pass 2 voice | reviews | wontfix |

---

## Wave 2 — PR [#178](https://github.com/yokiikoy/nabla-kaitai/pull/178)

| ID | Pri | File | Issue | Status |
|----|-----|------|-------|--------|
| BP-010–011 | P1 | ch01/ch02 | `---` checkpoints | wontfix (intentional) |
| BP-012–015 | P2 | appendix/afterword | EN-only | wontfix |
| BP-013 | P1 | `ch05/ch05.md` | $\rho_{\mathrm e}$ forward ref | done |
| BP-016, BP-019 | P1 | refs/ch10 | triage | wontfix |
| BP-017 | P2 | `ch04/ch04.md` | $W_{\text{実/素朴}}$ | **wontfix** (author: keep JA) |
| BP-021 | P1 | `en/ch00/02_introduction.md` | roadmap mirror | done |

---

## Wave 3 — PR (this branch, base wave2)

| ID | Pri | File | Issue | Status |
|----|-----|------|-------|--------|
| BP-020 | P2 | `ch06/ch06.md` App.D | Cross-read clarity | wontfix (付録A ref already at D.1 Note) |
| BP-022 | P1 | `ch01–04_*_note.md` | Remove unused note drafts | done (author approved all) |
| BP-023 | P1 | `ch03/ch03.md` §3.4.3 | $\rho_{\mathrm e}$ forward ref | done |

---

## Completion

| Wave | PR | Status |
|------|-----|--------|
| 1 | #177 | open |
| 2 | #178 | open |
| 3 | (this branch) | ready |

## Wave 4 candidates

- Full JA/EN roadmap audit after translation stack merges to `main`
- Optional: grep pass after #175 backmatter merge
