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

Decision: use **curl** in English prose unless specifically discussing notation.

Reason:

- `rot` is understandable in some mathematical traditions, but `curl` is the ordinary English vector-analysis term.
- The Japanese `回転` maps naturally to `curl` for English readers.
- The occurrence of `grad, rot, div` in the current TOC is retained only where it mirrors the Japanese operator triad and may be revisited at the chapter level.

### 4. Portal URL

Decision: keep `/jp/` for now.

Reason:

- There is no confirmed English portal URL yet.
- The review notes record this as a future publication issue.

---

## File Status

| File | Pass 3 Status | Notes |
|---|---|---|
| `manuscript/en/ch00/01_preface.md` | passed | English heading set to `Preface`; voice acceptable. |
| `manuscript/en/ch00/02_introduction.md` | passed | `del/nabla` explanation polished; math unchanged. |
| `manuscript/en/ch00/03_portal.md` | passed with note | English portal URL decision deferred. |

---

# Overall ch00 Pass 3 Result

`ch00` passes Pass 3.

It is now suitable as the first polished English sample for the project, subject to later global consistency checks once Chapter 1 and later chapters are translated.

Remaining global issues:

- Decide whether English chapter files should include YAML front matter.
- Decide whether the English edition will have its own portal URL.
- Revisit `grad, rot, div` vs `grad, curl, div` when translating Chapters 6–8.
