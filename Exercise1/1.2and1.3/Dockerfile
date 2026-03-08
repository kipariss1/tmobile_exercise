FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN . $HOME/.local/bin/env && uv sync

CMD ["uv", "run", "getweather.py"]