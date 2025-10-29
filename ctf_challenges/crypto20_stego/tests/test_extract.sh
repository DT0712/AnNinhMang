#!/usr/bin/env bash
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
IMG="$ROOT/static/stego.png"
if [ ! -f "$IMG" ]; then
  python3 "$ROOT/generate_stego.py"
fi
OUT=$(python3 "$ROOT/extract_flag.py" "$IMG")
echo "$OUT"
echo "$OUT" | grep -q "FLAG{" && echo "PASS" || (echo "FAIL" && exit 1)
