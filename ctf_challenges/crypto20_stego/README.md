crypto20_stego
===============

Local dev:
1. python -m venv .venv
2. .\.venv\Scripts\Activate.ps1
3. pip install -r requirements.txt
4. python generate_stego.py
5. python app.py
6. open http://127.0.0.1:8080

Docker:
docker build -t crypto20_stego:latest .
docker run -d -p 8080:8080 -e FLAG="FLAG{team_test}" crypto20_stego:latest
