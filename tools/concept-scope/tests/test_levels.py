"""Tests for usage level classification and occurrence extraction."""

from concept_scope.levels import (
    classify_usage_level,
    extract_occurrences,
    extract_occurrences_from_text,
)
from concept_scope.models import Concept


SAMPLE_CONCEPTS = [
    Concept(id="one_form", label="1-form", kind="object", introduced_in="ch01", order=10,
            aliases=["1-form", "一次形式"], summary="ベクトルを食べる測定器"),
    Concept(id="wedge_product", label="ウェッジ積", kind="operation", introduced_in="ch02", order=20,
            aliases=["ウェッジ積", "\\wedge", "外積"], summary="反対称積"),
    Concept(id="exterior_derivative", label="外微分", kind="operator", introduced_in="ch04", order=40,
            aliases=["外微分", "d"], summary="d operator"),
    Concept(id="hodge_star", label="ホッジ・スター", kind="operator", introduced_in="ch05", order=50,
            aliases=["ホッジ・スター", "\\ast", "*"], summary="Hodge star"),
]


class TestClassifyUsageLevel:
    def test_mention_in_prose(self):
        level = classify_usage_level("ここで外微分を考える。", "exterior_derivative")
        assert level in ("mention", "intuition")

    def test_definition_pattern(self):
        level = classify_usage_level("ウェッジ積とは、2つの1-formから反対称に積を取る操作である。", "wedge_product")
        assert level == "definition"

    def test_intuition_pattern(self):
        level = classify_usage_level("これは次章で直感的に説明する。", "hodge_star")
        assert level == "intuition"

    def test_formula_in_math(self):
        level = classify_usage_level("$\\ast(dx) = dy \\wedge dz$", "hodge_star")
        assert level in ("formula", "computation")  # = triggers computation

    def test_theorem_use_pattern(self):
        level = classify_usage_level("定理より導かれる", "stokes_theorem")
        assert level == "theorem_use"

    def test_computation_in_math(self):
        level = classify_usage_level("$\\int_M d\\omega$", "exterior_derivative")
        assert level in ("computation", "formula")


class TestExtractOccurrences:
    def test_find_single_alias(self):
        lines = [(1, "ホッジ・スターは後で定義する。")]
        occs = extract_occurrences(lines, SAMPLE_CONCEPTS)
        assert len(occs) >= 1
        hodge = [o for o in occs if o.concept_id == "hodge_star"]
        assert len(hodge) >= 1
        # "定義" appears in the text so definition wins over intuition
        assert hodge[0].level in ("definition", "intuition")

    def test_find_multiple(self):
        lines = [
            (1, "ウェッジ積とは反対称な積である。"),
            (2, "外微分はそれを $d\\omega$ とする。"),
        ]
        occs = extract_occurrences(lines, SAMPLE_CONCEPTS)
        wedge = [o for o in occs if o.concept_id == "wedge_product"]
        ext = [o for o in occs if o.concept_id == "exterior_derivative"]
        assert len(wedge) >= 1
        assert len(ext) >= 1

    def test_positions_are_correct(self):
        lines = [(1, "aaa ホッジ・スター bbb")]
        occs = extract_occurrences(lines, SAMPLE_CONCEPTS)
        hodge = [o for o in occs if o.concept_id == "hodge_star"]
        assert len(hodge) >= 1
        assert hodge[0].column > 1

    def test_empty_lines(self):
        occs = extract_occurrences([], SAMPLE_CONCEPTS)
        assert len(occs) == 0

    def test_no_matches(self):
        lines = [(1, "関係ない文章")]
        occs = extract_occurrences(lines, SAMPLE_CONCEPTS)
        assert len(occs) == 0


class TestExtractOccurrencesFromText:
    def test_simple(self):
        text = "1-form と ウェッジ積 について考える。"
        occs = extract_occurrences_from_text(text, SAMPLE_CONCEPTS)
        assert len(occs) >= 2


class TestLineContext:
    def test_context_match(self):
        from concept_scope.checker import _check_line_context
        line_map = {
            10: "次章で定義する",
            11: "$\\ast(dx)$",
            12: "後で使う",
        }
        assert _check_line_context(11, line_map, ["次章", "後で"]) is True

    def test_context_no_match(self):
        from concept_scope.checker import _check_line_context
        line_map = {
            10: "普通の文章",
            11: "$\\ast(dx)$",
            12: "さらに計算",
        }
        assert _check_line_context(11, line_map, ["次章", "後で"]) is False

    def test_context_empty_patterns(self):
        from concept_scope.checker import _check_line_context
        line_map = {10: "text"}
        assert _check_line_context(10, line_map, []) is False
