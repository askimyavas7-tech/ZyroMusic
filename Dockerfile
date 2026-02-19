FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    git ffmpeg curl build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -U pip setuptools wheel \
    && pip install -r /app/requirements.txt

COPY . /app/

# start dosyası execute değilse çalışmaz, garantiye alıyoruz
RUN chmod +x /app/start || true

CMD ["bash", "/app/start"]
