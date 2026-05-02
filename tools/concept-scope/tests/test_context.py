"""Tests for LLM context export."""

import json
from concept_scope.context import export_context_markdown, export_context_json


class TestExportContextMarkdown:
    def test_includes_sections(self):
        md = export_context_markdown("ch04")
        assert "使用可能な概念" in md
        assert "伏線のみ許可" in md
        assert "再説明禁止" in md
        assert "使用禁止" in md
        assert "恒久記法制約" in md

    def test_ch04_has_exterior_derivative(self):
        md = export_context_markdown("ch04")
        assert "exterior_derivative" in md
        assert "hodge_star" in md
        assert "maxwell_forms" in md

    def test_ch01_has_wedge_as_preview(self):
        md = export_context_markdown("ch01")
        assert "wedge_product" in md

    def test_returns_string(self):
        md = export_context_markdown("ch05")
        assert isinstance(md, str)
        assert len(md) > 100


class TestExportContextJson:
    def test_valid_json(self):
        data = export_context_json("ch04")
        assert isinstance(data, dict)
        assert "chapter" in data
        assert "available" in data
        assert "preview_only" in data
        assert "recap_limited" in data
        assert "forbidden" in data
        assert "notation_contracts" in data

    def test_ch04_json(self):
        data = export_context_json("ch04")
        assert data["chapter"] == "ch04"
        available_ids = [a["id"] for a in data["available"]]
        assert "exterior_derivative" in available_ids
        preview_ids = [p["id"] for p in data["preview_only"]]
        assert "hodge_star" in preview_ids

    def test_json_serializable(self):
        data = export_context_json("ch07")
        json_str = json.dumps(data, ensure_ascii=False)
        assert len(json_str) > 100

    def test_last_chapter_no_forbidden(self):
        data = export_context_json("ch11")
        assert len(data["forbidden"]) == 0
