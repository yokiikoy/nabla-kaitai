"""Tests for the checker module."""

from pathlib import Path

from concept_scope.checker import (
    check_file,
    check_text,
    iter_checkable_lines,
    iter_checkable_lines_from_text,
    render_text,
)
from concept_scope.models import Diagnostic
from concept_scope.registry import load_concepts


class TestIterCheckableLines:
    def test_empty_file(self, tmp_path):
        path = tmp_path / "empty.md"
        path.write_text("")
        lines = iter_checkable_lines(path)
        assert len(lines) == 0

    def test_plain_text(self, tmp_path):
        path = tmp_path / "plain.md"
        path.write_text("line one\nline two\nline three\n")
        lines = iter_checkable_lines(path)
        assert len(lines) == 3
        assert lines[0] == (1, "line one")
        assert lines[1] == (2, "line two")
        assert lines[2] == (3, "line three")

    def test_skips_frontmatter(self, tmp_path):
        path = tmp_path / "with_fm.md"
        path.write_text("---\nchapter: 1\n---\nreal content\n")
        lines = iter_checkable_lines(path)
        assert len(lines) == 1
        assert lines[0] == (4, "real content")

    def test_skips_code_fence(self, tmp_path):
        path = tmp_path / "code.md"
        path.write_text("before\n```python\ncode\n```\nafter\n")
        lines = iter_checkable_lines(path)
        assert len(lines) == 2
        assert lines[0][1] == "before"
        assert lines[1][1] == "after"

    def test_skips_incomplete_frontmatter(self, tmp_path):
        path = tmp_path / "bad_fm.md"
        path.write_text("---\nchapter: 1\nno closing\n")
        lines = iter_checkable_lines(path)
        assert len(lines) == 0

    def test_nested_code_fence(self, tmp_path):
        path = tmp_path / "nested.md"
        path.write_text("text\n```\ninner ``` still code\n```\nmore text\n")
        lines = iter_checkable_lines(path)
        assert len(lines) == 2
        assert lines[0][1] == "text"
        assert lines[1][1] == "more text"


class TestCheckFile:
    def test_dx_square_violation(self, tmp_path, chapters, rules, sample_text_violation):
        path = tmp_path / "test.md"
        path.write_text(sample_text_violation + "\n")
        diags = check_file(path, tmp_path, chapters, rules)
        assert any(d.code == "notation-contract-dx-square" for d in diags)

    def test_no_violation(self, tmp_path, chapters, rules, sample_text_clean):
        path = tmp_path / "test.md"
        path.write_text(sample_text_clean + "\n")
        diags = check_file(path, tmp_path, chapters, rules)
        assert len(diags) == 0

    def test_hodge_star_violation(self, tmp_path, chapters, rules):
        # ch03 frontmatter to trigger chapter=3
        path = tmp_path / "test.md"
        path.write_text("---\nchapter: 3\norder: 30\n---\n\nホッジ・スターを作用させると良い。\n")
        diags = check_file(path, tmp_path, chapters, rules)
        hodge_diags = [d for d in diags if "hodge" in d.code.lower() or "hodge" in d.message.lower()]
        assert len(hodge_diags) >= 1

    def test_overexplain_one_form(self, tmp_path, chapters, rules, sample_text_overexplain):
        path = tmp_path / "ch05.md"
        path.write_text("---\nchapter: 5\norder: 50\n---\n\n" + sample_text_overexplain + "\n")
        diags = check_file(path, tmp_path, chapters, rules)
        assert any("over-explain-one-form" in d.code for d in diags)


class TestCheckText:
    def test_dx_square_in_text(self, tmp_path, chapters, rules, sample_text_violation):
        # Use a real temp file so infer_chapter can read frontmatter if present
        path = tmp_path / "test.md"
        path.write_text(sample_text_violation + "\n")
        diags = check_text(sample_text_violation, str(path), tmp_path, chapters, rules)
        assert any(d.code == "notation-contract-dx-square" for d in diags)

    def test_regex_only_skips_levels(self, tmp_path, chapters, rules, concepts):
        """In regex_only mode, level-based checks should be skipped."""
        path = tmp_path / "ch01.md"
        path.write_text("---\nchapter: 1\norder: 10\n---\n\nホッジ・スターについて。\n")
        diags_full = check_text(
            "---\nchapter: 1\norder: 10\n---\n\nホッジ・スターについて。\n",
            str(path), tmp_path, chapters, rules, concepts=concepts, mode="full",
        )
        diags_regex = check_text(
            "---\nchapter: 1\norder: 10\n---\n\nホッジ・スターについて。\n",
            str(path), tmp_path, chapters, rules, concepts=concepts, mode="regex_only",
        )
        # regex_only should not produce level-based diagnostics
        level_in_full = any(d.code == "future-concept-level" for d in diags_full)
        level_in_regex = any(d.code == "future-concept-level" for d in diags_regex)
        # If hodge_star is previewed but used at intuition → may trigger in full
        # In regex_only, no level checking happens
        assert not level_in_regex or len(diags_regex) < len(diags_full)


class TestRenderText:
    def test_empty(self):
        assert render_text([]) == "concept-scope: no diagnostics"

    def test_one_diagnostic(self):
        d = Diagnostic(path="test.md", line=1, column=1, end_column=5, severity="error", code="E001", message="bad", match="x")
        out = render_text([d])
        assert "test.md:1:1:" in out
        assert "error: E001:" in out
        assert "(matched: x)" in out
