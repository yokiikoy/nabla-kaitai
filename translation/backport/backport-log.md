# Backport Log

Branch series: `edit/ja-backport-wave*` · Japanese primary (`manuscript/ja/`)

Legend: `pending` | `done` | `wontfix` | `P2-hold`

---

## Wave 1 (this PR)

| ID | Pri | File | Issue | Source | Status |
|----|-----|------|-------|--------|--------|
| BP-001 | P0 | `ch12/ch12.md` §12.3.3 | Charge density $\rho$ → $\rho_{\mathrm e}$; $\epsilon_0$ → $\varepsilon_0$ (align ch10, ch9 Note) | EN ch12-pass2; ja grep | done |
| BP-002 | P1 | `ch00/02_introduction.md` | Roadmap Part I/II chapter ranges wrong vs `toc.md`; restore rot not curl | EN ch00-pass3; toc diff | done |
| BP-003 | P1 | `ch03_note.md` | Says metric introduced in ch5; should be ch6 (×4 lines) | ja grep | pending (not in PDF build) |
| BP-004 | Skip | `ch11/ch11.md` §11.2.2 | EN changed rot→curl; JA keeps rot | style-guide | wontfix |
| BP-005 | Skip | all | English Pass 2 voice/connectors | reviews | wontfix |

---

## Mined — Wave 2 candidates

| ID | Pri | File | Issue | Source | Status |
|----|-----|------|-------|--------|--------|
| BP-010 | P1 | `ch02/ch02.md` | Check duplicate `---` at §2.4/§2.5 boundary (EN fixed) | ch02-pass2 | pending |
| BP-011 | P1 | `ch01/ch01.md` | Checkpoint blocks sandwiched by `---` (may be intentional) | ch02-pass3 pattern | pending |
| BP-012 | P2 | `appendix.md` | Add FAQ item if EN appendix surfaced new reader objection | backmatter | pending |
| BP-013 | P0 | `ch05/ch05.md` App.C | $\rho$ for charge density in Maxwell localization — check vs $\rho_{\mathrm e}$ convention | ch10 cross-ref | pending |
| BP-014 | P1 | `ch09/ch09.md` | Already warns $\rho$ vs $\rho_{\mathrm e}$ — verify ch12 fix closes loop | ch09 §9.5 Note | done (via BP-001) |
| BP-015 | P2 | `afterword.md` | LLM paragraph: optional JA polish after EN backmatter translation | EN afterword | pending |
| BP-016 | P1 | `references.md` | Burke comment「第5章まで」= metric delay (correct); do not change to ch6 | triage | wontfix |
| BP-017 | P2 | `ch04/ch04.md` | $W_{\text{実/素朴}}$ — consider renaming for consistency with EN $W_{\text{phys/naive}}$ | ch04-pass2 | P2-hold |
| BP-018 | P1 | `ch00/02_introduction.md` | Narrative line 65 lists 外微分 before ナブラ — OK; roadmap was main fix | — | done (BP-002) |
| BP-019 | P1 | `ch10/ch10.md` | $\rho_{\mathrm e}$ already consistent — no change | grep | wontfix |
| BP-020 | P2 | `ch06/ch06.md` | Cross-read with EN App.D for array notation clarity | ch06 reviews | pending |

---

## Review mining notes (Pass 2/3)

- **ch01-pass2**: typo class fixes were English-only; JA source had no equivalent typo found.
- **ch01-pass3**: `real space` → `physical space` — JA uses 実空間 consistently; no change.
- **ch05-pass2**: `Stokes's` → `Stokes'` — N/A for Japanese.
- **ch06-pass2**: wrong YAML draft replaced — N/A for JA.
- **ch10-pass2**: $\rho_{\mathrm e}$ already in JA ch10.
- **backmatter-pass2**: old EN afterword had ch5 metric error; JA afterword correctly says ch6.

---

## Completion

| Wave | PR | Status |
|------|-----|--------|
| 1 | (this branch) | in progress |
| 2 | — | not started |
