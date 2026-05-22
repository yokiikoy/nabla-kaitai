# Pass 3 Review: Chapter 2

Review date: 2026-05-22
Branch: `ai/english-translation-ch02`
File: `manuscript/en/ch02/ch02.md`
GitHub issue: #157

Pass 3 scope: authorial voice, note/aside handling, heading quality, publication polish.

Approach: same as Chapter 1 — keep distinctive voice; minimal consistency fixes only.

---

## Decisions

### 1. Chapter and section headings

Decision: **maintain** chapter title, all `### §2.x` headings, and Appendix A title as integrated.

Reason: Aligned with `manuscript/en/toc.md`; no genre mismatch like ch00 Preface/Greeting.

### 2. “Biased glasses” metaphor

Decision: **keep** throughout (§2.3, §2.4.6, checkpoints).

Reason: Book-specific metaphor parallel to ch01’s coordinate-rebuilding voice; flattening to “coordinate projection” would lose voice.

### 3. Authorial asides

Decision: **keep** “magic black box”, “handed down from on high by the author”, “slightly bad manners”, “Splendid —”, “That is everything!”

Reason: Pass 2–3 publication polish should not erase the physicist-textbook tone.

### 4. Signed-area and signed-volume Notes

Decision: **keep** full Notes in §2.2 and §2.5 (physicist orientation argument).

Reason: Pedagogically central; trimming would weaken the book’s vector-analysis bridge.

### 5. Cross product / scalar triple product Notes

Decision: **keep** wedge-first ordering and Hodge-dual deferral to Chapter 6.

Reason: Matches manuscript architecture; cross product named explicitly (not rot).

### 6. Appendix A

Decision: **keep** as chapter-end appendix in `ch02.md`; no separate file split.

Reason: Japanese source structure; referenced from §2.5.5.

### 7. Minor edits applied

| Location | Change | Reason |
|----------|--------|--------|
| §2.3 | Removed “In other words,” before biased-glasses sentence | Redundant connector after Pass 2 |
| §2.6 / Appendix A | Removed duplicate `---` | Same fix pattern as ch01 §2.3/§2.4 integration |

### 8. No change

- Elementary-school / tile intuition passages (intentional repetition with §2.1).
- Long tensor / $\widehat{\epsilon}$ Notes in §2.5.
- Hierarchy table in §2.5.10.

---

## Stage log

| Stage | Scope | Outcome |
|-------|--------|---------|
| 1 | §2.0–§2.2 | Recorded; no text change |
| 2 | §2.3–§2.4 | One connector trim; glasses metaphor kept |
| 3 | §2.5–§2.6 | Recorded; checkpoint wording kept |
| 4 | Appendix A | Duplicate rule fix only |
| 5 | Whole chapter | Terminology scan: no rot, no area meter, no YAML |

---

# Overall Chapter 2 Pass 3 Result

**Chapter 2 passes Pass 3** on `ai/english-translation-ch02`.

English Chapter 2 (`manuscript/en/ch02/ch02.md`, §2.0–§2.6 + Appendix A) is **Pass 1 + Pass 2 + Pass 3 complete**.

Next: optional draft cleanup; open PR from `ai/english-translation-ch02`; begin Chapter 3 Pass 1.
