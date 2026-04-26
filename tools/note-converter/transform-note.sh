#!/usr/bin/env bash
# main → note 変換（TypeScript / note-converter）。リポジトリ直下で実行。
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export TRANSFORM_REPO_ROOT="$ROOT"
cd "$ROOT"
if [[ ! -d node_modules ]]; then
  echo "Installing note-converter dependencies …"
  npm install
fi
exec npx tsx src/cli/transform-note.ts "$@"
