# Concept Scope Checker

CLI + LSP for managing educational concept scope in a math textbook project.

## Architecture

```
tools/concept-scope/
├── check.py                  # CLI entry point (thin wrapper)
├── lsp_server.py             # pygls-based LSP server
├── migrate_frontmatter.py    # One-shot frontmatter migration tool
├── concept_scope/            # Core package
│   ├── models.py             # Data classes (Diagnostic, Chapter, Concept, ...)
│   ├── config.py             # YAML loading, repo root
│   ├── registry.py           # CONCEPTS.yaml reader + alias index builder
│   ├── rules.py              # RULES.yaml compiler, active_rule
│   ├── scope.py              # CHAPTER_SCOPES.yaml reader, scope resolution
│   ├── frontmatter.py        # YAML frontmatter parser
│   ├── checker.py            # Core checking logic (regex + file scanning)
│   ├── levels.py             # Usage level classifier (mention..theorem_use)
│   ├── context.py            # LLM context export (Markdown + JSON)
│   └── hover.py              # Hover & completion providers (LSP)
├── tests/                    # pytest test suite (84 tests)
└── .venv/                    # Python virtual env with pygls + dependencies
```

It reads:
- `docs/concept-scope/CONCEPTS.yaml` — concept registry with aliases and summaries
- `docs/concept-scope/CHAPTER_SCOPES.yaml` — chapter-level scope
- `docs/concept-scope/RULES.yaml` — diagnostic rules (regex + level-based)
- Chapter `.md` files' YAML frontmatter — per-file scope overrides

## Quick Start

```sh
python3 -m venv tools/concept-scope/.venv
tools/concept-scope/.venv/bin/pip install -r tools/concept-scope/requirements.txt
```

## CLI Usage

```sh
# Check all chapters
python3 tools/concept-scope/check.py

# Check one file
python3 tools/concept-scope/check.py manuscript/ja/ch04/ch04.md

# JSON output
python3 tools/concept-scope/check.py --format json

# Fail on warnings
python3 tools/concept-scope/check.py --fail-on-warning

# LLM context export (Markdown)
python3 tools/concept-scope/check.py --export-context ch04

# LLM context export (JSON)
python3 tools/concept-scope/check.py --export-context ch04 --format json
```

## LSP Server

Provides `textDocument/didOpen`, `textDocument/didSave` diagnostics,
`textDocument/hover` concept info, and `textDocument/completion` concept suggestions.

### Stdio (editor integration)

```sh
tools/concept-scope/.venv/bin/python tools/concept-scope/lsp_server.py
```

With an explicit repository root:

```sh
tools/concept-scope/.venv/bin/python tools/concept-scope/lsp_server.py --root /path/to/nabla-kaitai
```

### TCP (debugging)

```sh
tools/concept-scope/.venv/bin/python tools/concept-scope/lsp_server.py --tcp --port 2087
```

Then connect an LSP client to `127.0.0.1:2087`.

### LSP Features

| Feature | Status |
|---|---|
| `textDocument/didOpen` | regex diagnostics on open |
| `textDocument/didSave` | regex diagnostics on save |
| `textDocument/hover` | concept definition, chapter, allowed level |
| `textDocument/completion` | concept suggestions filtered by chapter scope |
| `concept-scope/exportContext` | LLM context export via LSP command |

## Testing

```sh
tools/concept-scope/.venv/bin/python -m pytest tools/concept-scope/tests/ -v
```

## Frontmatter Migration

Chapter scope data from `CHAPTER_SCOPES.yaml` was migrated into each `.md` file's
YAML frontmatter via `migrate_frontmatter.py` (one-shot, already run).

## Notes

Diagnostics are regex-based. The checker ignores YAML frontmatter and fenced code
blocks. Usage level classification uses heuristic patterns (TeX math detection,
definition/intuition/theorem patterns). Full AST parsing is out of scope.
