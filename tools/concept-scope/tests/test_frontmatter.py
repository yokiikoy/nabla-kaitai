"""Tests for frontmatter parsing."""

import yaml
from concept_scope.frontmatter import (
    read_frontmatter,
    get_frontmatter_chapter,
    get_frontmatter_scope,
)


class TestReadFrontmatter:
    def test_no_frontmatter(self, tmp_path):
        path = tmp_path / "no.md"
        path.write_text("just text\n")
        assert read_frontmatter(path) is None

    def test_valid_frontmatter(self, tmp_path):
        path = tmp_path / "has.md"
        path.write_text("---\nchapter: 1\ntitle: Test\n---\n\nbody\n")
        fm = read_frontmatter(path)
        assert fm is not None
        assert fm["chapter"] == 1
        assert fm["title"] == "Test"

    def test_empty_frontmatter(self, tmp_path):
        path = tmp_path / "empty.md"
        path.write_text("---\n---\n\nbody\n")
        fm = read_frontmatter(path)
        assert fm == {} or fm is None

    def test_broken_frontmatter(self, tmp_path):
        path = tmp_path / "broken.md"
        path.write_text("---\nchapter: 1\n---\n---\nbad\n")
        fm = read_frontmatter(path)
        assert fm is not None
        assert fm["chapter"] == 1


class TestGetFrontmatterChapter:
    def test_extracts_chapter(self, tmp_path):
        path = tmp_path / "ch03.md"
        path.write_text("---\nchapter: 3\n---\n\ncontent\n")
        assert get_frontmatter_chapter(path) == 3

    def test_no_chapter(self, tmp_path):
        path = tmp_path / "nochap.md"
        path.write_text("---\ntitle: Hello\n---\n\ncontent\n")
        assert get_frontmatter_chapter(path) is None


class TestGetFrontmatterScope:
    def test_extracts_scope(self, tmp_path):
        path = tmp_path / "scoped.md"
        fm = {
            "chapter": 4, "order": 40,
            "assumes": ["one_form"],
            "introduces": {"exterior_derivative": {"from": "intuition", "to": "computation"}},
            "previews": {"hodge_star": {"max_level": "intuition"}},
            "recap_policy": {"wedge_product": {"max_level": "mention", "max_lines": 3}},
        }
        yaml_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False).strip()
        path.write_text(f"---\n{yaml_str}\n---\n\ncontent\n")
        scope = get_frontmatter_scope(path)
        assert scope is not None
        assert scope["chapter"] == 4
        assert "exterior_derivative" in scope["introduces"]
        assert "hodge_star" in scope["previews"]
        assert "wedge_product" in scope["recap_policy"]

    def test_no_scope_fields(self, tmp_path):
        path = tmp_path / "noscope.md"
        path.write_text("---\ntitle: Just a Title\n---\n\ncontent\n")
        scope = get_frontmatter_scope(path)
        assert scope is None
