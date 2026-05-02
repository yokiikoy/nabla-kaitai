"""LLM context export: generates chapter-scope constraints for LLM prompts."""

from __future__ import annotations

from concept_scope.models import ChapterScope
from concept_scope.scope import scope_for_chapter
from concept_scope.registry import load_concepts, build_concept_index


def export_context_markdown(chapter_id: str) -> str:
    """Generate a Markdown-formatted LLM context snippet for a chapter.

    Can be inserted at the top of an LLM writing prompt.
    """
    scope = scope_for_chapter(chapter_id)
    concepts = load_concepts()
    concept_index = build_concept_index(concepts)
    chapter_num = int(chapter_id.replace("ch", ""))

    lines = [
        f"<!-- CONCEPT-SCOPE: {chapter_id} -->",
        "<!-- LLM: 以下の制約に従って執筆してください -->",
        "",
    ]

    # Available concepts
    lines.append("## 使用可能な概念 (Available)")
    if scope.available:
        for cid, max_level in scope.available.items():
            concept = concept_index.get(cid)
            label = concept.label if concept else cid
            suffix = ""
            if cid in scope.being_introduced:
                suffix = " **(この章で定義中)**"
            lines.append(f"- **{label}** (`{cid}`): {max_level} まで可{suffix}")
    else:
        lines.append("- (なし)")

    # Preview only
    lines.append("")
    lines.append("## 伏線のみ許可 (Preview Only)")
    if scope.preview_only:
        for cid, info in scope.preview_only.items():
            concept = concept_index.get(cid)
            label = concept.label if concept else cid
            max_lvl = info.get("max_level", "mention") if isinstance(info, dict) else info
            note = ""
            if isinstance(info, dict) and info.get("note"):
                note = f" — {info['note']}"
            lines.append(f"- **{label}** (`{cid}`): {max_lvl} まで。具体式・計算禁止。{note}")
    else:
        lines.append("- (なし)")

    # Recap limited (do not re-explain)
    lines.append("")
    lines.append("## 再説明禁止 (Do Not Re-explain)")
    if scope.recap_limited:
        for cid, info in scope.recap_limited.items():
            concept = concept_index.get(cid)
            label = concept.label if concept else cid
            max_lvl = info.get("max_level", "mention") if isinstance(info, dict) else info
            max_lines = info.get("max_lines", 3) if isinstance(info, dict) else 3
            lines.append(f"- **{label}** (`{cid}`): 最大 {max_lines} 行の参照に留める")
    else:
        lines.append("- (なし)")

    # Forbidden
    lines.append("")
    lines.append("## 使用禁止 (Forbidden)")
    forbidden_items = list(scope.forbidden)
    all_concepts = [c.id for c in concepts]
    for c in concepts:
        intro_num = int(c.introduced_in.replace("ch", "")) if c.introduced_in.startswith("ch") else 99
        if intro_num > chapter_num and c.id not in forbidden_items:
            forbidden_items.append(c.id)

    if forbidden_items:
        for cid in forbidden_items:
            concept = concept_index.get(cid)
            label = concept.label if concept else cid
            intro = concept.introduced_in if concept else "?"
            lines.append(f"- **{label}** (`{cid}`): {intro} で導入。それまで使用禁止。")
    else:
        lines.append("- (なし)")

    # Permanent notation contracts
    lines.append("")
    lines.append("## 恒久記法制約 (Notation Contracts)")
    lines.append("- `dx^2`, `dy^2`, `dz^2`, `dr^2` 表記: **全章通して禁止**")
    lines.append("- `\\oint` を閉曲面積分に使わないこと (`\\iint` 推奨)")

    return "\n".join(lines)


def export_context_json(chapter_id: str) -> dict:
    """Generate a JSON-formatted LLM context for a chapter."""
    scope = scope_for_chapter(chapter_id)
    concepts = load_concepts()
    concept_index = build_concept_index(concepts)
    chapter_num = int(chapter_id.replace("ch", ""))

    result = {
        "chapter": chapter_id,
        "order": scope.order,
        "available": [],
        "preview_only": [],
        "recap_limited": [],
        "forbidden": [],
        "notation_contracts": [
            {"pattern": "dx^2|dy^2|dz^2|dr^2", "reason": "基底1-formの二乗禁止", "permanent": True},
            {"pattern": "\\oint_{\\partial V}", "reason": "閉曲面積分は\\iint推奨", "permanent": True},
        ],
    }

    for cid, max_level in scope.available.items():
        concept = concept_index.get(cid)
        item = {"id": cid, "max_level": max_level}
        if concept:
            item["label"] = concept.label
        if cid in scope.being_introduced:
            item["being_introduced"] = True
        result["available"].append(item)

    for cid, info in scope.preview_only.items():
        concept = concept_index.get(cid)
        max_lvl = info.get("max_level", "mention") if isinstance(info, dict) else info
        item = {"id": cid, "max_level": max_lvl}
        if concept:
            item["label"] = concept.label
            item["introduced_in"] = concept.introduced_in
        if isinstance(info, dict) and info.get("note"):
            item["note"] = info["note"]
        result["preview_only"].append(item)

    for cid, info in scope.recap_limited.items():
        concept = concept_index.get(cid)
        max_lvl = info.get("max_level", "mention") if isinstance(info, dict) else info
        max_lines = info.get("max_lines", 3) if isinstance(info, dict) else 3
        item = {"id": cid, "max_level": max_lvl, "max_lines": max_lines}
        if concept:
            item["label"] = concept.label
        result["recap_limited"].append(item)

    for cid in scope.forbidden:
        concept = concept_index.get(cid)
        item = {"id": cid}
        if concept:
            item["label"] = concept.label
            item["introduced_in"] = concept.introduced_in
        result["forbidden"].append(item)

    return result
