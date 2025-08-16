FROM debian:stable-slim

RUN apt-get update \
    && apt-get install -y \
        git \
        curl \
    && curl -LsSf https://astral.sh/uv/install.sh | sh \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY . /workspace
