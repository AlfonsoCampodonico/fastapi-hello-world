# Hello from Laravel Cloud

A small but complete [FastAPI](https://fastapi.tiangolo.com/) service that says
**hello from Laravel Cloud** and shows off FastAPI's auto-generated **OpenAPI**
documentation.

## Endpoints

| Method | Path                       | Description                                   |
| ------ | -------------------------- | --------------------------------------------- |
| GET    | `/`                        | Welcome message ("Hello from Laravel Cloud")  |
| GET    | `/health`                  | Health check (used by the platform probe)     |
| GET    | `/api/v1/greetings`        | List all greetings (seeded)                   |
| POST   | `/api/v1/greetings`        | Create a greeting                             |
| GET    | `/api/v1/greetings/{id}`   | Get a greeting by id (404 if missing)         |
| GET    | `/docs`                    | Swagger UI (interactive OpenAPI docs)         |
| GET    | `/redoc`                   | ReDoc (alternative docs)                      |
| GET    | `/openapi.json`            | Raw OpenAPI schema                            |

The request/response shapes are defined as Pydantic models in
[`app/models.py`](app/models.py), so they show up fully typed in the OpenAPI
schema and docs.

## Project structure

```
main.py                    # entrypoint (re-exports app so `uvicorn main:app` works)
app/
├── __init__.py            # __version__
├── main.py                # create_app(): FastAPI + OpenAPI metadata + routers
├── models.py              # Pydantic models (drive the OpenAPI schema)
├── store.py               # in-memory greeting store
└── routers/
    ├── system.py          # /, /health
    └── greetings.py       # /api/v1/greetings ...
tests/test_app.py          # pytest + FastAPI TestClient
```

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

uvicorn main:app --reload
```

Open <http://127.0.0.1:8000> for the welcome message, or
<http://127.0.0.1:8000/docs> for the interactive API docs.

## Tests

```bash
pip install -r requirements-dev.txt
pytest
```

## Run with Docker

```bash
docker build -t fastapi-hello-world .
docker run -p 8000:8000 fastapi-hello-world
```

## Deployment

The app reads the port from `$PORT` (default `8000`). The start command is:

```bash
uvicorn main:app --host '' --port ${PORT}
```

> **Why `--host ''`?** On IPv6 / dual-stack hosts (e.g. Laravel Cloud), the
> platform health probe connects to the pod's IPv6 address, while the in-pod
> proxy reaches the app over IPv4 loopback — the app must serve both. `--host ''`
> (empty) binds all interfaces on **both** families (separate IPv4 + IPv6
> sockets), whereas `--host ::` is IPv6-only and `--host 0.0.0.0` is IPv4-only.

On Laravel Cloud this matches the auto-detected default start command, so no
override is needed.
