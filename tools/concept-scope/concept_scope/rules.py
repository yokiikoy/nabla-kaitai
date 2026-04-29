"""Rule compilation and activation logic from RULES.yaml."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from concept_scope.config import CONFIG_DIR, load_yaml
from concept_scope.models import Chapter

_USAGE_LEVEL_ORDER = {
    "mention": 1,
    "intuition": 2,
    "definition": 3,
    "formula": 4,
    "computation": 5,
    "theorem_use": 6,
}


def compile_rules(config_dir: str | Path | None = None) -> list[dict[str, Any]]:
    if config_dir is None:
        config_dir = CONFIG_DIR
    if isinstance(config_dir, str):
        config_dir = Path(config_dir)
    path = config_dir / "RULES.yaml"
    data = load_yaml(path)
    compiled: list[dict[str, Any]] = []
    for rule in data.get("rules", []):
        item = dict(rule)
        item["_patterns"] = [
            re.compile(pattern) for pattern in item.get("patterns", [])
        ]
        item["_allowed_context_patterns"] = [
            re.compile(pattern) for pattern in item.get("allowed_context_patterns", [])
        ]
        if "after_heading_pattern" in item:
            item["_after_heading_pattern"] = re.compile(item["after_heading_pattern"])
        compiled.append(item)
    return compiled


def active_rule(rule: dict[str, Any], chapter: Chapter | None) -> bool:
    if rule.get("applies_to") == "all":
        return True
    if chapter is None:
        return True

    if "chapter_before" in rule and not (chapter.chapter < int(rule["chapter_before"])):
        return False
    if "chapter_after" in rule and not (chapter.chapter > int(rule["chapter_after"])):
        return False
    if "after_chapter" in rule and not (chapter.chapter > int(rule["after_chapter"])):
        return False
    if "before_chapter" in rule and not (chapter.chapter < int(rule["before_chapter"])):
        return False
    return True


def allowed_by_context(rule: dict[str, Any], line: str) -> bool:
    return any(
        pattern.search(line)
        for pattern in rule.get("_allowed_context_patterns", [])
    )


def usage_level_value(level: str) -> int:
    return _USAGE_LEVEL_ORDER.get(level, 0)
