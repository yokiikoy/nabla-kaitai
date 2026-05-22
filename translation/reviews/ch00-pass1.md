# Pass 1 Review: ch00

Review date: 2026-05-22
Branch: `ai/english-translation-start`

Pass 1 scope:

- Source fidelity
- Mathematical correctness
- Terminology consistency
- Markdown and build compatibility

Pass 1 does **not** attempt to polish English information structure or publication-level rhythm. Those belong to Pass 2 and Pass 3.

---

## `manuscript/en/ch00/01_preface.md`

### Scores

| Item | Score | Notes |
|---|---:|---|
| Source Fidelity | 4 | No major omissions. Japanese title says `ごあいさつ`; heading was changed from `Preface` to `Greeting` to match current TOC. |
| Mathematical Correctness | 5 | No mathematical content requiring correction. |
| Terminology Consistency | 4 | `Note` / `Remark` use follows style guide. `nose for rigor` is acceptable for `厳密さへの嗅覚`, but may need Pass 2 polishing. |
| Markdown and Build Compatibility | 4 | Markdown structure is valid. No YAML front matter yet; this may need a project-level decision. |

### Required Revisions Made

- Changed heading from `# Preface: ...` to `# Greeting: ...` to match the current Japanese heading and updated TOC.

### Remaining Pass 2 Issues

- Opening sentence is faithful but translation-like: `This book was written as a book for answering...`.
- Consider rewriting in Pass 2 as: `I wrote this book to answer the questions I had as an undergraduate.`
- The phrase `nose for “rigor”` preserves the metaphor, but may need rhythm adjustment.

### Pass 1 Status

Passed with minor notes.

---

## `manuscript/en/ch00/02_introduction.md`

### Scores

| Item | Score | Notes |
|---|---:|---|
| Source Fidelity | 4 | Main content preserved. One English-only explanatory sentence about `del` / `nabla` was added intentionally for English readers. |
| Mathematical Correctness | 5 | Equations and mathematical claims preserved. `linear functional`, `cotangent space`, `oriented area`, and `oriented volume` are appropriate. |
| Terminology Consistency | 4 | `measuring device` is used consistently. `curl` is used for `回転`, while roadmap retains `rot` in the Japanese-derived operator list where appropriate. |
| Markdown and Build Compatibility | 4 | Markdown and math blocks are valid. No YAML front matter yet; this may need a project-level decision. |

### Required Revisions Made

- None.

### Intentional Translation Note

The following explanation is not present literally in the Japanese source but was added for the English edition:

> In English, the symbol $\nabla$ is called **del**, and also **nabla**. In Japanese textbooks, it is often called *nabla*.

This is justified because the Japanese title and terminology rely on the Japanese convention of calling $\nabla$ `ナブラ`, whereas English readers need the `del` / `nabla` distinction.

### Remaining Pass 2 Issues

- Several sentences are faithful but still Japanese-like in information structure.
- The phrase `There is another symbol this book wants to take up` should probably become something like `The other symbol we need to confront is $\nabla$` in Pass 2.
- The paragraph on the graduate-school friend is clear but can be made more direct.

### Pass 1 Status

Passed with one documented English-edition addition.

---

## `manuscript/en/ch00/03_portal.md`

### Scores

| Item | Score | Notes |
|---|---:|---|
| Source Fidelity | 5 | Content preserved. |
| Mathematical Correctness | 5 | No mathematical content requiring correction. |
| Terminology Consistency | 5 | `Note` use is appropriate. |
| Markdown and Build Compatibility | 4 | Markdown structure and links preserved. English edition may later need an English portal URL rather than `/jp/`. |

### Required Revisions Made

- None.

### Remaining Pass 2 Issues

- Decide later whether the English edition should point to `/jp/` or to a future English portal page.

### Pass 1 Status

Passed.

---

# Overall ch00 Pass 1 Result

`ch00` passes Pass 1 as an initial faithful draft.

Current status:

- Source fidelity: acceptable for ch00.
- Mathematical correctness: no detected issues.
- Terminology consistency: acceptable.
- Markdown compatibility: acceptable, pending a project-level decision about YAML front matter for English chapter files.

Next recommended step:

- Begin Pass 2 for ch00, focusing on English information structure and rhythm, **before** treating these files as ready English prose.
