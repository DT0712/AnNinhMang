# web30/app/app.py
from flask import Flask, request, render_template, redirect, url_for, flash, abort
import os

app = Flask(__name__)
app.secret_key = "replace-me-with-random-secret"

# --- DEV-FRIENDLY: use project-relative paths for uploads and secret dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # web30/app
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))  # web30
UPLOAD_FOLDER = os.path.join(PROJECT_ROOT, "uploads")     # web30/uploads
SECRET_DIR = os.path.join(PROJECT_ROOT, "srv", "secret")  # web30/srv/secret

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(SECRET_DIR, exist_ok=True)

# intentionally insecure view path join for educational LFI
@app.route("/")
def index():
    files = []
    try:
        files = os.listdir(UPLOAD_FOLDER)
    except Exception:
        files = []
    return render_template("index.html", files=files)

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        flash("No file part")
        return redirect(url_for('index'))
    f = request.files["file"]
    if f.filename == "":
        flash("No selected file")
        return redirect(url_for('index'))
    # weak sanitization on purpose
    safe_name = f.filename.replace("../", "")
    dest = os.path.join(UPLOAD_FOLDER, safe_name)
    f.save(dest)
    flash("Uploaded")
    return redirect(url_for('index'))

# vulnerable endpoint: reads file by 'file' param without full sanitization
@app.route("/view")
def view():
    file = request.args.get("file", "")
    # intentionally vulnerable: naive join (teaches LFI via ../)
    target_path = os.path.join(UPLOAD_FOLDER, file)
    
    
    try:
        if not os.path.exists(target_path):
            abort(404)
        with open(target_path, "r", encoding="utf-8", errors="ignore") as fh:
            content = fh.read()
        return render_template("view.html", filename=file, content=content)
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    # dev: bind localhost only (safer) and debug off by default
    app.run(host="127.0.0.1", port=8080)
