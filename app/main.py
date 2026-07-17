"""Application factory: assembles the FastAPI app and its OpenAPI metadata."""

from fastapi import FastAPI

from app import __version__
from app.routers import greetings, system

DESCRIPTION = """
A small **FastAPI** service that says hello from Laravel Cloud — and shows off
the auto-generated **OpenAPI** documentation.

* Interactive docs: **[/docs](/docs)** (Swagger UI) and **[/redoc](/redoc)**
* Raw schema: **[/openapi.json](/openapi.json)**
"""

TAGS_METADATA = [
    {"name": "system", "description": "Welcome and health endpoints."},
    {"name": "greetings", "description": "Create and read greetings (in-memory)."},
]


def create_app() -> FastAPI:
    app = FastAPI(
        title="Hello from Laravel Cloud",
        summary="A FastAPI hello-world with first-class OpenAPI docs.",
        description=DESCRIPTION,
        version=__version__,
        openapi_tags=TAGS_METADATA,
        contact={"name": "Laravel Cloud", "url": "https://cloud.laravel.com"},
        license_info={"name": "MIT"},
    )

    app.include_router(system.router)
    app.include_router(greetings.router)

    return app


app = create_app()
