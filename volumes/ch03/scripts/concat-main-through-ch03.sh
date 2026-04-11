#!/usr/bin/env bash
# Concatenate vol03 main chapter sources into one file for LLM / review.
# Do not edit full_through_ch03_main.md by hand; re-run this script after changing ch01–ch03.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VOL="$(cd "$SCRIPT_DIR/.." && pwd)"
MAIN="$VOL/main"
OUT="$MAIN/full_through_ch03_main.md"
CH1="$MAIN/ch01_matrix_calculus_main.md"
CH2="$MAIN/ch02_area_volume_main.md"
CH3="$MAIN/ch03_integration_forms_main.md"

for f in "$CH1" "$CH2" "$CH3"; do
  if [[ ! -f "$f" ]]; then
    echo "error: missing $f" >&2
    exit 1
  fi
done

{
  cat << 'EOF'
---
title: "vol03 連続稿（第1章〜第3章）"
series: dx-matrix
chapters: [1, 2, 3]
source_files:
  - main/ch01_matrix_calculus_main.md
  - main/ch02_area_volume_main.md
  - main/ch03_integration_forms_main.md
---

EOF
  tail -n +7 "$CH1"
  printf '\n---\n\n'
  tail -n +7 "$CH2"
  printf '\n---\n\n'
  tail -n +7 "$CH3"
} > "$OUT"

echo "Wrote $OUT"
