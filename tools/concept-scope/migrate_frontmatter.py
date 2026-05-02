#!/usr/bin/env python3
"""Migrate CHAPTER_SCOPES.yaml data into each chapter's YAML frontmatter.

Reads docs/concept-scope/CHAPTER_SCOPES.yaml and writes the scope fields
(introduces, previews, recap_policy) into the frontmatter of each ch*.md file.

Existing frontmatter is preserved and merged. Non-scope fields are left intact.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = REPO_ROOT / "docs" / "concept-scope"
MANUSCRIPT_DIR = REPO_ROOT / "manuscript" / "ja"


def load_yaml_or_die(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return data


def read_frontmatter(path: Path) -> dict[str, Any] | None:
    """Read existing YAML frontmatter from a markdown file."""
    if not path.exists():
        return None
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            raw = "\n".join(lines[1:idx])
            data = yaml.safe_load(raw) or {}
            if isinstance(data, dict):
                return data
            return None
    return None


def write_frontmatter(path: Path, frontmatter: dict[str, Any]):
    """Replace or add YAML frontmatter in a markdown file.

    Preserves existing frontmatter fields that aren't being overwritten.
    """
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()

    existing = read_frontmatter(path) or {}
    # Merge: new scope values override existing
    merged = {**existing, **frontmatter}

    yaml_str = yaml.dump(merged, allow_unicode=True, default_flow_style=False, sort_keys=False).strip()

    if lines and lines[0].strip() == "---":
        # Replace existing frontmatter
        for end_idx in range(1, len(lines)):
            if lines[end_idx].strip() == "---":
                new_lines = ["---", yaml_str, "---"] + lines[end_idx + 1:]
                path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
                return
        # Frontmatter was never closed, treat as no frontmatter
        new_lines = ["---", yaml_str, "---", ""] + lines
        path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    else:
        # No frontmatter, prepend
        new_lines = ["---", yaml_str, "---", ""] + lines
        path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


def main():
    chapter_scopes = load_yaml_or_die(CONFIG_DIR / "CHAPTER_SCOPES.yaml")
    migrated = 0

    for item in chapter_scopes.get("chapters", []):
        chapter_path = REPO_ROOT / item["path"]
        if not chapter_path.exists():
            print(f"SKIP: {item['path']} (file not found)", file=sys.stderr)
            continue

        fm_data: dict[str, Any] = {
            "chapter": item["chapter"],
            "order": item["order"],
        }
        if item.get("assumes"):
            fm_data["assumes"] = item["assumes"]
        if item.get("introduces"):
            fm_data["introduces"] = item["introduces"]
        if item.get("previews"):
            fm_data["previews"] = item["previews"]
        if item.get("recap_policy"):
            fm_data["recap_policy"] = item["recap_policy"]

        write_frontmatter(chapter_path, fm_data)
        print(f"MIGRATED: {item['path']}")
        migrated += 1

    print(f"\nDone: {migrated} chapter(s) updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
