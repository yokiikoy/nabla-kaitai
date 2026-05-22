# Translation Progress

Branch: `ai/english-translation-start` · PR [#153](https://github.com/yokiikoy/nabla-kaitai/pull/153)

---

## Current status (authoritative)

### English front matter — ch00

| File | Pass | Notes |
|------|------|-------|
| `manuscript/en/ch00/01_preface.md` | **3** | Heading: Preface; see `ch00-pass3.md` |
| `manuscript/en/ch00/02_introduction.md` | **3** | del/nabla; roadmap aligned with Japanese |
| `manuscript/en/ch00/03_portal.md` | **3** | English portal URL |

### English Chapter 1 — `manuscript/en/ch01/ch01.md`

| Scope | Pass | Review record |
|-------|------|----------------|
| **Chapter 1 (§1.0–§1.6)** | **1 → 2 → 3** | `ch01-pass2.md`, `ch01-pass3.md`, `ch01-close-reading-polish.md` (#161, closed) |

Per-section Pass status (all included in chapter-wide Pass 2 and Pass 3):

| Section | Pass | Section review |
|---------|------|----------------|
| §1.0 | **3** | `ch01-1.0-review.md` (#147) |
| §1.1 | **3** | `ch01-1.1-review.md` |
| §1.2 | **3** | `ch01-1.2-review.md` |
| §1.3 | **3** | `ch01-1.3-review.md` |
| §1.4 | **3** | `ch01-1.4-review.md` (#148) |
| §1.5 | **3** | `ch01-1.5-review.md` (#149) |
| §1.6 | **3** | `ch01-1.6-review.md` (#150) |

### Supporting English files

| File | Status |
|------|--------|
| `manuscript/en/toc.md` | draft (Preface, curl normalized) |
| `manuscript/en/README.md` | boilerplate |

### Japanese files touched for alignment

| File | Status |
|------|--------|
| `manuscript/ja/toc.md` | updated from current chapter headings |
| `manuscript/ja/ch00/02_introduction.md` | roadmap aligned with current structure |

---

## Workflow artifacts

| Path | Role |
|------|------|
| `translation/style-guide.md` | English edition conventions |
| `translation/evaluation-rubric.md` | Pass 1 / 2 / 3 criteria |
| `translation/glossary.md` | Fixed term choices (e.g. curl not rot) |
| `translation/reviews/ch00-pass{1,2,3}.md` | ch00 pass logs |
| `translation/reviews/ch01-1.*-review.md` | ch01 per-section Pass 1 (+ notes) |
| `translation/reviews/ch01-pass2.md` | ch01 Pass 2 (staged §1.0–§1.6) |
| `translation/reviews/ch01-pass3.md` | ch01 Pass 3 decisions |
| `translation/reviews/ch01-close-reading-polish.md` | ch01 close-reading polish (#161) |

---

## Follow-up (not blocking merge)

| Item | Action |
|------|--------|
| `translation/drafts/ch01-1.4.md` | Integrated into `ch01.md`; safe to delete after optional diff check |
| English ch01 in HTML/PDF build | Wire into build when English edition is published |
| Chapter 2+ translation | New issues; Pass 1 per section |

### English Chapter 2 — `manuscript/en/ch02/ch02.md` (branch `ai/english-translation-ch02`, PR [#159](https://github.com/yokiikoy/nabla-kaitai/pull/159))

| Scope | Pass | Notes |
|-------|------|-------|
| §2.0–§2.6 + Appendix A | **1 → 2 → 3** | `ch02-pass3.md`; issue #157; English ch02 body complete |
| `translation/reviews/ch02-pass3.md` | complete | resolves #157 |
| §2.0 | 3 | bridge from ch01 |
| §2.1 | 3 | elementary vs 3D area |
| §2.2 | 3 | three rules, signed area |
| §2.3 | 3 | antisymmetric matrix / $2$-form |
| §2.4 | 3 | wedge product, projections |
| §2.5 | 3 | determinant / $3$-form |
| §2.6 | 3 | chapter summary |
| `translation/reviews/ch02-pass2.md` | complete | Pass 2 all stages |
| `translation/drafts/ch02-*.md` | integrated | optional cleanup after PR |

---

## History (closed issues on this branch)

| Issue | Work |
|-------|------|
| #138–#145, #147 | ch00 rhythm / structure |
| #146 | Replace outdated English ch01; restart §1.0 workflow |
| #148 | Integrate §1.4 into `ch01.md` |
| #149 | Translate §1.5 |
| #150 | Translate §1.6 |
| #151 | Chapter 1 Pass 2 |
| #152 | Chapter 1 Pass 3 |
| #161 | Chapter 1 close-reading polish (closed) |
