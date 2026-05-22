# Pass 3 Review: ch00

Review date: 2026-05-22
Branch: `ai/english-translation-start`

Pass 3 scope:

- Authorial voice
- Note and aside handling
- Title and heading quality
- Publication-level polish decisions

---

## Decisions

### 1. `Preface` vs `Greeting`

Decision: use **Preface** in English.

Reason:

- The Japanese heading `ごあいさつ` is source-faithful as `Greeting`, but English books normally use `Preface` for this function.
- The surrounding material functions as a preface, not as a casual greeting.
- Publication-level English should prioritize the English genre convention here.

Files updated:

- `manuscript/en/ch00/01_preface.md`
- `manuscript/en/toc.md`

### 2. `del` / `nabla`

Decision: keep the English-edition explanation, but polish it.

Final wording:

> In English, $\nabla$ is usually called **del**; it is also called **nabla**. Japanese textbooks often use the name *nabla*.

Reason:

- English readers need to know why a Japanese-origin title and discussion care about `nabla`.
- `usually called del` is more natural than `is called del, and also nabla`.

### 3. `curl` / `rot`

Decision: use **curl** consistently in the English edition.

Reason:

- `curl` is the ordinary English vector-analysis term.
- The Japanese `回転` maps naturally to `curl` for English readers.
- Even where the Japanese source uses the operator triad `grad, rot, div`, the English edition should normalize it to `grad, curl, div` unless a passage is explicitly discussing notation in different traditions.

Files updated:

- `translation/glossary.md`
- `translation/style-guide.md`
- `manuscript/en/toc.md`

### 4. Portal URL

Decision: use the English portal URL.

Final URL:

[https://covectorspace.xyz/en/](https://covectorspace.xyz/en/)

Files updated:

- `manuscript/en/ch00/03_portal.md`
- `translation/style-guide.md`

### 5. English Front Matter

Decision: English chapter files do not need YAML front matter for now.

Reason:

- There is no immediate build requirement for English chapter front matter.
- This can be revisited later if the build system or site generator requires it.

---

## File Status

| File | Pass 3 Status | Notes |
|---|---|---|
| `manuscript/en/ch00/01_preface.md` | passed | English heading set to `Preface`; voice acceptable. |
| `manuscript/en/ch00/02_introduction.md` | passed | `del/nabla` explanation polished; math unchanged. |
| `manuscript/en/ch00/03_portal.md` | passed | English portal URL applied. |

---

# Overall ch00 Pass 3 Result

`ch00` passes Pass 3.

It is now suitable as the first polished English sample for the project, subject to later global consistency checks once Chapter 1 and later chapters are translated.

Remaining global issues:

- Revisit YAML front matter only if the build system or site generator requires it.
- Apply `curl`, not `rot`, throughout future English chapters.
