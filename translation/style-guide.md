# English Translation Style Guide v0.1

## Title

*Unmasking Div, Grad, and Curl: A Heuristic Matrix Route from Differential Forms to Vector Analysis*

## Basic Policy

Literal but readable. Preserve the mathematical structure, notation, and order of argument as much as possible, while making the English natural.

## Tone

Clear, direct, mildly polemical. The target tone is roughly Feynman / Andy Weir: conversational, sharp, occasionally funny, willing to poke at authority, but never contemptuous toward the reader.

## Fixed Choices

| Japanese | English | Notes |
|---|---|---|
| 測定器 | measuring device | central metaphor |
| 面積測定器 | area-measuring device | |
| 体積測定器 | volume-measuring device | |
| 横ベクトル | row vector | omit horizontal/vertical note unless needed |
| 縦ベクトル | column vector | omit horizontal/vertical note unless needed |
| 我々 | we | often author + reader |
| 筆者 | I | avoid “the author” unless distance is useful |
| 本書 | this book / here / our goal | vary to avoid stiffness |
| 注 | Note / Warning / Aside / Remark | choose by function |
| ナブラ | nabla / del | explain at first appearance |
| 回転 | curl | use curl consistently; do not use rot in English edition |

## Notes and Asides

Do not translate every 注 mechanically as “Note.” Use:

- **Note** for mathematical or explanatory supplements.
- **Warning** for traps or possible misunderstandings.
- **Aside** for digressions, jokes, or authorial commentary.
- **Remark** for authorial positioning or meta-commentary.

## nabla / del

At the first substantial appearance of $\nabla$, explain that English usually calls it **del**, and also **nabla**, while Japanese textbooks often use *nabla*. The book is about what div, grad, and curl do, not primarily about the name of the symbol.

## curl / rot

Use **curl** throughout the English edition. Do not use **rot**, even when the Japanese source uses the operator triad `grad, rot, div`. Translate or normalize it as `grad, curl, div` unless a passage is explicitly discussing notation in different traditions.

## English Front Matter

For now, English chapter files do not need YAML front matter. Revisit this only if the build system or site generator requires it.

## English Portal

Use the English portal URL:

[https://covectorspace.xyz/en/](https://covectorspace.xyz/en/)
