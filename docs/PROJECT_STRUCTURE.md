# Project Structure

This repository separates source manuscripts from generated outputs.

## Source Manuscripts

- `manuscript/ja/ch01` through `manuscript/ja/ch11`: Japanese source chapters.
- `manuscript/en/ch01` through `manuscript/en/ch11`: English translation chapters.

Each chapter directory should contain Markdown math `.md` files. The exact file naming can be decided when the first full chapter is migrated, but the recommended default is:

```text
main.md
```

## Outputs

- `exports/pdf/`: combined full-book PDF exports.
- `exports/note/ja/`: note.com converted Japanese Markdown.
- `exports/note/en/`: note.com converted English Markdown, if needed.
- `galleys/`: review PDFs and proof files.

Generated scratch files should go under `build/`, which is ignored.

## References

- `references/pdfs/books/`: book PDFs.
- `references/pdfs/papers/`: paper PDFs.
- `references/pdfs/other/`: other PDF references.
- `references/ocr-md/`: OCR Markdown derived from PDFs when needed.

PDF originals are local by default. OCR Markdown may be committed when it is useful for drafting, review, or reproducibility.
