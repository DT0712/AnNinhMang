# extract_flag.py
from PIL import Image
import sys

def bits_to_text(bits):
    out = []
    i = 0
    while i + 8 <= len(bits):
        byte = 0
        for j in range(8):
            byte = (byte << 1) | bits[i+j]
        if byte == 0:
            break
        out.append(byte)
        i += 8
    try:
        return bytes(out).decode("utf-8")
    except:
        return None

def extract_lsb(path):
    img = Image.open(path).convert("RGB")
    w,h = img.size
    pixels = img.load()
    bits = []
    for y in range(h):
        for x in range(w):
            r,g,b = pixels[x,y]
            bits.append(b & 1)
    return bits_to_text(bits)

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "static/stego.png"
    s = extract_lsb(path)
    if s:
        print("EXTRACTED:", s)
    else:
        print("No message found")
