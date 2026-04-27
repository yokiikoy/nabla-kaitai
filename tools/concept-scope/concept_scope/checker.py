"""Core checking logic: scans markdown and applies rules."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from concept_scope.models import Chapter, Concept, Diagnostic
from concept_scope.rules import active_rule, allowed_by_context, usage_level_value
from concept_scope.scope import infer_chapter, relative_path, scope_for_chapter
from concept_scope.registry import load_concepts
from concept_scope.levels import (
    extract_occurrences,
    parse_allow_annotations,
    parse_roles,
)


def iter_checkable_lines(path: Path) -> list[tuple[int, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    lines_out: list[tuple[int, str]] = []
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    in_code_fence = False

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if idx == 1 and in_frontmatter:
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue
        if stripped.startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue
        lines_out.append((idx, line))
    return lines_out


def iter_checkable_lines_from_text(text: str) -> list[tuple[int, str]]:
    """Same as iter_checkable_lines but from a text string instead of a file."""
    lines = text.splitlines()
    lines_out: list[tuple[int, str]] = []
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    in_code_fence = False

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if idx == 1 and in_frontmatter:
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue
        if stripped.startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue
        lines_out.append((idx, line))
    return lines_out


def check_file(
    path: Path,
    root: Path,
    chapters: dict[str, Chapter],
    rules: list[dict[str, Any]],
    concepts: list[Concept] | None = None,
    mode: str = "full",
) -> list[Diagnostic]:
    """Check a markdown file.

    mode: "full" = regex + level-based, "regex_only" = regex only (faster).
    """
    chapter = infer_chapter(path, root, chapters)
    diagnostics: list[Diagnostic] = []

    for line_no, line in iter_checkable_lines(path):
        for rule in rules:
            if not active_rule(rule, chapter):
                continue
            if allowed_by_context(rule, line):
                continue

            for pattern in rule.get("_patterns", []):
                for match in pattern.finditer(line):
                    diagnostics.append(
                        Diagnostic(
                            path=relative_path(path, root),
                            line=line_no,
                            column=match.start() + 1,
                            end_column=match.end() + 1,
                            severity=str(rule.get("severity", "warning")),
                            code=str(rule["id"]),
                            message=str(rule.get("message", rule["title"])),
                            match=match.group(0),
                        )
                    )

    if mode == "full" and concepts and chapter:
        diagnostics.extend(
            _check_levels(path, root, chapter, concepts)
        )

    return diagnostics


def _check_levels(
    path: Path,
    root: Path,
    chapter: Chapter,
    concepts: list[Concept],
) -> list[Diagnostic]:
    """Level-based diagnostics using concept occurrence extraction and scope resolution.

    Checks:
    - Future concept usage (forbidden or exceeds preview max_level) → error
    - Over-explanation of known concepts (exceeds recap max_level) → warning
    """
    scope = scope_for_chapter(chapter.id, root=root, frontmatter_path=path)
    concept_index = {c.id: c for c in concepts}
    checkable = iter_checkable_lines(path)

    roles = parse_roles(checkable)
    allowed_on_line, allow_all_lines = parse_allow_annotations(checkable)

    occurrences = extract_occurrences(checkable, concepts, roles=roles)
    return _evaluate_occurrences(
        occurrences, scope, concept_index, path, root,
        checkable, allowed_on_line=allowed_on_line,
        allow_all_lines=allow_all_lines,
    )


def _evaluate_occurrences(
    occurrences: list,
    scope,
    concept_index: dict,
    path: Path,
    root: Path,
    checkable: list[tuple[int, str]] | None = None,
    allowed_on_line: dict[int, set[str]] | None = None,
    allow_all_lines: set[int] | None = None,
) -> list[Diagnostic]:
    """Evaluate extracted occurrences against chapter scope."""
    diagnostics: list[Diagnostic] = []
    seen_per_line: dict[tuple[int, str], bool] = {}

    # Build line lookup for context checking
    line_map: dict[int, str] = {}
    if checkable:
        for ln, txt in checkable:
            line_map[ln] = txt

    for occ in occurrences:
        cid = occ.concept_id
        concept = concept_index.get(cid)

        # ── Annotation: skip if line is in allow-all or concept is explicitly allowed ──
        if allow_all_lines and occ.line in allow_all_lines:
            continue
        if allowed_on_line and occ.line in allowed_on_line:
            if not allowed_on_line[occ.line] or cid in allowed_on_line[occ.line]:
                continue

        # ── Preview only: exceeds max_level ──
        if cid in scope.preview_only:
            info = scope.preview_only[cid]
            max_lvl = info.get("max_level", "mention") if isinstance(info, dict) else info
            occ_lvl_val = usage_level_value(occ.level)
            max_lvl_val = usage_level_value(max_lvl)
            if occ_lvl_val > max_lvl_val:
                # Check allowed context patterns in the full line text
                allowed_patterns = info.get("allowed_context_patterns", []) if isinstance(info, dict) else []
                if line_map and _check_line_context(occ.line, line_map, allowed_patterns):
                    continue

                label = concept.label if concept else cid
                msg = (
                    f"「{occ.surface}」({label}) はこの章では {max_lvl} までの"
                    f"伏線のみ許可されています (検出: {occ.level})。"
                )
                diagnostics.append(
                    Diagnostic(
                        path=relative_path(path, root),
                        line=occ.line,
                        column=occ.column,
                        end_column=occ.end_column,
                        severity="error",
                        code="future-concept-level",
                        message=msg,
                        match=occ.surface,
                    )
                )
            continue

        # ── Future concept: forbidden outright ──
        if cid in scope.forbidden:
            intro = concept.introduced_in if concept else "後続章"
            msg = (
                f"「{occ.surface}」({cid}) は {intro} で導入される未来概念です。"
                f"この章では使用できません。"
            )
            diagnostics.append(
                Diagnostic(
                    path=relative_path(path, root),
                    line=occ.line,
                    column=occ.column,
                    end_column=occ.end_column,
                    severity="error",
                    code="future-concept-level",
                    message=msg,
                    match=occ.surface,
                )
            )
            continue

        # ── Over-explanation: recap_limited concept used at definition level ──
        if cid in scope.recap_limited:
            info = scope.recap_limited[cid]
            max_lvl = info.get("max_level", "mention") if isinstance(info, dict) else info
            if occ.level == "definition":
                label = concept.label if concept else cid
                key = (occ.line, cid)
                if key not in seen_per_line:
                    seen_per_line[key] = True
                    msg = (
                        f"「{occ.surface}」({label}) は既習概念です。"
                        f"再定義せず {max_lvl} 程度の参照に留めてください。"
                    )
                    diagnostics.append(
                        Diagnostic(
                            path=relative_path(path, root),
                            line=occ.line,
                            column=occ.column,
                            end_column=occ.end_column,
                            severity="warning",
                            code="over-explanation-level",
                            message=msg,
                            match=occ.surface,
                        )
                    )

    return diagnostics


def _check_line_context(
    line: int,
    line_map: dict[int, str],
    patterns: list[str],
) -> bool:
    """Check if any line adjacent to `line` matches an allowed context pattern."""
    if not patterns:
        return False
    import re
    compiled = [re.compile(p) for p in patterns if p]
    if not compiled:
        return False

    for delta in (-1, 0, 1):
        text = line_map.get(line + delta, "")
        for pat in compiled:
            if pat.search(text):
                return True
    return False


def check_text(
    text: str,
    path: str,
    root: Path,
    chapters: dict[str, Chapter],
    rules: list[dict[str, Any]],
    concepts: list[Concept] | None = None,
    mode: str = "full",
) -> list[Diagnostic]:
    """Check a text string against rules, treating it as if from the given path."""
    file_path = Path(path)
    chapter = None
    if file_path.exists():
        chapter = infer_chapter(file_path, root, chapters)
    diagnostics: list[Diagnostic] = []

    checkable = iter_checkable_lines_from_text(text)
    for line_no, line in checkable:
        for rule in rules:
            if not active_rule(rule, chapter):
                continue
            if allowed_by_context(rule, line):
                continue

            for pattern in rule.get("_patterns", []):
                for match in pattern.finditer(line):
                    diagnostics.append(
                        Diagnostic(
                            path=path,
                            line=line_no,
                            column=match.start() + 1,
                            end_column=match.end() + 1,
                            severity=str(rule.get("severity", "warning")),
                            code=str(rule["id"]),
                            message=str(rule.get("message", rule["title"])),
                            match=match.group(0),
                        )
                    )

    if mode == "full" and concepts and chapter and file_path.exists():
        diagnostics.extend(
            _check_levels_from_occurrences(
                file_path, root, chapter, concepts, checkable
            )
        )

    return diagnostics


def _check_levels_from_occurrences(
    path: Path,
    root: Path,
    chapter: Chapter,
    concepts: list[Concept],
    checkable: list[tuple[int, str]],
) -> list[Diagnostic]:
    """Level-based diagnostics from pre-extracted checkable lines (for check_text reuse)."""
    scope = scope_for_chapter(chapter.id, root=root, frontmatter_path=path)
    concept_index = {c.id: c for c in concepts}

    roles = parse_roles(checkable)
    allowed_on_line, allow_all_lines = parse_allow_annotations(checkable)

    occurrences = extract_occurrences(checkable, concepts, roles=roles)
    return _evaluate_occurrences(
        occurrences, scope, concept_index, path, root,
        checkable, allowed_on_line=allowed_on_line,
        allow_all_lines=allow_all_lines,
    )


def default_files(root: Path) -> list[Path]:
    return sorted((root / "manuscript" / "ja").glob("ch*/ch*.md"))


def render_text(diagnostics: list[Diagnostic]) -> str:
    if not diagnostics:
        return "concept-scope: no diagnostics"
    lines = []
    for diag in diagnostics:
        lines.append(
            f"{diag.path}:{diag.line}:{diag.column}: "
            f"{diag.severity}: {diag.code}: {diag.message} "
            f"(matched: {diag.match})"
        )
    return "\n".join(lines)
