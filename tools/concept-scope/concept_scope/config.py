"""Configuration and YAML loading utilities."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_DIR = REPO_ROOT / "docs" / "concept-scope"


def get_concepts_path(language: str = "ja") -> Path:
    """Return the path to the concepts registry for the given language."""
    if language == "en":
        return CONFIG_DIR / "CONCEPTS_EN.yaml"
    return CONFIG_DIR / "CONCEPTS.yaml"


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return data
