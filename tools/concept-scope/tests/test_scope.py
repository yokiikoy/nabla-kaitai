"""Tests for chapter scope resolution."""

from concept_scope.scope import load_chapters, scope_for_chapter, infer_chapter, relative_path
from pathlib import Path


class TestLoadChapters:
    def test_loads_all(self, chapters):
        assert len(chapters) >= 10

    def test_chapter_has_order(self, chapters):
        for path, ch in chapters.items():
            assert ch.order > 0

    def test_ch04_exists(self, chapters):
        ch04_path = "manuscript/ja/ch04/ch04.md"
        assert ch04_path in chapters
        assert chapters[ch04_path].id == "ch04"


class TestScopeForChapter:
    def test_ch04_scope(self):
        scope = scope_for_chapter("ch04")
        assert scope.chapter_id == "ch04"
        assert "exterior_derivative" in scope.being_introduced
        assert "hodge_star" in scope.preview_only
        assert "one_form" in scope.available
        assert "maxwell_forms" in scope.preview_only  # ch04 previews maxwell

    def test_ch01_scope(self):
        scope = scope_for_chapter("ch01")
        assert scope.chapter_id == "ch01"
        assert "displacement_vector" in scope.being_introduced
        assert "wedge_product" in scope.preview_only
        assert len(scope.preview_only) >= 10  # Many concepts are previewed
        assert len(scope.forbidden) >= 3  # Some truly not in scope

    def test_ch05_scope_hodge_available(self):
        scope = scope_for_chapter("ch05")
        assert "hodge_star" in scope.being_introduced
        assert "hodge_star" in scope.available

    def test_ch11_scope(self):
        scope = scope_for_chapter("ch11")
        assert "clifford_dirac" in scope.being_introduced
        assert len(scope.forbidden) == 0  # Last chapter, nothing future

    def test_preview_only_detail(self):
        scope = scope_for_chapter("ch04")
        hodge = scope.preview_only["hodge_star"]
        assert isinstance(hodge, dict)
        assert hodge.get("max_level") == "intuition"

    def test_recap_policy(self):
        scope = scope_for_chapter("ch03")
        assert "one_form" in scope.recap_limited
        assert "wedge_product" in scope.recap_limited


class TestInferChapter:
    def test_infer_from_path(self, chapters):
        # relative_path resolves to the absolute path, so a relative path
        # under the current working directory may match the chapters dict key
        c = infer_chapter(Path("/repo/manuscript/ja/ch04/ch04.md"), Path("/repo"), chapters)
        assert c is not None
        assert c.id == "ch04"

    def test_infer_from_frontmatter(self, tmp_path):
        path = tmp_path / "unknown.md"
        path.write_text("---\nchapter: 5\n---\n\ncontent\n")
        c = infer_chapter(path, tmp_path, {})
        assert c is not None
        assert c.id == "ch05"
        assert c.chapter == 5

    def test_infer_none(self, tmp_path):
        path = tmp_path / "random.md"
        path.write_text("just text\n")
        c = infer_chapter(path, tmp_path, {})
        assert c is None


class TestRelativePath:
    def test_relative(self):
        assert relative_path(Path("/repo/a/b.md"), Path("/repo")) == "a/b.md"

    def test_not_under_root(self):
        assert relative_path(Path("/other/a.md"), Path("/repo")).startswith("/other")
