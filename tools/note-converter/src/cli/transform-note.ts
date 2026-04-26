#!/usr/bin/env npx tsx
/**
 * CLI: main → note 変換（旧 transform_note_reusable.py の代替）
 *
 * 使い方（リポジトリ直下から）:
 *   ./transform-note.sh volumes/note/vol00-nabla/main/フランダース01_main.md volumes/note/vol00-nabla/note/フランダース01_note.md
 * または viewer-ts 内から相対パス:
 *   npm run transform-note -- ../../volumes/note/vol00-nabla/main/foo_main.md ../../volumes/note/vol00-nabla/note/foo_note.md
 */
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { parseArgs } from "node:util";
import { transformMainToNoteMarkdown } from "../transformMainToNote.js";

function readMdUtf8(filePath: string): string {
  try {
    return readFileSync(filePath, "utf-8");
  } catch (e) {
    const err = e as NodeJS.ErrnoException;
    if (err.code === "ENOENT") {
      throw new Error(`Input file not found: ${filePath}`);
    }
    throw e;
  }
}

function main() {
  const repoRoot =
    process.env.TRANSFORM_REPO_ROOT?.trim() || process.cwd();

  const { values, positionals } = parseArgs({
    options: {
      input: { type: "string", short: "i" },
      output: { type: "string", short: "o" },
      verbose: { type: "boolean", short: "v", default: false },
    },
    allowPositionals: true,
    strict: false,
  });

  let inputPath =
    (values.input as string | undefined) || positionals[0] || "";
  let outputPath =
    (values.output as string | undefined) || positionals[1] || "";

  if (!inputPath || !outputPath) {
    console.error(
      "Usage: transform-note <input.md> <output.md>  or  -i in -o out"
    );
    process.exit(1);
  }

  if (!path.isAbsolute(inputPath)) {
    inputPath = path.join(repoRoot, inputPath);
  }
  if (!path.isAbsolute(outputPath)) {
    outputPath = path.join(repoRoot, outputPath);
  }

  if (values.verbose) {
    console.error("Input:", inputPath);
    console.error("Output:", outputPath);
  }

  const content = readMdUtf8(inputPath);
  const transformed = transformMainToNoteMarkdown(content);
  mkdirSync(path.dirname(outputPath), { recursive: true });
  writeFileSync(outputPath, transformed, "utf-8");

  console.error("✓ Transformation complete.");
  console.error("  Input: ", inputPath);
  console.error("  Output:", outputPath);
}

main();
