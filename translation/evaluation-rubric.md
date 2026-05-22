# English Translation Evaluation Rubric v0.1

This rubric is used to evaluate each English translation draft of *Unmasking Div, Grad, and Curl*.

The goal is not merely to produce grammatically correct English. The goal is to produce an English mathematical text that preserves the author’s argument, tone, and pedagogical strategy while reading naturally as English.

## Rating Scale

Use a 1–5 scale for each item.

| Score | Meaning |
|---|---|
| 5 | Ready for publication, except for minor polishing |
| 4 | Good; only local revisions needed |
| 3 | Understandable, but visibly draft-like |
| 2 | Meaning often survives, but the English or structure obstructs reading |
| 1 | Needs retranslation |

## Core Evaluation Items

### 1. Source Fidelity

Does the translation preserve the meaning, argumentative order, mathematical claims, and rhetorical intent of the Japanese source?

Checkpoints:

- No missing claims.
- No added claims that change the argument.
- Mathematical dependencies are preserved.
- Jokes, cautions, and authorial asides are not silently flattened.
- Where the English rearranges the sentence, the logical relation remains intact.

### 2. Mathematical Correctness

Does the English preserve the mathematics exactly and avoid introducing misleading terminology?

Checkpoints:

- Symbols, equations, indices, signs, and dimensions are unchanged unless deliberately corrected.
- Standard terms are used correctly: differential form, exterior derivative, pullback, metric, Hodge star, divergence, gradient, curl.
- Informal terms such as “measuring device” remain compatible with the formal mathematics.
- No English phrasing suggests a false mathematical statement.
- Ambiguous terms such as “operator,” “function,” “map,” and “form” are used consistently with the local context.

### 3. Terminology Consistency

Does the translation follow `translation/glossary.md` and the project style decisions?

Checkpoints:

- 測定器 → measuring device, with occasional natural variation such as “measures ...”.
- 横ベクトル → row vector.
- 縦ベクトル → column vector.
- ナブラ / $\nabla$ → del / nabla according to context.
- 注 → Note / Warning / Aside / Remark according to function.
- Repeated conceptual terms are not translated differently without reason.

### 4. English Information Structure

Does the English present information in an order that feels natural to English readers?

Checkpoints:

- Paragraphs usually begin with the point, not only with background.
- Long Japanese-style buildup is shortened or reorganized when needed.
- Topic sentences are clear.
- Contrast markers such as “however,” “but,” “instead,” and “therefore” are used naturally.
- The reader can tell what each paragraph is doing before reaching its final sentence.

### 5. English Naturalness and Rhythm

Does the prose sound like English rather than translated Japanese?

Checkpoints:

- Avoids unnecessary “there is/there are.”
- Avoids stiff expressions such as “the author thinks” where “I think” is natural.
- Avoids redundant structures such as “was written as a book for answering.”
- Uses active verbs where appropriate.
- Sentence lengths vary naturally.
- The text can be read aloud without excessive friction.

### 6. Authorial Voice

Does the translation preserve the intended voice: clear, direct, mildly polemical, with Feynman / Andy Weir-like energy?

Checkpoints:

- The prose can be sharp without sounding hostile.
- Authority may be teased, but the reader is not mocked.
- Humor and irritation are preserved when they serve the argument.
- The voice remains personal where the Japanese is personal.
- Over-polishing does not erase the author’s character.

### 7. Pedagogical Flow

Does the translation preserve the learning path designed by the book?

Checkpoints:

- The concrete-to-abstract progression remains visible.
- The reader is not thrown into advanced terminology too early.
- Repeated phrases that serve pedagogy are preserved or replaced with equivalent English cues.
- Summaries and previews actually help the reader navigate.
- Notes do not unnecessarily interrupt the learning flow in English.

### 8. Note and Aside Handling

Are notes, warnings, asides, and remarks handled appropriately in English?

Checkpoints:

- The label matches the function: Note, Warning, Aside, or Remark.
- Long notes are readable and not overly dense.
- Defensive notes remain defensive where needed, but not excessively legalistic.
- Meta-comments are not made more pompous than the Japanese.
- Jokes in notes are preserved when possible.

### 9. Title and Heading Quality

Do headings work as English headings, not merely translations of Japanese headings?

Checkpoints:

- Headings are concise enough to scan.
- The “What is ...?” structure is preserved where pedagogically important.
- Long subtitles are readable and not overloaded.
- Chapter and section titles are consistent with the current Japanese TOC.
- Key title terms match the style guide.

### 10. Markdown and Build Compatibility

Does the translated file remain structurally compatible with the project?

Checkpoints:

- YAML front matter is preserved or intentionally adapted.
- Markdown heading levels are preserved.
- Math blocks remain valid.
- HTML fragments such as `<strong>` are not broken.
- Links and URLs remain valid.
- No temporary or test files are left behind.

## Recommended Passes

Use the rubric differently in each pass.

### Pass 1: Faithful Draft

Primary items:

- Source Fidelity
- Mathematical Correctness
- Terminology Consistency
- Markdown and Build Compatibility

### Pass 2: English Information Structure

Primary items:

- English Information Structure
- English Naturalness and Rhythm
- Pedagogical Flow

### Pass 3: Voice and Publication Polish

Primary items:

- Authorial Voice
- Note and Aside Handling
- Title and Heading Quality

## Per-File Review Template

```markdown
# Review: <file path>

## Scores

| Item | Score | Notes |
|---|---:|---|
| Source Fidelity |  |  |
| Mathematical Correctness |  |  |
| Terminology Consistency |  |  |
| English Information Structure |  |  |
| English Naturalness and Rhythm |  |  |
| Authorial Voice |  |  |
| Pedagogical Flow |  |  |
| Note and Aside Handling |  |  |
| Title and Heading Quality |  |  |
| Markdown and Build Compatibility |  |  |

## Required Revisions

- 

## Optional Revisions

- 

## Representative Before / After

### Before

> 

### After

> 
```

## Practical Rule

A file should not be considered “translated” until it has passed at least Pass 1. A file should not be considered “ready” until it has passed Pass 2. Publication-level English requires Pass 3.
