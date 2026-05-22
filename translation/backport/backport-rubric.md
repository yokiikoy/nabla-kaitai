# Japanese Backport Rubric

Reverse-import from the English translation workflow into `manuscript/ja/`. Japanese edition remains the primary voice; English-only choices are not backported.

## Priority

| Level | Apply when | Approval |
|-------|------------|----------|
| **P0** | Factual error: wrong chapter ref, symbol clash ($\rho$ vs $\rho_{\mathrm e}$), sign/dimension typo | Apply in Wave PR |
| **P1** | Formatting, duplicate `---`, internal JA terminology drift, TOC/roadmap mismatch | Apply in Wave PR |
| **P2** | Clarity: ambiguous sentence, redundant Note, FAQ gap | Author review |
| **Skip** | English voice, `curl` vs `rot`, `del`/`nabla` notes, paragraph reorder | Log as wontfix |

## Do not backport

- `rot` → `curl` (English edition only)
- English information-structure rewrites
- Metaphor substitutions (`measuring rod` → `measuring device`) unless JA already inconsistent

## Record format

See `backport-log.md`. Each item: id, file, priority, source, action, status.

## PR rules

- Branch: `edit/ja-backport-waveN` from `main`
- One theme per PR when possible; rebuild PDF after merge
- If fix is factual, optionally mirror in `manuscript/en/` in a follow-up translation PR
