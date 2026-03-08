# Exercise 1.2

Install deps & run
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh  # install uv
uv sync
uv run getweather.py
```

Build & run docker container
```bash
docker build -t getweather:dev .
docker run --rm -e OWM_API_KEY="xxxx" -e OWM_CITY="Honolulu" getweather:dev
```