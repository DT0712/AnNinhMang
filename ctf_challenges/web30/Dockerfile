FROM python:3.11-slim

# create app user and dir
RUN useradd -m ctfuser && mkdir -p /app

WORKDIR /app

# install deps
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy app
COPY app/ /app/

# copy flag into location only inside image
COPY secrets/flag.txt /srv/secret/flag.txt
RUN chown -R ctfuser:ctfuser /app /srv/secret && chmod 440 /srv/secret/flag.txt

# run as unprivileged user
USER ctfuser

EXPOSE 8080

ENV FLASK_ENV=production
CMD ["python", "/app/app.py"]
