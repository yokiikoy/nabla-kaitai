# Close-Reading Polish: Chapter 1

Review date: 2026-05-22  
Branch: `ai/english-translation-start`  
File: `manuscript/en/ch01/ch01.md`  
GitHub issue: #161 (closed)  
Commit: `4bb50c0`

Scope: publication polish after Pass 3 — mathematical safety, English naturalness, Markdown maintainability.

---

## Applied

### B1 — `df(\mathbf{v})` as linear part

- §1.2.2 note heading and bullet, §1.2 checkpoint, §1.3 bullet and checkpoint now consistently describe `df(\mathbf{v})` as the **linear part of the change**, not the exact change.

### B2 — §1.6 Markdown

- Removed fragmented `<strong>` around inline math; used plain `**...**` where clean.

### C items (C1–C27 except C2)

- Wording and heading polish across §1.0–§1.6, including §1.4 heading **in New Coordinates** and **viewed through cylindrical coordinates** (replacing `scale marks` / `on Another Scale` in body and `manuscript/en/toc.md`).

### Intentionally unchanged

- **C2** `physical mathematics` — kept as authorial term.
- **D1–D4** — deferred (pullback `\ast` vs `*`, matrix vs linear form, point-dependent `df`, final sentence).

---

## Supersedes Pass 3 decision 5

`ch01-pass3.md` decision 5 kept `scale marks` for voice. Issue #161 C15/C16/C21 replaced that idiom with more natural English (`viewed through cylindrical coordinates`, heading `in New Coordinates`, parameter-space pullback wording). Pass 3 decision 5 is **superseded** for the published English text.

---

## Verification

- Post-edit searches: no `scale marks`, `another scale`, `standard entrance`, `Numerical changes are written as`, or `df(\mathbf{v}) is the change`.
- `git diff --check` passes.
