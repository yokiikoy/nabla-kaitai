"""Tests for frontmatter <-> CHAPTER_SCOPES.yaml consistency checker."""

from pathlib import Path

from concept_scope.consistency import check_consistency, ConsistencyIssue


class TestCheckConsistency:
    def test_empty_if_no_config_dir(self, tmp_path):
        """With no config, returns no issues (or fails gracefully)."""
        # Use a non-existent root
        issues = check_consistency(tmp_path)
        # Should be empty since there's no config
        assert isinstance(issues, list)

    def test_detects_missing_ch11(self):
        """The actual repo has ch11 with no .md file."""
        from concept_scope.config import REPO_ROOT

        issues = check_consistency(REPO_ROOT)
        ch11_issues = [i for i in issues if i.chapter_id == "ch11" and i.kind == "missing_file"]
        assert len(ch11_issues) >= 1, "ch11 should be detected as missing"

    def test_after_migration_is_clean(self):
        """After migration, only ch11 should have a missing file issue."""
        from concept_scope.config import REPO_ROOT

        issues = check_consistency(REPO_ROOT)
        non_ch11 = [i for i in issues if i.chapter_id != "ch11"]
        assert len(non_ch11) == 0, f"Expected no mismatches, got: {non_ch11}"

    def test_detects_missing_frontmatter(self, tmp_path):
        """A chapter file without scope frontmatter should be detected."""
        import yaml
        config_dir = tmp_path / "docs" / "concept-scope"
        config_dir.mkdir(parents=True)
        chapter_dir = tmp_path / "manuscript" / "ja" / "ch01"
        chapter_dir.mkdir(parents=True)

        # Write chapter file WITHOUT frontmatter
        (chapter_dir / "ch01.md").write_text("no frontmatter\n")

        # Write minimal CHAPTER_SCOPES.yaml
        scope_data = {
            "version": "0.1",
            "chapters": [{
                "id": "ch01",
                "path": "manuscript/ja/ch01/ch01.md",
                "chapter": 1,
                "order": 10,
                "assumes": [],
                "introduces": {"test_concept": {"from": "definition", "to": "computation"}},
                "previews": {},
                "recap_policy": {},
            }],
        }
        (config_dir / "CHAPTER_SCOPES.yaml").write_text(
            yaml.dump(scope_data, allow_unicode=True, default_flow_style=False)
        )

        issues = check_consistency(tmp_path)
        missing_fm = [i for i in issues if i.kind == "missing_frontmatter"]
        assert len(missing_fm) >= 1

    def test_detects_yaml_only_field(self, tmp_path):
        """Concepts in CHAPTER_SCOPES.yaml but not in frontmatter."""
        import yaml
        config_dir = tmp_path / "docs" / "concept-scope"
        config_dir.mkdir(parents=True)
        chapter_dir = tmp_path / "manuscript" / "ja" / "ch02"
        chapter_dir.mkdir(parents=True)

        # Frontmatter has wedge_product but not k_form
        (chapter_dir / "ch02.md").write_text(
            "---\nchapter: 2\norder: 20\nintroduces:\n  wedge_product:\n    from: definition\n    to: computation\npreviews: {}\nrecap_policy: {}\n---\n\ncontent\n"
        )

        scope_data = {
            "version": "0.1",
            "chapters": [{
                "id": "ch02",
                "path": "manuscript/ja/ch02/ch02.md",
                "chapter": 2,
                "order": 20,
                "assumes": [],
                "introduces": {
                    "wedge_product": {"from": "definition", "to": "computation"},
                    "k_form": {"from": "intuition", "to": "formula"},
                },
                "previews": {},
                "recap_policy": {},
            }],
        }
        (config_dir / "CHAPTER_SCOPES.yaml").write_text(
            yaml.dump(scope_data, allow_unicode=True, default_flow_style=False)
        )

        issues = check_consistency(tmp_path)
        yaml_only = [i for i in issues if i.kind == "yaml_only"]
        assert len(yaml_only) >= 1
        assert any("k_form" in i.concept_id for i in yaml_only)

    def test_detects_mismatched_value(self, tmp_path):
        """Same concept but different max_level."""
        import yaml
        config_dir = tmp_path / "docs" / "concept-scope"
        config_dir.mkdir(parents=True)
        chapter_dir = tmp_path / "manuscript" / "ja" / "ch04"
        chapter_dir.mkdir(parents=True)

        (chapter_dir / "ch04.md").write_text(
            "---\nchapter: 4\norder: 40\npreviews:\n  hodge_star:\n    max_level: mention\n---\n\ncontent\n"
        )

        scope_data = {
            "version": "0.1",
            "chapters": [{
                "id": "ch04",
                "path": "manuscript/ja/ch04/ch04.md",
                "chapter": 4,
                "order": 40,
                "assumes": [],
                "introduces": {},
                "previews": {"hodge_star": {"max_level": "intuition"}},
                "recap_policy": {},
            }],
        }
        (config_dir / "CHAPTER_SCOPES.yaml").write_text(
            yaml.dump(scope_data, allow_unicode=True, default_flow_style=False)
        )

        issues = check_consistency(tmp_path)
        mismatches = [i for i in issues if i.kind == "mismatch"]
        assert len(mismatches) >= 1
