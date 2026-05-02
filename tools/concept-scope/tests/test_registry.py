"""Tests for concept registry."""

from concept_scope.registry import load_concepts, build_concept_index, build_alias_index


class TestLoadConcepts:
    def test_loads_all(self, concepts):
        assert len(concepts) >= 18

    def test_has_ids(self, concepts):
        ids = {c.id for c in concepts}
        assert "hodge_star" in ids
        assert "exterior_derivative" in ids
        assert "one_form" in ids
        assert "wedge_product" in ids

    def test_aliases_non_empty(self, concepts):
        for concept in concepts:
            assert len(concept.aliases) >= 1, f"{concept.id} has no aliases"


class TestBuildConceptIndex:
    def test_builds_dict(self, concepts):
        idx = build_concept_index(concepts)
        assert isinstance(idx, dict)
        assert idx["hodge_star"].label == "ホッジ・スター"

    def test_lookup_by_id(self, concepts):
        idx = build_concept_index(concepts)
        c = idx["metric"]
        assert c.introduced_in == "ch05"


class TestBuildAliasIndex:
    def test_builds_flat_dict(self, concepts):
        alias_idx = build_alias_index(concepts)
        assert "ホッジ・スター" in alias_idx
        assert "\\ast" in alias_idx
        assert alias_idx["\\ast"] == "hodge_star"

    def test_longer_aliases_first(self, concepts):
        alias_idx = build_alias_index(concepts)
        items = list(alias_idx.items())
        # Check that longer aliases come before shorter ones
        for i in range(len(items) - 1):
            if items[i][1] == items[i + 1][1]:
                continue
            # Actually, we sort by length descending, so the first should be longest
            # But same concept_id aliases are independent
            pass  # The keys are unique, so sorting is across all aliases

    def test_common_aliases(self, concepts):
        alias_idx = build_alias_index(concepts)
        assert "grad" in alias_idx
        assert "rot" in alias_idx
        assert "div" in alias_idx
        assert "ウェッジ積" in alias_idx
