import os
import glob
import re
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from core.profile import BuildProfile

@dataclass
class TocItem:
    level: int
    title: str
    anchor: str

@dataclass
class Chapter:
    id: str             # e.g., "01", "afterword"
    title: str          # Full title from h1
    short_title: str    # Short title for sidebar
    content_lines: List[str]
    toc_items: List[TocItem]
    filename: str       # HTML filename, e.g., "ch01.html"
    is_front_matter: bool = False
    is_included_in_content: bool = True

class ManuscriptModel:
    def __init__(self, profile: BuildProfile, base_dir: str = 'manuscript/ja'):
        self.profile = profile
        self.base_dir = base_dir
        self.chapters: List[Chapter] = []
        self.front_matter: List[Chapter] = []
        self._load()

    def _slugify(self, text: str) -> str:
        # Simple slugify for anchors
        text = re.sub(r'<[^>]+>', '', text)  # remove tags
        text = re.sub(r'[\s]+', '-', text.strip())
        return text

    def _parse_markdown(self, filepath: str) -> tuple[str, List[str], List[TocItem]]:
        lines = []
        toc = []
        title = ""
        if not os.path.exists(filepath):
            return title, lines, toc

        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                lines.append(line.rstrip('\n'))
                # Extract headers
                h_match = re.match(r'^(#{1,3})\s+(.+)$', line)
                if h_match:
                    level = len(h_match.group(1))
                    text = h_match.group(2).strip()
                    if level == 1 and not title:
                        title = text
                    elif level > 1:
                        anchor = self._slugify(text)
                        toc.append(TocItem(level=level, title=text, anchor=anchor))
        return title, lines, toc

    def _load_chapter(self, ch_id: str, is_front: bool = False) -> Optional[Chapter]:
        # Determine paths
        if is_front:
            files = glob.glob(os.path.join(self.base_dir, 'ch00', f'*{ch_id}*.md'))
            if not files: return None
            filepath = files[0]
            fname = os.path.basename(filepath)
            # mapping logic logic
            mapping = {"01_preface.md": "index.html", "02_introduction.md": "intro.html", "03_portal.md": "portal.html"}
            filename = mapping.get(fname, fname.replace('.md', '.html'))
        elif ch_id.isdigit():
            filepath = os.path.join(self.base_dir, f'ch{ch_id}', f'ch{ch_id}.md')
            filename = f'ch{ch_id}.html'
        else:
            filepath = os.path.join(self.base_dir, f'{ch_id}.md')
            mapping = {"afterword": "postscript.html", "references": "refs.html", "appendix": "appendix.html"}
            filename = mapping.get(ch_id, f'{ch_id}.html')

        title, content_lines, toc_items = self._parse_markdown(filepath)
        if not title:
            title = f"Chapter {ch_id}"

        short_title = title.split("：")[0] if "：" in title else title.split("——")[0]
        
        is_included = ch_id in self.profile.content_scope or is_front

        return Chapter(
            id=ch_id,
            title=title,
            short_title=short_title,
            content_lines=content_lines if is_included else [], # Hide content if not in scope
            toc_items=toc_items, # Keep TOC items regardless of content scope
            filename=filename,
            is_front_matter=is_front,
            is_included_in_content=is_included
        )

    def _load(self):
        # Load Front Matter (Content scope only, usually)
        fm_files = sorted(glob.glob(os.path.join(self.base_dir, 'ch00', '*.md')))
        for f in fm_files:
            ch_id = os.path.basename(f).split('_')[0] # e.g., '01', '02'
            ch = self._load_chapter(ch_id, is_front=True)
            if ch:
                self.front_matter.append(ch)

        # Load TOC Scope Chapters
        for ch_id in self.profile.toc_scope:
            ch = self._load_chapter(ch_id)
            if ch:
                self.chapters.append(ch)

    def get_full_toc_chapters(self) -> List[Chapter]:
        return self.chapters

    def get_content_chapters(self) -> List[Chapter]:
        # Return front matter + chapters that are in content scope
        return self.front_matter + [ch for ch in self.chapters if ch.is_included_in_content]
