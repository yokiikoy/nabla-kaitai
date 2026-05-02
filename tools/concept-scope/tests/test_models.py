"""Tests for models dataclasses."""

from concept_scope.models import Diagnostic, Chapter, Concept, ConceptOccurrence, ChapterScope


class TestDiagnostic:
    def test_creation(self):
        d = Diagnostic(path="test.md", line=10, column=5, end_column=10, severity="error", code="T001", message="test", match="dx^2")
        assert d.path == "test.md"
        assert d.line == 10
        assert d.severity == "error"

    def test_frozen(self):
        d = Diagnostic(path="test.md", line=1, column=1, end_column=1, severity="warning", code="X", message="m", match="")
        try:
            d.line = 2
            assert False, "Should not mutate frozen dataclass"
        except Exception:
            pass


class TestChapter:
    def test_creation(self):
        c = Chapter(id="ch04", path="manuscript/ja/ch04/ch04.md", chapter=4, order=40)
        assert c.id == "ch04"
        assert c.chapter == 4
        assert c.order == 40


class TestConcept:
    def test_creation(self):
        c = Concept(
            id="test_concept", label="Test", kind="object",
            introduced_in="ch01", order=10,
            aliases=["test", "Test"], summary="A test concept."
        )
        assert c.id == "test_concept"
        assert len(c.aliases) == 2


class TestConceptOccurrence:
    def test_creation(self):
        o = ConceptOccurrence(
            concept_id="one_form", surface="1-form",
            level="definition", line=42, column=3, end_column=9
        )
        assert o.concept_id == "one_form"
        assert o.level == "definition"


class TestChapterScope:
    def test_creation(self):
        s = ChapterScope(
            chapter_id="ch04", order=40,
            available={"one_form": "computation"},
            being_introduced={"exterior_derivative": {"from": "intuition", "to": "computation"}},
            preview_only={"hodge_star": {"max_level": "intuition"}},
            recap_limited={"wedge_product": {"max_level": "mention", "max_lines": 3}},
            forbidden=["maxwell_forms"],
        )
        assert "one_form" in s.available
        assert "hodge_star" in s.preview_only
        assert "maxwell_forms" in s.forbidden
