from dataclasses import dataclass
from typing import List, Optional

@dataclass
class BuildProfile:
    name: str
    content_scope: List[str]  # e.g., ['00', '01', 'afterword', 'references', 'appendix']
    toc_scope: List[str]      # e.g., ['01', '02', '03', ..., '12', 'afterword', ...]
    is_preview: bool

# Define scopes
FULL_CHAPTERS = [f"{i:02d}" for i in range(1, 13)]
FRONT_MATTER = ['00']
BACK_MATTER = ['afterword', 'references', 'appendix']

PROFILES = {
    'full': BuildProfile(
        name='full',
        content_scope=FRONT_MATTER + FULL_CHAPTERS + BACK_MATTER,
        toc_scope=FULL_CHAPTERS + BACK_MATTER,
        is_preview=False
    ),
    'preview': BuildProfile(
        name='preview',
        content_scope=FRONT_MATTER + ['01'] + BACK_MATTER,
        toc_scope=FULL_CHAPTERS + BACK_MATTER,  # TOC is full!
        is_preview=True
    )
}

def get_profile(name: str) -> BuildProfile:
    if name not in PROFILES:
        raise ValueError(f"Unknown profile: {name}")
    return PROFILES[name]
