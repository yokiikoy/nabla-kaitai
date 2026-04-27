#!/usr/bin/env python3
"""pygls-based LSP server for concept-scope diagnostics.

Reuses diagnostic logic from the concept_scope package.
Start via stdio or TCP. Requires pygls and its dependencies
(install with: pip install pygls pyyaml).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import urlparse, unquote

from pygls.lsp.server import LanguageServer
from lsprotocol.types import (
    TEXT_DOCUMENT_DID_OPEN,
    TEXT_DOCUMENT_DID_SAVE,
    TEXT_DOCUMENT_DID_CHANGE,
    TEXT_DOCUMENT_HOVER,
    TEXT_DOCUMENT_COMPLETION,
    CompletionItem,
    CompletionItemKind,
    CompletionItemTag,
    CompletionList,
    CompletionParams,
    Diagnostic,
    DiagnosticSeverity,
    Hover,
    HoverParams,
    MarkupContent,
    MarkupKind,
    Position,
    PublishDiagnosticsParams,
    Range,
)

from concept_scope import (
    Chapter,
    compile_rules,
    check_file,
    check_text,
    load_chapters,
    scope_for_chapter,
    build_concept_index,
    build_alias_index,
    load_concepts,
    REPO_ROOT,
)

SEVERITY_MAP = {
    "error": DiagnosticSeverity.Error,
    "warning": DiagnosticSeverity.Warning,
    "information": DiagnosticSeverity.Information,
    "hint": DiagnosticSeverity.Hint,
}


class ConceptScopeServer(LanguageServer):
    def __init__(self, repo_root: Path):
        super().__init__("concept-scope", "v0.2.0")
        self.repo_root = repo_root
        self._chapters: dict[str, Chapter] | None = None
        self._rules: list[dict] | None = None
        self._concepts: dict[str, list] = {}
        self._concept_index: dict[str, dict] = {}
        self._alias_index: dict[str, dict] = {}

    @property
    def chapters(self):
        if self._chapters is None:
            self._chapters = load_chapters(self.repo_root)
        return self._chapters

    @property
    def rules(self):
        if self._rules is None:
            self._rules = compile_rules(str(self.repo_root / "docs" / "concept-scope"))
        return self._rules

    @staticmethod
    def _detect_language(path: Path) -> str:
        try:
            rel = path.relative_to(Path.home() / "dev" / "knowledge" / "work" / "nabla-kaitai")
        except ValueError:
            try:
                rel = path.relative_to(Path("/home/yokii/dev/knowledge/work/nabla-kaitai"))
            except ValueError:
                rel = path
        parts = rel.parts
        if "en" in parts:
            return "en"
        return "ja"

    def concepts_for(self, path: Path):
        lang = self._detect_language(path)
        if lang not in self._concepts:
            self._concepts[lang] = load_concepts(language=lang)
        return self._concepts[lang]

    def concept_index_for(self, path: Path):
        lang = self._detect_language(path)
        if lang not in self._concept_index:
            self._concept_index[lang] = build_concept_index(self.concepts_for(path))
        return self._concept_index[lang]

    def alias_index_for(self, path: Path):
        lang = self._detect_language(path)
        if lang not in self._alias_index:
            self._alias_index[lang] = build_alias_index(self.concepts_for(path))
        return self._alias_index[lang]

    @staticmethod
    def uri_to_path(uri: str) -> Path:
        parsed = urlparse(uri)
        return Path(unquote(parsed.path))


def _diagnostics_for_path(ls: ConceptScopeServer, path: Path) -> list[Diagnostic]:
    concept_diags = check_file(path, ls.repo_root, ls.chapters, ls.rules, concepts=ls.concepts_for(path))
    ls_diagnostics: list[Diagnostic] = []
    for diag in concept_diags:
        ls_diagnostics.append(
            Diagnostic(
                range=Range(
                    start=Position(line=diag.line - 1, character=diag.column - 1),
                    end=Position(line=diag.line - 1, character=diag.end_column - 1),
                ),
                severity=SEVERITY_MAP.get(diag.severity, DiagnosticSeverity.Warning),
                code=diag.code,
                message=diag.message,
                source="concept-scope",
            )
        )
    return ls_diagnostics


def _find_concept_at_position(
    ls: ConceptScopeServer, uri: str, position: Position
) -> str | None:
    """Return concept_id if cursor is on a concept alias, else None."""
    doc = ls.workspace.get_text_document(uri)
    if doc is None:
        return None
    try:
        line_text = doc.lines[position.line]
    except IndexError:
        return None

    # Try aliases sorted by length (longest first = greedy)
    for alias, concept_id in ls.alias_index_for(ls.uri_to_path(uri)).items():
        idx = 0
        while True:
            idx = line_text.find(alias, idx)
            if idx == -1:
                break
            if idx <= position.character < idx + len(alias):
                return concept_id
            idx += 1
    return None


def _find_chapter_for_uri(ls: ConceptScopeServer, uri: str) -> str | None:
    from concept_scope.scope import infer_chapter, relative_path

    path = ls.uri_to_path(uri)
    chapter = infer_chapter(path, ls.repo_root, ls.chapters)
    if chapter:
        return chapter.id
    return None


def parse_args(argv: list[str]):
    parser = argparse.ArgumentParser(
        description="Start concept-scope LSP server (pygls)."
    )
    parser.add_argument(
        "--root",
        default=str(REPO_ROOT),
        help="Repository root. Defaults to detected nabla-kaitai root.",
    )
    parser.add_argument(
        "--tcp",
        action="store_true",
        help="Start TCP server instead of stdio.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=2087,
        help="TCP port (only with --tcp). Default 2087.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    root = Path(args.root).resolve()
    if not root.exists():
        print(f"Root does not exist: {root}", file=sys.stderr)
        return 1

    server = ConceptScopeServer(root)

    @server.feature(TEXT_DOCUMENT_DID_OPEN)
    @server.feature(TEXT_DOCUMENT_DID_SAVE)
    def check_document(ls: ConceptScopeServer, params):
        # Ensure workspace is synced (our handler overrides pygls's built-in)
        if hasattr(params, "text_document"):
            try:
                ls.protocol.workspace.put_text_document(params.text_document)
            except Exception:
                pass

        uri = params.text_document.uri
        path = ls.uri_to_path(uri)
        if not path.exists():
            return
        diagnostics = _diagnostics_for_path(ls, path)
        ls.text_document_publish_diagnostics(
            PublishDiagnosticsParams(uri=uri, diagnostics=diagnostics)
        )

    @server.feature(TEXT_DOCUMENT_DID_CHANGE)
    def check_change(ls: ConceptScopeServer, params):
        """On each keystroke, run regex-only checks for speed."""
        uri = params.text_document.uri
        path = ls.uri_to_path(uri)
        doc = ls.workspace.get_text_document(uri)
        if doc is None:
            return

        text = doc.source
        file_path_str = str(path)

        diags = check_text(
            text, file_path_str, ls.repo_root,
            ls.chapters, ls.rules, concepts=ls.concepts_for(path),
            mode="regex_only",
        )
        ls_diagnostics: list[Diagnostic] = []
        for diag in diags:
            ls_diagnostics.append(
                Diagnostic(
                    range=Range(
                        start=Position(line=diag.line - 1, character=diag.column - 1),
                        end=Position(line=diag.line - 1, character=diag.end_column - 1),
                    ),
                    severity=SEVERITY_MAP.get(diag.severity, DiagnosticSeverity.Warning),
                    code=diag.code,
                    message=diag.message,
                    source="concept-scope",
                )
            )
        ls.text_document_publish_diagnostics(
            PublishDiagnosticsParams(uri=uri, diagnostics=ls_diagnostics)
        )

    @server.feature(TEXT_DOCUMENT_HOVER)
    def hover(ls: ConceptScopeServer, params: HoverParams):
        uri = params.text_document.uri
        concept_id = _find_concept_at_position(ls, uri, params.position)
        if not concept_id:
            return None

        concept = ls.concept_index_for(ls.uri_to_path(uri)).get(concept_id)
        if not concept:
            return None

        chapter_id = _find_chapter_for_uri(ls, uri)
        scope = scope_for_chapter(
            chapter_id, root=ls.repo_root, frontmatter_path=ls.uri_to_path(uri)
        ) if chapter_id else None

        return _format_hover(concept, chapter_id, scope)

    @server.feature(TEXT_DOCUMENT_COMPLETION)
    def completion(ls: ConceptScopeServer, params: CompletionParams):
        chapter_id = _find_chapter_for_uri(ls, uri=params.text_document.uri)
        if not chapter_id:
            return None

        scope = scope_for_chapter(
            chapter_id, root=ls.repo_root,
            frontmatter_path=ls.uri_to_path(params.text_document.uri)
        )
        return _format_completions(ls.concepts_for(ls.uri_to_path(params.text_document.uri)), scope)

    if args.tcp:
        server.start_tcp("127.0.0.1", args.port)
    else:
        server.start_io()

    return 0


def _format_hover(concept, chapter_id: str | None, scope) -> Hover | None:
    concept = concept  # concept is a Concept dataclass
    intro_chapter = concept.introduced_in

    if scope and concept.id in scope.being_introduced:
        info = scope.being_introduced[concept.id]
        allowed = info.get("to", "computation") if isinstance(info, dict) else info
        status = f"**この章で定義中**。{allowed} まで可。"
    elif scope and concept.id in scope.preview_only:
        info = scope.preview_only[concept.id]
        max_lvl = info.get("max_level", "mention") if isinstance(info, dict) else info
        status = f"⚠ **伏線のみ許可** ({max_lvl} まで)。具体式・計算禁止。"
    elif scope and concept.id in scope.available:
        max_lvl = scope.available[concept.id]
        status = f"使用可能 (最大: {max_lvl})"
    elif scope and concept.id in scope.forbidden:
        status = "❌ **使用禁止**"
    elif intro_chapter and chapter_id:
        intro_num = int(intro_chapter.replace("ch", ""))
        cur_num = int(chapter_id.replace("ch", ""))
        if intro_num > cur_num:
            status = f"❌ **未来概念** ({intro_chapter} で導入)"
        else:
            status = f"使用可能 (最大: computation)"
    else:
        status = "定義済み"

    markdown = (
        f"**{concept.label}**  (`{concept.id}`)\n\n"
        f"Defined in: **{intro_chapter}**\n"
        f"Kind: {concept.kind}\n"
        f"Status: {status}\n\n"
        f"*{concept.summary}*\n"
    )

    return Hover(
        contents=MarkupContent(kind=MarkupKind.Markdown, value=markdown)
    )


def _format_completions(concepts, scope) -> CompletionList:
    items: list[CompletionItem] = []
    for concept in concepts:
        if concept.id in scope.being_introduced:
            info = scope.being_introduced[concept.id]
            to_level = info.get("to", "computation") if isinstance(info, dict) else info
            items.append(
                CompletionItem(
                    label=concept.label,
                    detail=f"導入中 · {concept.kind}",
                    documentation=concept.summary,
                    kind=CompletionItemKind.Reference,
                )
            )
        elif concept.id in scope.available:
            items.append(
                CompletionItem(
                    label=concept.label,
                    detail=f"ch{concept.introduced_in} · {concept.kind}",
                    documentation=concept.summary,
                    kind=CompletionItemKind.Reference,
                )
            )
        elif concept.id in scope.preview_only:
            info = scope.preview_only[concept.id]
            max_lvl = info.get("max_level", "mention") if isinstance(info, dict) else info
            items.append(
                CompletionItem(
                    label=f"{concept.label} (preview only)",
                    detail=f"ch{concept.introduced_in} · 伏線のみ ({max_lvl})",
                    documentation=concept.summary,
                    kind=CompletionItemKind.Reference,
                    tags=[CompletionItemTag.Deprecated],
                )
            )
    return CompletionList(is_incomplete=False, items=items)


if __name__ == "__main__":
    raise SystemExit(main())
