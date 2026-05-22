# Pass 3 Review: Chapter 1

Review date: 2026-05-22
Branch: `ai/english-translation-start`
File: `manuscript/en/ch01/ch01.md`
GitHub issue: #152

Pass 3 scope:

- Authorial voice
- Note and aside handling
- Title and heading quality
- Publication-level polish decisions

User direction: proceed with recommended decisions (collaborative sign-off).

---

## Decisions

### 1. §1.0 — maintain current text

Decision: **no substantive edits** to §1.0.

Reason:

- Section was already polished for rhythm in issue #147 and checked in Pass 2 stage 5.
- Signature voice (`But here, we are physicists.`, the “not a physicist” Note, `I still wrote it a little grandly…`) should stay.
- Three closing Notes (standpoint, Cartesian coordinates, Part III) each serve a distinct function; merging would save space at the cost of lookup clarity.

### 2. Chapter and section headings

Decision: **maintain** chapter title and all `### §1.x` headings as in `manuscript/en/toc.md`.

Reason:

- Headings are already natural English and aligned with the TOC.
- No ch00-style genre mismatch (unlike `Greeting` vs `Preface`).

### 3. Notational-contract repetition (§1.1.6, §1.2.2, §1.2.3, checkpoints)

Decision: **keep intentional repetition**; do not merge or shorten the “repetition is worth it” Note in §1.2.2.

Reason:

- Japanese source repeats the contract deliberately.
- Misreading $dx$ vs $\Delta x$ breaks the rest of the chapter; the safety net outweighs redundancy.

### 4. Advanced $dx=(1\ 0\ 0)$ Note (§1.1.3)

Decision: **keep full Note** (vector analysis / tensor / manifold blocks).

Reason:

- Serves advanced readers without moving core exposition; trimming would save length but remove a useful map to other literatures.

### 5. “Scale marks” (§1.4)

Decision: **keep** `scale marks` in both occurrences.

Reason:

- Distinctive book metaphor; replacing with bland “coordinate labels” would flatten authorial voice.

### 6. Terminology consistency — `physical space`

Decision: replace the lone **`real space`** in §1.2.3 with **`physical space`**.

Reason:

- Rest of Chapter 1 and Pass 2 use `physical space` / `parameter space`; one leftover “real space” was inconsistent, not an intentional variant.

### 7. §1.6 chapter checkpoint — “protagonist”

Decision: rephrase **“The protagonist of Chapter 1”** to **“Chapter 1 centers on”**.

Reason:

- “Protagonist” is slightly literary/translationese for an expository math book; meaning unchanged.

### 8. §1.3, §1.5, §1.6 body

Decision: **no further Pass 3 edits** beyond decision 7.

Reason:

- Pass 2 already addressed rhythm; additional rewriting risked voice drift.

---

## Stage log

| Stage | Scope | Outcome |
|-------|--------|---------|
| 1 | §1.0 | Recorded; no text change |
| 2 | §1.1–§1.2 | Recorded; repetition and advanced Note kept |
| 3 | §1.3 | Recorded; no text change |
| 4 | §1.4 | Recorded; scale marks kept |
| 5 | §1.5–§1.6 | Checkpoint wording fix (decision 7) |
| 6 | Whole chapter | `real space` → `physical space` (decision 6) |

---

## Files changed in Pass 3

- `manuscript/en/ch01/ch01.md` — two wording fixes (decisions 6–7)
- `translation/progress.md` — Pass 3 status
- `translation/reviews/ch01-pass3.md` — this file

---

# Overall Chapter 1 Pass 3 Result

**Chapter 1 passes Pass 3** on `ai/english-translation-start`.

English Chapter 1 (`manuscript/en/ch01/ch01.md`) is now **Pass 1 + Pass 2 + Pass 3 complete** for the translated body §1.0–§1.6.

Next recommended step:

- Optional: remove `translation/drafts/ch01-1.4.md` after diff check.
- Begin Chapter 2 translation (Pass 1 per section) or run HTML/PDF build smoke test for English ch01 if/when wired into the build.
