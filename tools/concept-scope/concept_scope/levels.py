"""Usage level detection for concept occurrences in Markdown text.

Classifies each occurrence of a concept as one of:
mention, intuition, definition, formula, computation, theorem_use

Heuristic-based: uses TeX math detection, natural language patterns,
surrounding context, annotations, and section roles to approximate
the usage level.
"""

from __future__ import annotations

import re
from typing import Any

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
        r"(?<![ことものの])とは",
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
        r"第\s*\d+\s*章で",
        r"先の章",
        r"のちに",
        r"いずれ",
        r"一種と(みな|見な)",
        r"結実する",
    ]
]

# ── Annotation parsing ─────────────────────────────────────────

_ANNOTATION_ALLOW_LINE_RE = re.compile(
    r"<!--\s*concept-scope:\s*allow\(([^)]*)\)\s*-->"
)
_ANNOTATION_ALLOW_ALL_RE = re.compile(
    r"<!--\s*concept-scope:\s*allow-all\s*-->"
)
_ANNOTATION_END_ALLOW_RE = re.compile(
    r"<!--\s*concept-scope:\s*end-allow(-all)?\s*-->"
)
_ROLE_RE = re.compile(r"<!--\s*role:\s*(\w+)\s*-->")

# Role → max classification level (capped)
_ROLE_CAPS: dict[str, str] = {
    "roadmap": "mention",
    "foreshadowing": "intuition",
}

# Window (chars) around a concept position to check for nearby NLP patterns.
_SURROUNDING_WINDOW = 60
_TIGHT_WINDOW = 20   # for definition/theorem patterns — must be very close


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


def _pattern_near_concept(
    pattern: re.Pattern, line: str, concept_col: int, concept_end_col: int,
    window: int = _SURROUNDING_WINDOW,
) -> bool:
    """Check if pattern matches within `window` chars of the concept."""
    for m in pattern.finditer(line):
        p_start, p_end = m.start(), m.end()
        if (abs(p_start - concept_end_col) <= window or
                abs(concept_col - p_end) <= window):
            return True
    return False


def _any_pattern_near(
    patterns: list[re.Pattern], line: str, concept_col: int, concept_end_col: int,
    window: int = _SURROUNDING_WINDOW,
) -> bool:
    """Check if any pattern in the list matches near the concept."""
    for pat in patterns:
        if _pattern_near_concept(pat, line, concept_col, concept_end_col, window=window):
            return True
    return False


def _any_pattern_on_line(
    patterns: list[re.Pattern], line: str,
) -> bool:
    """Check if any pattern matches anywhere on the line."""
    for pat in patterns:
        if pat.search(line):
            return True
    return False


# ── Level classification ──────────────────────────────────────

def classify_usage_level(
    line: str,
    concept_id: str,
    column: int = 0,
    alias_len: int = 0,
    context_before: list[str] | None = None,
    context_after: list[str] | None = None,
    role: str | None = None,
) -> str:
    """Classify the usage level of a concept mention.

    The `line` is the line containing the mention.
    `column` is the 0-based index where the concept alias starts.
    `alias_len` is the length of the matched alias string.
    `role` is the current section role (roadmap, foreshadowing, etc.).

    Returns one of: mention, intuition, definition, formula, computation, theorem_use.
    """
    concept_end_col = column + alias_len

    # Priority 0: section role forces the classification cap
    # (checked at the end — we compute the raw classification first, then cap it)

    # Priority 1: NLP context patterns take precedence over math detection
    #    because they signal author intent (foreshadowing, definition, etc.)
    #    even when the concept appears inside inline math.

    # Intuition: full-line match — "次章" etc. set the tone for the whole line
    if _any_pattern_on_line(_INTUITION_PATTERNS, line):
        result = "intuition"
    # Definition: must be very close to the concept (±20 chars)
    elif _any_pattern_near(_DEFINITION_PATTERNS, line, column, concept_end_col, window=_TIGHT_WINDOW):
        result = "definition"
    else:
        # Priority 2: if the concept is inside a TeX math environment
        in_math, math_text = _is_in_math(line, column)

        if in_math and math_text:
            if _IS_COMPUTATION_TOKEN.search(math_text):
                result = "computation"
            elif _IS_FORMULA_TOKEN.search(math_text):
                result = "formula"
            else:
                result = "mention"
        else:
            # Priority 3: nearby theorem-use patterns (tight window)
            if _any_pattern_near(_THEOREM_USE_PATTERNS, line, column, concept_end_col, window=_TIGHT_WINDOW):
                result = "theorem_use"
            else:
                result = "mention"

    # Apply role cap
    if role and role in _ROLE_CAPS:
        cap = _ROLE_CAPS[role]
        if _usage_level_order(result) > _usage_level_order(cap):
            result = cap

    return result


def _usage_level_order(level: str) -> int:
    """Map usage level name to ordinal value."""
    order_map = {
        "mention": 1,
        "intuition": 2,
        "definition": 3,
        "formula": 4,
        "computation": 5,
        "theorem_use": 6,
    }
    return order_map.get(level, 0)


# ── Occurrence extraction ─────────────────────────────────────

def extract_occurrences(
    lines: list[tuple[int, str]],
    concepts: list[Concept],
    roles: dict[int, str] | None = None,
) -> list[ConceptOccurrence]:
    """Extract all concept occurrences from a list of (line_no, text) pairs.

    Uses concept aliases for matching and classifies usage level.
    """
    alias_to_id = build_alias_index(concepts)
    occurrences: list[ConceptOccurrence] = []

    for line_no, line in lines:
        line_role = roles.get(line_no) if roles else None
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

                level = classify_usage_level(
                    line, concept_id,
                    column=idx, alias_len=len(alias),
                    context_before=context_before, context_after=context_after,
                    role=line_role,
                )

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


def extract_occurrences_from_text(
    text: str, concepts: list[Concept], roles: dict[int, str] | None = None
) -> list[ConceptOccurrence]:
    """Extract occurrences from a raw text string (no file path)."""
    lines = text.splitlines()
    line_pairs = [(i + 1, line) for i, line in enumerate(lines)]
    return extract_occurrences(line_pairs, concepts, roles=roles)


# ── Annotation / role parsing ─────────────────────────────────

def _clean_line(line: str) -> str:
    """Strip blockquote markers and whitespace from a markdown line."""
    s = line.strip()
    while s.startswith(">"):
        s = s[1:].strip()
    return s


def parse_allow_annotations(
    checkable: list[tuple[int, str]],
) -> tuple[dict[int, set[str]], set[int]]:
    """Parse concept-scope allow annotations from checkable lines.

    Supported forms:
      <!-- concept-scope: allow(id1, id2) -->   → applies to the NEXT line
      <!-- concept-scope: allow-all -->          → start of allow-all block
      <!-- concept-scope: end-allow-all -->      → end of allow-all block
      <!-- concept-scope: end-allow -->          → end of allow block

    Returns:
        allowed_on_line: dict line_no -> set of concept_ids to allow on that line
        allow_all_lines: set of line numbers where all checks are suppressed
    """
    allowed_on_line: dict[int, set[str]] = {}
    allow_all_lines: set[int] = set()

    # First pass: identify annotation lines and their types
    ann_lines: dict[int, tuple] = {}  # line_no -> (type, detail)
    for line_no, line in checkable:
        stripped = _clean_line(line)

        m = _ANNOTATION_ALLOW_LINE_RE.match(stripped)
        if m:
            raw = m.group(1).strip()
            if raw:
                ids = {c.strip() for c in raw.split(",") if c.strip()}
            else:
                ids = set()
            ann_lines[line_no] = ("allow", ids)
            continue

        if _ANNOTATION_ALLOW_ALL_RE.match(stripped):
            ann_lines[line_no] = ("allow_all", None)
            continue

        if _ANNOTATION_END_ALLOW_RE.match(stripped):
            ann_lines[line_no] = ("end", None)
            continue

    # Second pass: apply single-line annotations to the following line
    # and track allow-all block ranges
    in_allow_all = False
    sorted_lines = sorted(checkable, key=lambda x: x[0])
    for i, (line_no, line) in enumerate(sorted_lines):
        if line_no in ann_lines:
            info = ann_lines[line_no]
            if info[0] == "allow":
                # Apply to the next non-annotation line
                for j in range(i + 1, len(sorted_lines)):
                    next_ln = sorted_lines[j][0]
                    if next_ln not in ann_lines:
                        allowed_on_line.setdefault(next_ln, set()).update(info[1])
                        break
            elif info[0] == "allow_all":
                in_allow_all = True
            elif info[0] == "end":
                in_allow_all = False
            continue

        if in_allow_all:
            allow_all_lines.add(line_no)

    return allowed_on_line, allow_all_lines


def parse_roles(
    checkable: list[tuple[int, str]],
) -> dict[int, str]:
    """Parse role annotations and return line_no -> role mapping.

    Supported forms:
      <!-- role: roadmap -->        (standalone)
      ## Heading <!-- role: recap -->  (inline in heading)
    """
    roles: dict[int, str] = {}
    current_role: str | None = None

    for line_no, line in checkable:
        m = _ROLE_RE.search(line)
        if m:
            current_role = m.group(1)
        if current_role is not None:
            roles[line_no] = current_role

    return roles
