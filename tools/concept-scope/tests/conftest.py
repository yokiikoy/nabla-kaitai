"""Test fixtures for concept-scope tests."""

from pathlib import Path
import pytest
import yaml
import tempfile


@pytest.fixture
def repo_root():
    """Returns the actual repository root."""
    return Path(__file__).resolve().parents[3]


@pytest.fixture
def config_dir(repo_root):
    return repo_root / "docs" / "concept-scope"


@pytest.fixture
def concepts():
    from concept_scope.registry import load_concepts

    return load_concepts()


@pytest.fixture
def chapters():
    from concept_scope.scope import load_chapters

    return load_chapters()


@pytest.fixture
def rules():
    from concept_scope.rules import compile_rules

    return compile_rules()


@pytest.fixture
def tmp_chapter_md(tmp_path):
    """Create a temporary markdown file with frontmatter for testing."""

    def _create(chapter_num: int, body: str = "", extra_frontmatter: dict | None = None):
        fm = {"chapter": chapter_num, "order": chapter_num * 10}
        if extra_frontmatter:
            fm.update(extra_frontmatter)
        fm_yaml = yaml.dump(fm, allow_unicode=True, default_flow_style=False).strip()
        content = f"---\n{fm_yaml}\n---\n\n{body}\n"
        filepath = tmp_path / f"ch{chapter_num:02d}.md"
        filepath.write_text(content, encoding="utf-8")
        return filepath

    return _create


@pytest.fixture
def sample_text_violation():
    """Text that should trigger dx^2 violation."""
    return "測定すると dx^2 が得られる。"


@pytest.fixture
def sample_text_clean():
    """Text that should not trigger any violation."""
    return "外微分 d により、形式の次数が1つ上がる。"


@pytest.fixture
def sample_text_hodge_violation():
    """Text that should trigger hodge-star future concept violation."""
    return "ホッジ・スターを作用させると \\ast(dx) が得られる。"


@pytest.fixture
def sample_text_overexplain():
    """Text that should trigger over-explanation of one-form."""
    return "1-form とは、ベクトルを1つ食べてスカラーを返す測定器である。"
