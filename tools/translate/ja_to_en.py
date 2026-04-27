#!/usr/bin/env python3
"""Translation pipeline: Japanese manuscript → English draft.

Usage:
    python tools/translate/ja_to_en.py manuscript/ja/ch01/ch01.md

Output:
    manuscript/en/ch01/ch01.md

Preserves:
  - YAML frontmatter
  - Code fences (```)
  - Display math ($$, \\[...\\])
  - Inline math ($...$)
  - LSP annotations (<!-- concept-scope: ... -->)
  - HTML tags (<strong>, etc.)

Translates:
  - Japanese prose paragraphs

If --auto flag is given and ollama with a translation model is available,
attempts automatic translation via local LLM.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import requests


def _load_env_file(repo_root: Path) -> None:
    """Load .env file into os.environ if present."""
    env_path = repo_root / ".env"
    if not env_path.exists():
        return
    with env_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())


def find_repo_root() -> Path:
    """Find nabla-kaitai repo root from cwd or script location."""
    cwd = Path.cwd()
    if (cwd / "manuscript" / "ja").exists():
        return cwd
    script_dir = Path(__file__).resolve().parent
    for parent in [script_dir, *script_dir.parents]:
        if (parent / "manuscript" / "ja").exists():
            return parent
    raise RuntimeError("Could not find repo root containing manuscript/ja/")


def protect_blocks(text: str) -> tuple[str, list[tuple[int, str]]]:
    """Replace protected blocks with placeholders.

    Returns (text_with_placeholders, list_of_placeholders).
    """
    placeholders: list[tuple[int, str]] = []
    counter = 0

    def _repl(match: re.Match) -> str:
        nonlocal counter
        ph = f"__PH_{counter:04d}__"
        placeholders.append((counter, match.group(0)))
        counter += 1
        return ph

    # Frontmatter
    text = re.sub(r"^---\n.*?\n---\n", _repl, text, count=1, flags=re.DOTALL)
    # Code fences
    text = re.sub(r"```[\s\S]*?```", _repl, text)
    # Display math
    text = re.sub(r"\$\$[\s\S]*?\$\$", _repl, text)
    text = re.sub(r"\\\[[\s\S]*?\\\]", _repl, text)
    # LSP annotations
    text = re.sub(r"<!--\s*concept-scope:.*?-->", _repl, text)
    text = re.sub(r"<!--\s*role:.*?-->", _repl, text)
    # HTML tags (preserve as-is)
    text = re.sub(r"<[^>]+>", _repl, text)
    # Inline math (preserve as-is)
    text = re.sub(r"(?<!\\)\$[^$\n]+?\$", _repl, text)

    return text, placeholders


def restore_placeholders(text: str, placeholders: list[tuple[int, str]]) -> str:
    """Restore protected blocks from placeholders."""
    for idx, original in placeholders:
        text = text.replace(f"__PH_{idx:04d}__", original, 1)
    return text


def split_paragraphs(text: str) -> list[str]:
    """Split text into paragraphs (blank-line separated)."""
    return [p.strip() for p in text.split("\n\n") if p.strip()]


def is_japanese_prose(paragraph: str) -> bool:
    """Check if paragraph contains Japanese text worth translating."""
    # If it's just placeholders or whitespace, skip
    if not paragraph.strip():
        return False
    # If it contains Japanese characters, it's prose
    if re.search(r"[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9faf]", paragraph):
        return True
    # If it's mostly placeholders with no Japanese, skip
    return False


def build_prompt(paragraphs: list[str]) -> str:
    """Build a single LLM prompt for all Japanese prose paragraphs."""
    lines = [
        "Translate the following Japanese mathematical prose into English.",
        "Rules:",
        "- Preserve all mathematical notation (TeX, inline math, display math).",
        "- Preserve all placeholder markers like __PH_0000__ exactly as-is.",
        "- Use natural, pedagogical English suitable for undergraduate students.",
        "- Maintain the tone: conversational but mathematically precise.",
        "- Do NOT translate placeholder markers.",
        "",
        "Paragraphs (separated by '---PARA---'):",
        "",
    ]
    lines.append("---PARA---".join(paragraphs))
    lines.append("")
    lines.append("Return the translated paragraphs in the same order, separated by '---PARA---'.")
    return "\n".join(lines)


def translate_with_ollama(prompt: str, model: str = "llama3") -> str | None:
    """Attempt translation via local ollama. Returns None if unavailable."""
    if not shutil.which("ollama"):
        return None
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=300,
        )
        if result.returncode == 0:
            return result.stdout
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None


def translate_with_deepseek(prompt: str, api_key: str | None = None, model: str = "deepseek-chat") -> str | None:
    """Attempt translation via DeepSeek API. Returns None if unavailable."""
    if api_key is None:
        api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        return None

    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a professional mathematical translator. "
                    "Translate Japanese mathematical prose into natural, pedagogical English "
                    "suitable for undergraduate students. "
                    "Preserve all TeX math notation exactly. "
                    "Do not translate placeholder markers like __PH_0000__."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.3,
    }
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=120)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]
    except Exception:
        return None


def translate_file(src: Path, dst: Path, auto: bool = False, model: str = "llama3") -> None:
    """Translate a single Japanese chapter to English."""
    text = src.read_text(encoding="utf-8")
    protected_text, placeholders = protect_blocks(text)
    paragraphs = split_paragraphs(protected_text)

    # Separate translatable and non-translatable paragraphs
    translatable: list[tuple[int, str]] = []
    non_translatable: dict[int, str] = {}

    for i, para in enumerate(paragraphs):
        if is_japanese_prose(para):
            translatable.append((i, para))
        else:
            non_translatable[i] = para

    if not translatable:
        print(f"No Japanese prose found in {src}")
        dst.write_text(text, encoding="utf-8")
        return

    # Build prompt
    prompt = build_prompt([para for _, para in translatable])

    translated_raw: str | None = None
    if auto:
        # 1. Try DeepSeek API first
        deepseek_key = os.environ.get("DEEPSEEK_API_KEY")
        deepseek_model = os.environ.get("DEEPSEEK_MODEL", "deepseek-chat")
        if deepseek_key:
            print(f"Attempting automatic translation via DeepSeek ({deepseek_model})...")
            translated_raw = translate_with_deepseek(prompt, api_key=deepseek_key, model=deepseek_model)
            if translated_raw is None:
                print("DeepSeek translation failed.")
        # 2. Fallback to ollama
        if translated_raw is None:
            print(f"Attempting automatic translation via ollama ({model})...")
            translated_raw = translate_with_ollama(prompt, model=model)
        if translated_raw is None:
            print("Automatic translation failed. Falling back to prompt-only mode.")
            auto = False

    if not auto or translated_raw is None:
        # Write prompt to a sidecar file for manual LLM usage
        prompt_path = dst.with_suffix(".prompt.txt")
        prompt_path.write_text(prompt, encoding="utf-8")
        print(f"Prompt written to: {prompt_path}")
        print(f"Feed this prompt to your LLM (ChatGPT, Claude, DeepSeek, etc.),")
        print(f"then paste the result back and run with --apply {prompt_path}")
        return

    # Parse translated output
    translated_paras = translated_raw.split("---PARA---")
    if len(translated_paras) != len(translatable):
        print(
            f"Warning: paragraph count mismatch ({len(translated_paras)} vs {len(translatable)})"
        )
        # Pad or truncate to match
        while len(translated_paras) < len(translatable):
            translated_paras.append("[TRANSLATION MISSING]")
        translated_paras = translated_paras[: len(translatable)]

    # Reconstruct
    translated_map: dict[int, str] = {}
    for (idx, _), trans in zip(translatable, translated_paras):
        translated_map[idx] = trans.strip()
    translated_map.update(non_translatable)

    final_paragraphs = [translated_map[i] for i in range(len(paragraphs))]
    final_text = "\n\n".join(final_paragraphs)
    final_text = restore_placeholders(final_text, placeholders)

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(final_text, encoding="utf-8")
    print(f"Translated: {src} → {dst}")


def apply_translation(src_md: Path, prompt_response_path: Path) -> None:
    """Apply a saved LLM response to reconstruct the English markdown."""
    text = src_md.read_text(encoding="utf-8")
    protected_text, placeholders = protect_blocks(text)
    paragraphs = split_paragraphs(protected_text)

    translatable_indices = [
        i for i, para in enumerate(paragraphs) if is_japanese_prose(para)
    ]

    response_text = prompt_response_path.read_text(encoding="utf-8")
    translated_paras = response_text.split("---PARA---")

    if len(translated_paras) != len(translatable_indices):
        print(
            f"Warning: paragraph count mismatch ({len(translated_paras)} vs {len(translatable_indices)})"
        )

    translated_map: dict[int, str] = {}
    for idx, trans in zip(translatable_indices, translated_paras):
        translated_map[idx] = trans.strip()

    for i, para in enumerate(paragraphs):
        if i not in translated_map:
            translated_map[i] = para

    final_paragraphs = [translated_map[i] for i in range(len(paragraphs))]
    final_text = "\n\n".join(final_paragraphs)
    final_text = restore_placeholders(final_text, placeholders)

    dst = src_md.parent.parent.parent / "en" / src_md.parent.name / src_md.name
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(final_text, encoding="utf-8")
    print(f"Applied translation: {src_md} → {dst}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Translate Japanese manuscript to English.")
    parser.add_argument("source", type=Path, help="Source Japanese .md file")
    parser.add_argument(
        "--auto", action="store_true", help="Attempt automatic translation via ollama"
    )
    parser.add_argument("--model", default="llama3", help="Ollama model name (default: llama3)")
    parser.add_argument(
        "--apply", type=Path, metavar="RESPONSE", help="Apply a saved LLM response file"
    )
    args = parser.parse_args(argv)

    repo_root = find_repo_root()
    _load_env_file(repo_root)
    src = args.source.resolve()

    if not src.exists():
        print(f"Source file not found: {src}", file=sys.stderr)
        return 1

    # Compute destination path: manuscript/ja/... → manuscript/en/...
    rel = src.relative_to(repo_root / "manuscript" / "ja")
    dst = repo_root / "manuscript" / "en" / rel

    if args.apply:
        apply_translation(src, args.apply)
    else:
        translate_file(src, dst, auto=args.auto, model=args.model)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
