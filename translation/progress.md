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
| `manuscript/ja/ch00/02_introduction.md` | roadmap aligned with `toc.md` (backport Wave 1) |

### Japanese backport — `translation/backport/`

| Wave | Branch | Items | Log |
|------|--------|-------|-----|
| **1** | #177 | BP-001, BP-002 |
| **2** | #178 | BP-013, BP-021 |
| **3** | `edit/ja-backport-wave3` | BP-022–023; BP-017 wontfix (author) | `backport-log.md`, `backport-rubric.md` |

---

## Workflow artifacts

| Path | Role |
|------|------|
| `translation/backport/backport-log.md` | JA reverse-import candidate tracker |
| `translation/backport/backport-rubric.md` | P0–P2 triage rules |
| `translation/style-guide.md` | English edition conventions |
| `translation/evaluation-rubric.md` | Pass 1 / 2 / 3 criteria |
| `translation/glossary.md` | Fixed term choices (e.g. curl not rot) |
| `translation/reviews/ch00-pass{1,2,3}.md` | ch00 pass logs |
| `translation/reviews/ch01-1.*-review.md` | ch01 per-section Pass 1 (+ notes) |
| `translation/reviews/ch01-pass2.md` | ch01 Pass 2 (staged §1.0–§1.6) |
| `translation/reviews/ch01-pass3.md` | ch01 Pass 3 decisions |
| `translation/reviews/ch01-close-reading-polish.md` | ch01 close-reading polish (#161) |
| `translation/reviews/ch03-3.*-review.md` | ch03 per-section Pass 1 |
| `translation/reviews/ch03-pass2.md` | ch03 Pass 2 |
| `translation/reviews/ch03-pass3.md` | ch03 Pass 3 |

---

## Follow-up (not blocking merge)

| Item | Action |
|------|--------|
| `translation/drafts/ch01-1.4.md` | Integrated into `ch01.md`; safe to delete after optional diff check |
| English ch01 in HTML/PDF build | Wire into build when English edition is published |
| Chapter 2+ translation | New issues; Pass 1 per section |

### English Chapter 2 — `manuscript/en/ch02/ch02.md` (branch `ai/english-translation-ch02`, PR [#165](https://github.com/yokiikoy/nabla-kaitai/pull/165))

| Scope | Pass | Notes |
|-------|------|-------|
| §2.0–§2.6 + Appendix A | **1 → 2 → 3** | `ch02-pass3.md`, `ch02-close-reading-polish.md` (#157, #172) |
| `translation/reviews/ch02-pass3.md` | complete | resolves #157 |
| `translation/reviews/ch02-close-reading-polish.md` | complete | #172 close-reading polish |
| §2.0 | 3 | bridge from ch01 |
| §2.1 | 3 | elementary vs 3D area |
| §2.2 | 3 | three rules, signed area |
| §2.3 | 3 | antisymmetric matrix / $2$-form |
| §2.4 | 3 | wedge product, projections |
| §2.5 | 3 | determinant / $3$-form |
| §2.6 | 3 | chapter summary |
| `translation/reviews/ch02-pass2.md` | complete | Pass 2 all stages |
| `translation/drafts/ch02-*.md` | integrated | optional cleanup after PR |

### English Chapter 3 — `manuscript/en/ch03/ch03.md` (branch `ai/english-translation-ch03`, PR [#162](https://github.com/yokiikoy/nabla-kaitai/pull/162))

| Scope | Pass | Notes |
|-------|------|-------|
| **Chapter 3 (§3.0–§3.5)** | **1 → 2 → 3** | `ch03-pass2.md`, `ch03-pass3.md` |

Per-section Pass status:

| Section | Pass | Section review |
|---------|------|----------------|
| §3.0 | **3** | `ch03-3.0-review.md` (#158) |
| §3.1 | **3** | `ch03-3.1-review.md` (#160) |
| §3.2 | **3** | `ch03-3.2-review.md` |
| §3.3 | **3** | `ch03-3.3-review.md` |
| §3.4 | **3** | `ch03-3.4-review.md` |
| §3.5 | **3** | `ch03-3.5-review.md` |

| Artifact | Status |
|----------|--------|
| `translation/drafts/ch03-3.*.md` | integrated into `ch03.md` |
| `translation/reviews/ch03-pass2.md` | complete |
| `translation/reviews/ch03-pass3.md` | complete |
| `translation/reviews/ch03-close-reading-polish.md` | complete (#181) |

### English Chapter 4 — `manuscript/en/ch04/ch04.md` (branch `ai/english-translation-ch04`, PR [#163](https://github.com/yokiikoy/nabla-kaitai/pull/163))

| Scope | Pass | Notes |
|-------|------|-------|
| **Chapter 4 (§4.0–§4.5)** | **1 → 2 → 3** | `ch04-pass2.md`, `ch04-pass3.md`; old YAML draft replaced |

Per-section Pass status:

| Section | Pass | Section review |
|---------|------|----------------|
| §4.0 | **3** | `ch04-4.0-review.md` |
| §4.1 | **3** | `ch04-4.1-review.md` |
| §4.2 | **3** | `ch04-4.2-review.md` |
| §4.3 | **3** | `ch04-4.3-review.md` |
| §4.4 | **3** | `ch04-4.4-review.md` |
| §4.5 | **3** | `ch04-4.5-review.md` |

| Artifact | Status |
|----------|--------|
| `translation/drafts/ch04-4.*.md` | integrated into `ch04.md` |
| `translation/reviews/ch04-pass2.md` | complete |
| `translation/reviews/ch04-pass3.md` | complete |
| `translation/reviews/ch04-close-reading-polish.md` | complete (#182) |

### English Chapter 5 — `manuscript/en/ch05/ch05.md` (branch `ai/english-translation-ch05`, PR [#166](https://github.com/yokiikoy/nabla-kaitai/pull/166))

| Scope | Pass | Notes |
|-------|------|-------|
| **Chapter 5 (§5.0–§5.11 + App. B–C)** | **1 → 2 → 3** | `ch05-pass2.md`, `ch05-pass3.md`; old YAML draft replaced |

| Section / appendix | Pass | Review |
|--------------------|------|--------|
| §5.0–§5.3 | **3** | `ch05-5.0-5.3-review.md` |
| §5.4–§5.6 | **3** | `ch05-5.4-5.6-review.md` |
| §5.7–§5.9 | **3** | `ch05-5.7-5.9-review.md` |
| §5.10–§5.11 | **3** | `ch05-5.10-5.11-review.md` |
| Appendices B–C | **3** | `ch05-appendix-BC-review.md` |

| Artifact | Status |
|----------|--------|
| `translation/drafts/ch05-*.md` | integrated into `ch05.md` |
| `translation/reviews/ch05-pass2.md` | complete |
| `translation/reviews/ch05-pass3.md` | complete |
| `translation/reviews/ch05-close-reading-polish.md` | complete (#183) |

### English Chapter 6 — `manuscript/en/ch06/ch06.md` (branch `ai/english-translation-ch06`, PR [#167](https://github.com/yokiikoy/nabla-kaitai/pull/167))

| Scope | Pass | Notes |
|-------|------|-------|
| **Chapter 6 (§6.0–§6.6 + App. D)** | **1 → 2 → 3** | `ch06-pass2.md`, `ch06-pass3.md`; old YAML draft replaced |

| Block | Pass | Review |
|-------|------|--------|
| §6.0–§6.2 | **3** | `ch06-6.0-6.2-review.md` |
| §6.3 | **3** | `ch06-6.3-review.md` |
| §6.4–§6.5 | **3** | `ch06-6.4-6.5-review.md` |
| §6.6 | **3** | `ch06-6.6-review.md` |
| Appendix D | **3** | `ch06-appendix-D-review.md` |

| Artifact | Status |
|----------|--------|
| `translation/drafts/ch06-*.md` | integrated into `ch06.md` |
| `translation/reviews/ch06-pass2.md` | complete |
| `translation/reviews/ch06-pass3.md` | complete |
| `translation/reviews/ch06-close-reading-polish.md` | complete (#184) |

### English Chapter 7 — `manuscript/en/ch07/ch07.md` (branch `ai/english-translation-ch07`, PR [#168](https://github.com/yokiikoy/nabla-kaitai/pull/168))

| Scope | Pass | Notes |
|-------|------|-------|
| **Chapter 7 (§7.0–§7.9)** | **1 → 2 → 3** | `ch07-pass2.md`, `ch07-pass3.md`; new file |

| Block | Pass | Review |
|-------|------|--------|
| §7.0–§7.2 | **3** | `ch07-7.0-7.2-review.md` |
| §7.3–§7.4 | **3** | `ch07-7.3-7.4-review.md` |
| §7.5–§7.7 | **3** | `ch07-7.5-7.7-review.md` |
| §7.8–§7.9 | **3** | `ch07-7.8-7.9-review.md` |

| Artifact | Status |
|----------|--------|
| `translation/drafts/ch07-*.md` | integrated into `ch07.md` |
| `translation/reviews/ch07-pass2.md` | complete |
| `translation/reviews/ch07-pass3.md` | complete |
| `translation/reviews/ch07-close-reading-polish.md` | complete (#185) |

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
