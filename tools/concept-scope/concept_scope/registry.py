"""Concept registry: loads CONCEPTS.yaml into structured data."""

from __future__ import annotations

import re
from typing import Any

from concept_scope.config import CONFIG_DIR, get_concepts_path, load_yaml
from concept_scope.models import Concept


def load_concepts(language: str = "ja") -> list[Concept]:
    data = load_yaml(get_concepts_path(language))
    concepts: list[Concept] = []
    for item in data.get("concepts", []):
        concepts.append(
            Concept(
                id=str(item["id"]),
                label=str(item["label"]),
                kind=str(item["kind"]),
                introduced_in=str(item["introduced_in"]),
                order=int(item["order"]),
                aliases=[str(a) for a in item.get("aliases", [])],
                summary=str(item.get("summary", "")),
            )
        )
    return concepts


def build_concept_index(concepts: list[Concept]) -> dict[str, Concept]:
    """Build a lookup dict from concept_id -> Concept."""
    return {c.id: c for c in concepts}


def build_alias_index(concepts: list[Concept]) -> dict[str, str]:
    """Build a lookup dict from alias text -> concept_id.

    Longer aliases come first to ensure greedy matching.
    """
    pairs = []
    for concept in concepts:
        for alias in concept.aliases:
            pairs.append((alias, concept.id))
    pairs.sort(key=lambda x: len(x[0]), reverse=True)
    return dict(pairs)
