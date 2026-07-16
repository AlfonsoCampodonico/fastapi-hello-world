# FastAPI Hello World

A minimal [FastAPI](https://fastapi.tiangolo.com/) application, ready to deploy.

## Endpoints

| Method | Path      | Response                        |
| ------ | --------- | ------------------------------- |
| GET    | `/`       | `{"message": "Hello, World!"}`  |
| GET    | `/health` | `{"status": "ok"}`              |
| GET    | `/docs`   | Interactive Swagger UI          |

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000 — or http://127.0.0.1:8000/docs for the auto-generated API docs.

## Run with Docker

```bash
docker build -t fastapi-hello-world .
docker run -p 8000:8000 fastapi-hello-world
```

## Deployment

The app reads the port from the `$PORT` environment variable (defaulting to `8000`), so it works on most container and PaaS hosts out of the box:

- **Docker / Cloud Run / any container host** — uses the included `Dockerfile`.
- **PaaS (Heroku-style)** — uses the included `Procfile`.

The start command is:

```bash
uvicorn app.main:app --host 0.0.0.0 --port ${PORT}
```
