# app.py
from flask import Flask, render_template, url_for
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html", stego_url=url_for('static', filename='stego.png'))

@app.route("/image")
def image_page():
    return render_template("image.html", stego_url=url_for('static', filename='stego.png'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
