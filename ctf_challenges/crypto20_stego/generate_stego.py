# generate_stego.py
from PIL import Image, ImageDraw, ImageFont
import os, sys

FLAG = os.environ.get("FLAG", "FLAG{stego_simple_lsb_2025}")

OUTDIR = "static"
COVER_PATH = os.path.join(OUTDIR, "cover.png")
STEGO_PATH = os.path.join(OUTDIR, "stego.png")

def make_cover(path, w=400, h=200):
    img = Image.new("RGB", (w, h), color=(120,140,200))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except Exception:
        font = None
    draw.text((10, 10), "Sample cover image for stego challenge", fill=(255,255,255), font=font)
    img.save(path)

def text_to_bits(text):
    b = text.encode("utf-8")
    bits = []
    for byte in b:
        for i in range(8):
            bits.append((byte >> (7 - i)) & 1)
    bits += [0]*8  # terminator
    return bits

def embed_lsb(cover_path, out_path, message):
    img = Image.open(cover_path).convert("RGB")
    w,h = img.size
    pixels = img.load()
    bits = text_to_bits(message)
    capacity = w * h
    if len(bits) > capacity:
        raise ValueError("Message too long for image capacity")
    idx = 0
    for y in range(h):
        for x in range(w):
            if idx >= len(bits): break
            r,g,b = pixels[x,y]
            b = (b & 0xFE) | bits[idx]
            pixels[x,y] = (r,g,b)
            idx += 1
        if idx >= len(bits): break
    img.save(out_path, "PNG")

if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)
    if not os.path.exists(COVER_PATH):
        make_cover(COVER_PATH)
    embed_lsb(COVER_PATH, STEGO_PATH, FLAG)
    print("Generated:", STEGO_PATH)
