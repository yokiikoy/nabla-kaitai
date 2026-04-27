"""Concept scope tool package."""

from concept_scope.models import (
    Chapter,
    ChapterScope,
    Concept,
    ConceptOccurrence,
    Diagnostic,
)
from concept_scope.config import REPO_ROOT, CONFIG_DIR, load_yaml
from concept_scope.registry import (
    build_alias_index,
    build_concept_index,
    load_concepts,
)
from concept_scope.rules import (
    active_rule,
    allowed_by_context,
    compile_rules,
    usage_level_value,
)
from concept_scope.scope import (
    infer_chapter,
    load_chapters,
    load_chapters_list,
    relative_path,
    scope_for_chapter,
)
from concept_scope.frontmatter import (
    get_frontmatter_chapter,
    get_frontmatter_scope,
    read_frontmatter,
)
from concept_scope.checker import (
    check_file,
    check_text,
    default_files,
    iter_checkable_lines,
    iter_checkable_lines_from_text,
    render_text,
)

from concept_scope.levels import classify_usage_level, extract_occurrences, extract_occurrences_from_text
from concept_scope.context import export_context_json, export_context_markdown

__all__ = [
    "Chapter",
    "ChapterScope",
    "Concept",
    "ConceptOccurrence",
    "Diagnostic",
    "REPO_ROOT",
    "CONFIG_DIR",
    "load_yaml",
    "build_alias_index",
    "build_concept_index",
    "load_concepts",
    "active_rule",
    "allowed_by_context",
    "compile_rules",
    "usage_level_value",
    "infer_chapter",
    "load_chapters",
    "load_chapters_list",
    "relative_path",
    "scope_for_chapter",
    "get_frontmatter_chapter",
    "get_frontmatter_scope",
    "read_frontmatter",
    "check_file",
    "check_text",
    "default_files",
    "iter_checkable_lines",
    "iter_checkable_lines_from_text",
    "render_text",
    "classify_usage_level",
    "extract_occurrences",
    "extract_occurrences_from_text",
    "export_context_json",
    "export_context_markdown",
]
