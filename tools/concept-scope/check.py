#!/usr/bin/env python3
"""Concept-scope checker — thin compatibility wrapper.

All real logic lives in the `concept_scope` package.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

from concept_scope import (
    compile_rules,
    check_file,
    default_files,
    load_chapters,
    load_concepts,
    render_text,
    scope_for_chapter,
    Diagnostic,
    REPO_ROOT,
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check manuscript concept scope.")
    parser.add_argument(
        "files",
        nargs="*",
        help="Markdown files to check. Defaults to manuscript/ja/ch*/ch*.md.",
    )
    parser.add_argument(
        "--root",
        default=str(REPO_ROOT),
        help="Repository root. Defaults to the detected nabla-kaitai root.",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format.",
    )
    parser.add_argument(
        "--fail-on-warning",
        action="store_true",
        help="Return non-zero if any diagnostic is found, not only errors.",
    )
    parser.add_argument(
        "--export-context",
        metavar="CHAPTER",
        help="Export LLM context for the given chapter (e.g. ch04).",
    )
    parser.add_argument(
        "--check-consistency",
        action="store_true",
        help="Check frontmatter vs CHAPTER_SCOPES.yaml consistency.",
    )
    return parser.parse_args(argv)


def _export_markdown(chapter_id: str) -> str:
    from concept_scope.context import export_context_markdown

    return export_context_markdown(chapter_id)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    root = Path(args.root).resolve()

    # LLM context export mode
    if args.export_context:
        chapter_id = args.export_context
        scope = scope_for_chapter(chapter_id)
        if args.format == "json":
            from concept_scope.context import export_context_json

            print(json.dumps(export_context_json(chapter_id), ensure_ascii=False, indent=2))
        else:
            print(_export_markdown(chapter_id))
        return 0

    # Consistency check mode
    if args.check_consistency:
        from concept_scope.consistency import check_consistency, render_consistency

        issues = check_consistency(root)
        print(render_consistency(issues))
        return 1 if issues else 0

    chapters = load_chapters(root)
    rules = compile_rules(str(root / "docs" / "concept-scope"))
    concepts = load_concepts()

    files = [Path(item) for item in args.files] if args.files else default_files(root)
    files = [(path if path.is_absolute() else root / path) for path in files]

    diagnostics: list[Diagnostic] = []
    for path in files:
        diagnostics.extend(check_file(path, root, chapters, rules, concepts=concepts))

    diagnostics.sort(key=lambda item: (item.path, item.line, item.column, item.code))

    if args.format == "json":
        print(json.dumps([asdict(item) for item in diagnostics], ensure_ascii=False, indent=2))
    else:
        print(render_text(diagnostics))

    if any(item.severity == "error" for item in diagnostics):
        return 1
    if args.fail_on_warning and diagnostics:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
