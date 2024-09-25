FROM python:3.12.0b2-slim-buster

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt clean && \
    rm -rf /var/cache/apt/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

COPY requirements.txt /tmp

RUN pip install -U pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app

WORKDIR /app
