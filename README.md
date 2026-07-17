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

uvicorn main:app --reload
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
gunicorn main:app -k uvicorn.workers.UvicornWorker --bind [::]:${PORT}
```

> **Why gunicorn with `--bind [::]`?** On IPv6 / dual-stack hosts (e.g. Laravel
> Cloud), the platform health probe connects to the pod's IPv6 address, while the
> in-pod proxy reaches the app over IPv4 loopback. `gunicorn --bind [::]` binds
> **dual-stack** (serves both), whereas `uvicorn --host ::` binds IPv6-only and
> `uvicorn --host 0.0.0.0` binds IPv4-only — so neither uvicorn form satisfies
> both paths. gunicorn (with the uvicorn worker) does.

On Laravel Cloud this matches the auto-detected default start command (`uvicorn main:app --host 0.0.0.0 --port $PORT`), so no override is needed.
