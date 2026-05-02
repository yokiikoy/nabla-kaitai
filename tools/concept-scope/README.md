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

## Daily Workflow

### Editing a chapter

```sh
# Save, then check just your chapter
python3 tools/concept-scope/check.py manuscript/ja/ch05/ch05.md

# Check all chapters for cross-chapter regressions
python3 tools/concept-scope/check.py --fail-on-warning
```

### Before committing

```sh
# Full check + consistency audit
python3 tools/concept-scope/check.py --fail-on-warning && \
python3 tools/concept-scope/check.py --check-consistency
```

Both should exit 0. If `--check-consistency` reports mismatches, re-run
`migrate_frontmatter.py` to sync frontmatter.

## Adding a New Concept

1. Add an entry to `docs/concept-scope/CONCEPTS.yaml`:

```yaml
- id: your_concept_id
  label: "表示名"
  kind: object            # object | notation | operator | operation | theorem | structure | application
  introduced_in: ch05     # chapter where defined
  order: 55               # pedagogical order (must be unique-ish)
  aliases:
    - "表示名"
    - "another-name"
  summary: "One-line description."
```

2. **Alias rules**:
   - Must be **at least 3 characters** (no single-char like `*`, `d`, `J`)
   - Must be **unambiguous** — no everyday Japanese words like `形式`, `長さ`, `角度`
   - Use multi-character TeX commands (`\ast`, `\nabla`) rather than raw symbols
   - Test with `check.py` — if you get false positives, the alias is too broad

3. Add the concept to the appropriate chapter in `CHAPTER_SCOPES.yaml`
   (either `introduces`, `previews`, or `assumes`).

4. Run:
```sh
python3 tools/concept-scope/migrate_frontmatter.py
python3 tools/concept-scope/check.py --check-consistency
```

## Adding a New Chapter

1. Create `manuscript/ja/chXX/chXX.md` with YAML frontmatter:

```yaml
---
chapter: 12
order: 120
assumes:
  - concept_already_known
introduces:
  new_concept:
    from: intuition
    to: computation
previews:
  future_concept:
    max_level: mention
    allowed_context_patterns:
      - "次章"
      - "後で"
recap_policy:
  old_concept:
    max_level: mention
    max_lines: 3
---
```

2. Add the chapter definition to `docs/concept-scope/CHAPTER_SCOPES.yaml`:

```yaml
- id: ch12
  path: manuscript/ja/ch12/ch12.md
  title: "章タイトル"
  chapter: 12
  order: 120
  assumes: [...]
  introduces:
    new_concept:
      from: intuition
      to: computation
  previews: {}
  recap_policy: {}
```

3. Run consistency check:
```sh
python3 tools/concept-scope/check.py --check-consistency
```

## LLM-Assisted Writing

### Generate writing constraints before prompting

```sh
# Paste this output at the top of your LLM prompt
python3 tools/concept-scope/check.py --export-context ch05
```

The output tells the LLM:
- Which concepts are **available** and at what max level
- Which concepts can only be **foreshadowed** (name/intuition, no formulas)
- Which concepts must **not be re-explained** (already defined)
- Which concepts are **forbidden** entirely
- **Permanent notation contracts** (e.g., no `dx^2`)

### After LLM generates text

```sh
# Check LLM output for violations
python3 tools/concept-scope/check.py path/to/generated.md --fail-on-warning
```

### JSON format for tool-based LLM integration

```sh
python3 tools/concept-scope/check.py --export-context ch05 --format json
```

## CI Integration

`.github/workflows/concept-scope.yaml` runs on push/PR:

```yaml
steps:
  - run: python -m venv tools/concept-scope/.venv
  - run: tools/concept-scope/.venv/bin/pip install -r tools/concept-scope/requirements.txt
  - run: tools/concept-scope/.venv/bin/python -m pytest tools/concept-scope/tests/ -v
  - run: python3 tools/concept-scope/check.py --fail-on-warning
```

PRs with concept violations fail in CI. Adjust severity thresholds in
`RULES.yaml` if needed for your project's strictness level.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Too many false positives from aliases | Narrow aliases in `CONCEPTS.yaml`. Avoid single chars, common words |
| Legitimate foreshadowing flagged as error | Add concept to chapter `previews` in `CHAPTER_SCOPES.yaml` with appropriate `max_level` |
| Legitimate formula with foreshadowing context flagged | Add `allowed_context_patterns` to the preview entry |
| Frontmatter out of sync with CHAPTER_SCOPES.yaml | Run `migrate_frontmatter.py` or `--check-consistency` |
| LSP hover shows nothing | Ensure `didOpen` fired; server needs file to exist on disk |
| `python3: No module named yaml` | Use system Python for `check.py` (needs `pyyaml` installed system-wide) |
| `python3: No module named pygls` | Use `.venv/bin/python` for `lsp_server.py` |

## Notes

Diagnostics are regex-based (RULES.yaml) + heuristic level-based (levels.py).
The checker ignores YAML frontmatter and fenced code blocks. Usage level
classification uses TeX math detection and Japanese definition/intuition/theorem
patterns. Full AST parsing is out of scope.
