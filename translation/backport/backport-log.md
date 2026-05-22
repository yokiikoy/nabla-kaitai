# Backport Log

Branch series: `edit/ja-backport-wave*` · Japanese primary (`manuscript/ja/`)

Legend: `pending` | `done` | `wontfix` | `P2-hold` | `out-of-scope`

---

## Wave 1 — PR [#177](https://github.com/yokiikoy/nabla-kaitai/pull/177)

| ID | Pri | File | Issue | Source | Status |
|----|-----|------|-------|--------|--------|
| BP-001 | P0 | `ch12/ch12.md` §12.3.3 | Charge density $\rho$ → $\rho_{\mathrm e}$; $\epsilon_0$ → $\varepsilon_0$ | EN ch12-pass2 | done |
| BP-002 | P1 | `ch00/02_introduction.md` | Roadmap Part I/II 1–4 / 5–9 vs `toc.md`; rot not curl | EN ch00-pass3 | done |
| BP-003 | — | `ch03_note.md` | Metric chapter refs | ja grep | **out-of-scope** (file deprecated) |
| BP-004 | Skip | `ch11/ch11.md` | EN rot→curl; JA keeps rot | style-guide | wontfix |
| BP-005 | Skip | all | English Pass 2 voice | reviews | wontfix |

---

## Wave 2 — PR (this branch, base wave1)

| ID | Pri | File | Issue | Source | Status |
|----|-----|------|-------|--------|--------|
| BP-010 | P1 | `ch02/ch02.md` | Duplicate `---` at §2.4/§2.5 | ch02-pass2 | wontfix (checkpoint framing; no bare `---\n\n---`) |
| BP-011 | P1 | `ch01/ch01.md` | Checkpoint `---` blocks | ch02-pass3 | wontfix (intentional) |
| BP-012 | P2 | `appendix.md` | New FAQ from EN | backmatter | wontfix (EN translated JA; no new item) |
| BP-013 | P1 | `ch05/ch05.md` §5.10.2 + App.C | Forward ref $\rho_{\mathrm e}$ vs radial $\rho$ | ch09/ch10 convention | done |
| BP-014 | P1 | `ch09/ch09.md` | Loop closed via BP-001 | ch09 §9.5 | done |
| BP-015 | P2 | `afterword.md` | LLM paragraph polish | EN afterword | wontfix (JA already complete) |
| BP-016 | P1 | `references.md` | Burke「第5章まで」| triage | wontfix (metric delay; correct) |
| BP-017 | P2 | `ch04/ch04.md` | $W_{\text{実/素朴}}$ rename | ch04-pass2 | P2-hold |
| BP-018 | P1 | `ch00/02_introduction.md` | Narrative line 65 | — | done (BP-002) |
| BP-019 | P1 | `ch10/ch10.md` | $\rho_{\mathrm e}$ consistent | grep | wontfix |
| BP-020 | P2 | `ch06/ch06.md` | App.D clarity | ch06 reviews | pending (Wave 3) |
| BP-021 | P1 | `en/ch00/02_introduction.md` | Mirror BP-002 roadmap ranges | factual sync | done |

---

## Review mining notes (Pass 2/3)

- **ch01-pass2**: typo fixes English-only; JA unchanged.
- **ch01-pass3**: `real space` → `physical space` — JA uses 実空間 consistently.
- **ch05-pass2**: `Stokes's` → `Stokes'` — N/A for Japanese.
- **ch10-pass2**: $\rho_{\mathrm e}$ already in JA ch10.
- **backmatter-pass2**: old EN afterword ch5 metric error; JA afterword correct (ch6).

---

## Completion

| Wave | PR | Status |
|------|-----|--------|
| 1 | #177 | open |
| 2 | (this branch) | in progress |

## Wave 3 candidates

- BP-020: ch06 Appendix D cross-read
- BP-017: ch04 subscript rename (author decision)
- Full JA/EN roadmap audit after translation stack merges
