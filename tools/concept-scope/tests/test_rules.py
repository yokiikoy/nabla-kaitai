"""Tests for rule compilation and activation."""

from concept_scope.rules import compile_rules, active_rule, allowed_by_context, usage_level_value
from concept_scope.models import Chapter


class TestCompileRules:
    def test_compiles_all_rules(self):
        rules = compile_rules()
        assert len(rules) >= 8
        for rule in rules:
            assert "_patterns" in rule
            assert isinstance(rule.get("_patterns"), list)
            assert len(rule["_patterns"]) > 0

    def test_rule_has_id_and_severity(self):
        rules = compile_rules()
        for rule in rules:
            assert "id" in rule
            assert "severity" in rule


class TestActiveRule:
    def test_applies_to_all(self):
        rule = {"applies_to": "all", "id": "test"}
        assert active_rule(rule, None) is True
        assert active_rule(rule, Chapter(id="ch04", path="x", chapter=4, order=40)) is True

    def test_chapter_before(self):
        rule = {"chapter_before": 5, "id": "test"}
        ch03 = Chapter(id="ch03", path="x", chapter=3, order=30)
        ch06 = Chapter(id="ch06", path="x", chapter=6, order=60)
        assert active_rule(rule, ch03) is True
        assert active_rule(rule, ch06) is False

    def test_chapter_after(self):
        rule = {"after_chapter": 2, "id": "test"}
        ch03 = Chapter(id="ch03", path="x", chapter=3, order=30)
        ch01 = Chapter(id="ch01", path="x", chapter=1, order=10)
        assert active_rule(rule, ch03) is True
        assert active_rule(rule, ch01) is False

    def test_no_chapter_still_active(self):
        rule = {"chapter_before": 5, "id": "test"}
        assert active_rule(rule, None) is True

    def test_before_chapter(self):
        rule = {"before_chapter": 4, "id": "test"}
        ch03 = Chapter(id="ch03", path="x", chapter=3, order=30)
        ch05 = Chapter(id="ch05", path="x", chapter=5, order=50)
        assert active_rule(rule, ch03) is True
        assert active_rule(rule, ch05) is False


class TestAllowedByContext:
    def test_empty_patterns(self):
        rule = {"_allowed_context_patterns": []}
        assert allowed_by_context(rule, "any text") is False

    def test_matching_context(self):
        import re
        rule = {"_allowed_context_patterns": [re.compile(r"次章"), re.compile(r"後で")]}
        assert allowed_by_context(rule, "次章で導入する") is True

    def test_non_matching_context(self):
        import re
        rule = {"_allowed_context_patterns": [re.compile(r"次章")]}
        assert allowed_by_context(rule, "普通の文章") is False


class TestUsageLevelValue:
    def test_order(self):
        assert usage_level_value("mention") < usage_level_value("intuition")
        assert usage_level_value("intuition") < usage_level_value("definition")
        assert usage_level_value("definition") < usage_level_value("formula")
        assert usage_level_value("formula") < usage_level_value("computation")
        assert usage_level_value("computation") < usage_level_value("theorem_use")

    def test_unknown(self):
        assert usage_level_value("nonexistent") == 0
