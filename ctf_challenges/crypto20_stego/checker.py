# checker.py
import sys, requests, re, tempfile, os
from extract_flag import extract_lsb

if len(sys.argv) != 2:
    print("Usage: python checker.py http://host:port")
    sys.exit(2)

BASE = sys.argv[1].rstrip('/')
IMG_URL = BASE + "/static/stego.png"

try:
    r = requests.get(IMG_URL, timeout=6)
    r.raise_for_status()
except Exception as e:
    print("ERROR:", e)
    sys.exit(1)

tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
tmp.write(r.content); tmp.close()
try:
    flag = extract_lsb(tmp.name)
    if flag and re.match(r"FLAG\{[A-Za-z0-9_\-]+\}", flag):
        print("OK:", flag)
        sys.exit(0)
    else:
        print("NOFLAG")
        sys.exit(3)
finally:
    try: os.unlink(tmp.name)
    except: pass
