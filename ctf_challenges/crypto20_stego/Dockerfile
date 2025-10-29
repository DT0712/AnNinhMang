# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

RUN useradd -m ctfuser && chown -R ctfuser:ctfuser /app
USER ctfuser

ENV PORT=8080
ENTRYPOINT ["sh","-c","python generate_stego.py && exec python app.py"]
