"""YAML frontmatter parsing for chapter Markdown files."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def read_frontmatter(path: Path) -> dict[str, Any] | None:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            raw = "\n".join(lines[1:idx])
            data = yaml.safe_load(raw) or {}
            if not isinstance(data, dict):
                return None
            return data
    return None


def get_frontmatter_chapter(path: Path) -> int | None:
    """Extract chapter number from frontmatter, or None."""
    frontmatter = read_frontmatter(path)
    if frontmatter and "chapter" in frontmatter:
        return int(frontmatter["chapter"])
    return None


def get_frontmatter_scope(path: Path) -> dict[str, Any] | None:
    """Extract concept-scope fields from frontmatter.

    Returns a dict with keys: chapter, order, assumes, introduces,
    previews, recap_policy. Returns None if frontmatter has no scope info.
    """
    frontmatter = read_frontmatter(path)
    if not frontmatter:
        return None
    has_scope = any(
        key in frontmatter
        for key in ("chapter", "assumes", "introduces", "previews", "recap_policy")
    )
    if not has_scope:
        return None
    return {
        "chapter": frontmatter.get("chapter"),
        "order": frontmatter.get("order"),
        "assumes": frontmatter.get("assumes", []),
        "introduces": frontmatter.get("introduces", {}),
        "previews": frontmatter.get("previews", {}),
        "recap_policy": frontmatter.get("recap_policy", {}),
    }
