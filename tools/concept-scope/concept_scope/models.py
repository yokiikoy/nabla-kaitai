"""Dataclass models for concept-scope diagnostics."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Diagnostic:
    path: str
    line: int
    column: int
    end_column: int
    severity: str
    code: str
    message: str
    match: str


@dataclass(frozen=True)
class Chapter:
    id: str
    path: str
    chapter: int
    order: int


@dataclass(frozen=True)
class Concept:
    id: str
    label: str
    kind: str
    introduced_in: str
    order: int
    aliases: list[str]
    summary: str


@dataclass(frozen=True)
class ConceptOccurrence:
    """A single usage of a concept at a specific location in text."""

    concept_id: str
    surface: str
    level: str
    line: int
    column: int
    end_column: int


@dataclass(frozen=True)
class ChapterScope:
    """Resolved scope for a chapter: what's allowed, forbidden, etc."""

    chapter_id: str
    order: int
    available: dict[str, str]
    being_introduced: dict[str, dict]
    preview_only: dict[str, dict]
    recap_limited: dict[str, dict]
    forbidden: list[str]
