# Pass 2 Review: ch00

Review date: 2026-05-22
Branch: `ai/english-translation-start`

Pass 2 scope:

- English information structure
- English naturalness and rhythm
- Pedagogical flow

Pass 2 preserves the Pass 1 meaning and mathematical content while reducing translationese.

---

## `manuscript/en/ch00/01_preface.md`

### Main Changes

- Rewrote the opening from a passive, translation-like structure to a direct first-person sentence.
- Split long Japanese-style buildup into clearer English paragraph flow.
- Replaced `nose for “rigor”` with `a feel for “rigor”` for more natural English while preserving the metaphorical intent.
- Simplified several note sentences for rhythm.

### Representative Before / After

Before:

> This book was written as a book for answering the questions I myself had as an undergraduate.

After:

> I wrote this book to answer the questions I had as an undergraduate.

Before:

> In this book, however, notes have three roles.

After:

> Here, however, the notes have three jobs.

### Pass 2 Status

Passed.

Remaining Pass 3 issue: decide whether `Greeting` or `Preface` is better as an English-facing heading. `Greeting` is source-faithful to `ごあいさつ`; `Preface` may be more conventional.

---

## `manuscript/en/ch00/02_introduction.md`

### Main Changes

- Rewrote prerequisites for more natural English.
- Reorganized several paragraphs so the claim appears earlier.
- Replaced weaker structures such as `There is another symbol this book wants to take up` with stronger English topic sentences.
- Preserved the English-edition `del` / `nabla` explanation documented in Pass 1.
- Kept all equations unchanged.

### Representative Before / After

Before:

> There is another symbol this book wants to take up: $\nabla$.

After:

> The other symbol this book wants to confront is $\nabla$.

Before:

> Of course, from a more advanced mathematical point of view, my graduate-school friend’s explanation was overwhelmingly correct, and it is better if one can understand it that way. But it is hard.

After:

> From the more advanced mathematical point of view, my friend was overwhelmingly right. It is better if one can understand $dx$ that way. But it is hard.

### Pass 2 Status

Passed.

Remaining Pass 3 issue: polish voice around the midterm/final joke and decide whether `curl` should be accompanied by `rot` where the Japanese says `回転`.

---

## `manuscript/en/ch00/03_portal.md`

### Main Changes

- Slightly smoothed one awkward sentence about Discord and public social media.
- Kept URLs unchanged.

### Pass 2 Status

Passed.

Remaining Pass 3 issue: decide whether the English edition should eventually point to an English portal rather than `/jp/`.

---

# Overall ch00 Pass 2 Result

`ch00` passes Pass 2.

Current status:

- Source fidelity: preserved from Pass 1.
- Mathematical correctness: no changes introduced.
- English information structure: improved.
- English naturalness and rhythm: improved.
- Pedagogical flow: acceptable.

Next recommended step:

- Either run Pass 3 for ch00 to polish authorial voice and publication style, or begin translating Chapter 1 with the Pass 1 → Pass 2 workflow established here.
