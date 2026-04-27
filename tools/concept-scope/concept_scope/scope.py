"""Chapter scope resolution: determines what concepts are allowed in each chapter."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from concept_scope.config import CONFIG_DIR, load_yaml
from concept_scope.frontmatter import get_frontmatter_scope
from concept_scope.models import Chapter, ChapterScope


def load_chapters(root: Path | None = None) -> dict[str, Chapter]:
    """Load chapter registry from CHAPTER_SCOPES.yaml.

    Returns a dict mapping relative file path -> Chapter.
    """
    config_dir = CONFIG_DIR if root is None else (Path(root) / "docs" / "concept-scope")
    data = load_yaml(config_dir / "CHAPTER_SCOPES.yaml")
    chapters: dict[str, Chapter] = {}
    for item in data.get("chapters", []):
        chapter = Chapter(
            id=str(item["id"]),
            path=str(item["path"]),
            chapter=int(item["chapter"]),
            order=int(item["order"]),
        )
        chapters[chapter.path] = chapter
    return chapters


def load_chapters_list(root: Path | None = None) -> list[dict[str, Any]]:
    """Load raw chapter scope data from CHAPTER_SCOPES.yaml as a list."""
    config_dir = CONFIG_DIR if root is None else (Path(root) / "docs" / "concept-scope")
    config_file = config_dir / "CHAPTER_SCOPES.yaml"
    if not config_file.exists():
        return []
    data = load_yaml(config_file)
    return data.get("chapters", [])


def _chapter_number(name: str) -> int:
    return int(name.replace("ch", ""))


def scope_for_chapter(
    chapter_id: str,
    root: Path | None = None,
    frontmatter_path: Path | None = None,
) -> ChapterScope:
    """Resolve the full scope for a given chapter.

    Merges frontmatter (priority) with CHAPTER_SCOPES.yaml (fallback).

    Returns a ChapterScope with:
    - available: concept_id -> max_level (concepts introduced in or before this chapter)
    - being_introduced: concept_id -> {from, to} (concepts this chapter introduces)
    - preview_only: concept_id -> {max_level, note?} (future concepts allowed as foreshadowing)
    - recap_limited: concept_id -> {max_level, max_lines} (known concepts with recap limits)
    - forbidden: list of concept_ids that must not be used
    """
    chapters_list = load_chapters_list(root)
    fm_scope = get_frontmatter_scope(frontmatter_path) if frontmatter_path else None

    chapter_num = _chapter_number(chapter_id)

    # Find chapter definition from centralized config
    chap_def = None
    for item in chapters_list:
        if item["id"] == chapter_id:
            chap_def = item
            break

    # Merge: frontmatter overrides centralized config
    introduces = fm_scope.get("introduces", {}) if fm_scope else {}
    previews = fm_scope.get("previews", {}) if fm_scope else {}
    recap_policy = fm_scope.get("recap_policy", {}) if fm_scope else {}
    if chap_def:
        if not introduces:
            introduces = chap_def.get("introduces", {})
        if not previews:
            previews = chap_def.get("previews", {})
        if not recap_policy:
            recap_policy = chap_def.get("recap_policy", {})

    order = chap_def.get("order", chapter_num * 10) if chap_def else chapter_num * 10

    # Build available concepts from all chapters up to and including current
    available: dict[str, str] = {}
    being_introduced: dict[str, dict] = {}
    preview_only: dict[str, dict] = {}
    recap_limited: dict[str, dict] = {}
    forbidden: list[str] = []

    for item in chapters_list:
        item_num = _chapter_number(item["id"])
        item_introduces = item.get("introduces", {})
        item_previews = item.get("previews", {})

        for cid, info in item_introduces.items():
            if isinstance(info, dict):
                to_level = info.get("to", "computation")
            else:
                to_level = "computation"
            if item_num <= chapter_num:
                available[cid] = to_level
                if item_num == chapter_num:
                    being_introduced[cid] = info if isinstance(info, dict) else {"to": info}
            else:
                forbidden.append(cid)

        if item_num == chapter_num:
            for cid, info in item_previews.items():
                if isinstance(info, dict):
                    preview_only[cid] = info
                else:
                    preview_only[cid] = {"max_level": str(info)}

            if recap_policy:
                recap_limited = recap_policy

    for cid in list(forbidden):
        if cid in available or cid in preview_only:
            forbidden.remove(cid)

    return ChapterScope(
        chapter_id=chapter_id,
        order=order,
        available=available,
        being_introduced=being_introduced,
        preview_only=preview_only,
        recap_limited=recap_limited,
        forbidden=forbidden,
    )


def infer_chapter(
    path: Path,
    root: Path,
    chapters: dict[str, Chapter] | None = None,
) -> Chapter | None:
    """Infer which chapter a file belongs to.

    Tries in order:
    1. Exact path match in chapters dict
    2. Frontmatter chapter field
    3. Returns None if not determinable
    """
    from concept_scope.frontmatter import get_frontmatter_chapter

    rel = relative_path(path, root)
    if chapters and rel in chapters:
        return chapters[rel]

    chapter_num = get_frontmatter_chapter(path)
    if chapter_num is not None:
        return Chapter(
            id=f"ch{chapter_num:02d}",
            path=rel,
            chapter=chapter_num,
            order=chapter_num * 10,
        )
    return None


def relative_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()
