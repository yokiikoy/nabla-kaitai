#!/usr/bin/env bash
# main → note 変換（TypeScript / note-converter）。
# 引数はプロジェクトルートからの相対パス、または絶対パスで指定する。
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$SCRIPT_DIR"
if [[ ! -d node_modules ]]; then
  echo "Installing note-converter dependencies …"
  npm install
fi
exec env TRANSFORM_REPO_ROOT="$PROJECT_ROOT" npx tsx src/cli/transform-note.ts "$@"
