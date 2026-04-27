"""Frontmatter ↔ CHAPTER_SCOPES.yaml consistency checker.

Detects mismatches between per-file YAML frontmatter and the centralized
CHAPTER_SCOPES.yaml config.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from concept_scope.config import CONFIG_DIR, load_yaml
from concept_scope.frontmatter import read_frontmatter, get_frontmatter_scope
from concept_scope.scope import load_chapters_list


@dataclass(frozen=True)
class ConsistencyIssue:
    chapter_id: str
    field: str
    concept_id: str
    kind: str
    detail: str


def check_consistency(root: Path | None = None) -> list[ConsistencyIssue]:
    """Compare frontmatter scope with CHAPTER_SCOPES.yaml for all chapters.

    Returns a list of mismatches. Empty list = consistent.
    """
    config_dir = CONFIG_DIR if root is None else (Path(root) / "docs" / "concept-scope")
    config_file = config_dir / "CHAPTER_SCOPES.yaml"
    if not config_file.exists():
        # No config file — can't check consistency
        return []

    chapters_list = load_chapters_list(root)
    issues: list[ConsistencyIssue] = []

    for chap_def in chapters_list:
        chapter_id = chap_def["id"]
        chapter_path = root / chap_def["path"] if root else CONFIG_DIR.parent.parent / chap_def["path"]
        if not chapter_path.exists():
            issues.append(ConsistencyIssue(
                chapter_id=chapter_id, field="file", concept_id="",
                kind="missing_file",
                detail=f"File not found: {chap_def['path']}",
            ))
            continue

        fm_scope = get_frontmatter_scope(chapter_path)
        if fm_scope is None:
            issues.append(ConsistencyIssue(
                chapter_id=chapter_id, field="frontmatter", concept_id="",
                kind="missing_frontmatter",
                detail="No concept-scope fields in frontmatter",
            ))
            # Still compare for other issues with empty fm
            fm_scope = {"introduces": {}, "previews": {}, "recap_policy": {}}

        # Compare introduces
        _compare_scopes(
            chapter_id, "introduces",
            chap_def.get("introduces", {}),
            fm_scope.get("introduces", {}),
            issues,
        )

        # Compare previews
        _compare_scopes(
            chapter_id, "previews",
            chap_def.get("previews", {}),
            fm_scope.get("previews", {}),
            issues,
        )

        # Compare recap_policy
        _compare_scopes(
            chapter_id, "recap_policy",
            chap_def.get("recap_policy", {}),
            fm_scope.get("recap_policy", {}),
            issues,
        )

    return issues


def _compare_scopes(
    chapter_id: str,
    field: str,
    yaml_val: dict,
    fm_val: dict,
    issues: list[ConsistencyIssue],
):
    all_keys = set(yaml_val.keys()) | set(fm_val.keys())
    for key in all_keys:
        in_yaml = key in yaml_val
        in_fm = key in fm_val

        if in_yaml and not in_fm:
            issues.append(ConsistencyIssue(
                chapter_id=chapter_id, field=field, concept_id=key,
                kind="yaml_only",
                detail=f"CHAPTER_SCOPES.yaml に定義あり、frontmatter になし",
            ))
        elif not in_yaml and in_fm:
            issues.append(ConsistencyIssue(
                chapter_id=chapter_id, field=field, concept_id=key,
                kind="frontmatter_only",
                detail=f"frontmatter に定義あり、CHAPTER_SCOPES.yaml になし",
            ))
        else:
            yaml_info = _normalize_info(yaml_val[key])
            fm_info = _normalize_info(fm_val[key])
            if yaml_info != fm_info:
                issues.append(ConsistencyIssue(
                    chapter_id=chapter_id, field=field, concept_id=key,
                    kind="mismatch",
                    detail=f"yaml={yaml_info} vs frontmatter={fm_info}",
                ))


def _normalize_info(val: Any) -> dict:
    """Normalize scope info to a comparable dict."""
    if isinstance(val, dict):
        return {k: str(v) for k, v in sorted(val.items())}
    return {"_value": str(val)}


def render_consistency(issues: list[ConsistencyIssue]) -> str:
    if not issues:
        return "consistency: all chapters match CHAPTER_SCOPES.yaml"

    from collections import defaultdict
    by_chapter: dict[str, list[ConsistencyIssue]] = defaultdict(list)
    for issue in issues:
        by_chapter[issue.chapter_id].append(issue)

    lines: list[str] = []
    for chapter_id in sorted(by_chapter.keys()):
        lines.append(f"\n{chapter_id}:")
        for issue in by_chapter[chapter_id]:
            lines.append(
                f"  {issue.kind:20s} {issue.field:14s} {issue.concept_id:25s} {issue.detail}"
            )

    return "\n".join(lines)
