"""Usage level detection for concept occurrences in Markdown text.

Classifies each occurrence of a concept as one of:
mention, intuition, definition, formula, computation, theorem_use

Heuristic-based: uses TeX math detection, natural language patterns,
and surrounding context to approximate the usage level.
"""

from __future__ import annotations

import re

from concept_scope.models import Concept, ConceptOccurrence
from concept_scope.registry import build_alias_index

# ── TeX math environment detection ──────────────────────────────

_INLINE_MATH_RE = re.compile(r"(?<!\\)\$(.+?)(?<!\\)\$")
_DISPLAY_MATH_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
_BRACKET_MATH_RE = re.compile(r"\\\[(.+?)\\\]", re.DOTALL)
_ALIGN_RE = re.compile(
    r"\\begin\{(align|equation|eqnarray|gather|multline)\*?\}"
)

_IS_FORMULA_TOKEN = re.compile(
    r"\\int|\\sum|\\prod|\\oint|\\iint|\\iiint|\\frac|\\\\|\\sqrt|\\partial"
    r"|\\nabla|\\mathbf|\\left|\\right|\\ast|\\wedge|="
)
_IS_COMPUTATION_TOKEN = re.compile(
    r"\\int|\\sum|\\prod|="
)

# ── Natural language definition patterns ──────────────────────

_DEFINITION_PATTERNS = [
    re.compile(p) for p in [
        r"とは",
        r"と定義",
        r"と呼ぶ",
        r"を次(のよう)?に(定義|定める|おく)",
        r"で(定義|定める)",
    ]
]

_THEOREM_USE_PATTERNS = [
    re.compile(p) for p in [
        r"(定理|法則|公式).*より",
        r"(定理|法則|公式).*から",
        r"(定理|法則|公式).*を用い",
        r"(定理|法則|公式).*を使",
        r"より",
        r"に(より|よって|よれば)",
        r"から(直ちに)?(従|したが)",
    ]
]

_INTUITION_PATTERNS = [
    re.compile(p) for p in [
        r"直感的",
        r"イメージ",
        r"たとえ",
        r"あたかも",
        r"将来的",
        r"後の章",
        r"次章",
        r"後で",
        r"後述",
        r"伏線",
    ]
]

# ── Level classification ──────────────────────────────────────

def _is_in_math(text: str, column: int) -> tuple[bool, str]:
    """Check if position is inside a TeX math environment.

    Returns (is_in_math, math_text_or_empty).
    """
    # Check inline math
    for m in re.finditer(r"(?<!\\)\$[^$]+(?<!\\)\$", text):
        if m.start() <= column < m.end():
            return True, m.group(0)
    # Check display math
    for m in re.finditer(r"\$\$.*?\$\$", text):
        if m.start() <= column < m.end():
            return True, m.group(0)
    for m in re.finditer(r"\\\[.*?\\\]", text):
        if m.start() <= column < m.end():
            return True, m.group(0)
    return False, ""


def classify_usage_level(
    line: str,
    concept_id: str,
    context_before: list[str] | None = None,
    context_after: list[str] | None = None,
) -> str:
    """Classify the usage level of a concept mention.

    The `line` is the line containing the mention.
    `context_before`/`context_after` are surrounding lines for pattern analysis.

    Returns one of: mention, intuition, definition, formula, computation, theorem_use.
    """
    in_math, math_text = _is_in_math(line, len(line) // 2)

    if in_math and math_text:
        if _IS_COMPUTATION_TOKEN.search(math_text):
            return "computation"
        return "formula"

    for pat in _DEFINITION_PATTERNS:
        if pat.search(line):
            return "definition"

    for pat in _INTUITION_PATTERNS:
        if pat.search(line):
            return "intuition"

    for pat in _THEOREM_USE_PATTERNS:
        if pat.search(line):
            return "theorem_use"

    if in_math:
        return "mention"

    # Default: if the line is just prose mentioning a concept, it's a mention
    return "mention"


def extract_occurrences(lines: list[tuple[int, str]], concepts: list[Concept]) -> list[ConceptOccurrence]:
    """Extract all concept occurrences from a list of (line_no, text) pairs.

    Uses concept aliases for matching and classifies usage level.
    """
    alias_to_id = build_alias_index(concepts)
    occurrences: list[ConceptOccurrence] = []

    for line_no, line in lines:
        for alias, concept_id in alias_to_id.items():
            idx = 0
            while True:
                idx = line.find(alias, idx)
                if idx == -1:
                    break

                # Get surrounding context (adjacent lines)
                context_before = []
                context_after = []
                for lno, ltxt in lines:
                    if lno == line_no - 1:
                        context_before.append(ltxt)
                    elif lno == line_no + 1:
                        context_after.append(ltxt)

                level = classify_usage_level(line, concept_id, context_before, context_after)

                occurrences.append(
                    ConceptOccurrence(
                        concept_id=concept_id,
                        surface=alias,
                        level=level,
                        line=line_no,
                        column=idx + 1,
                        end_column=idx + len(alias) + 1,
                    )
                )
                idx += len(alias)

    return occurrences


def extract_occurrences_from_text(text: str, concepts: list[Concept]) -> list[ConceptOccurrence]:
    """Extract occurrences from a raw text string (no file path)."""
    lines = text.splitlines()
    line_pairs = [(i + 1, line) for i, line in enumerate(lines)]
    return extract_occurrences(line_pairs, concepts)
