"""Application factory: assembles the FastAPI app and its OpenAPI metadata."""

from fastapi import FastAPI
from fastapi.openapi.docs import get_redoc_html
from fastapi.responses import HTMLResponse

from app import __version__
from app.routers import greetings, system

# FastAPI's built-in ReDoc points at the `redoc@next` CDN tag, which jsdelivr no
# longer resolves (404) — so the default /redoc renders blank. Serve it ourselves
# from a pinned, valid ReDoc release instead.
REDOC_JS_URL = "https://cdn.jsdelivr.net/npm/redoc@2/bundles/redoc.standalone.js"

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
        redoc_url=None,  # replaced by the pinned-version route below
    )

    @app.get("/redoc", include_in_schema=False)
    def redoc_html() -> HTMLResponse:
        return get_redoc_html(
            openapi_url=app.openapi_url,
            title=f"{app.title} - ReDoc",
            redoc_js_url=REDOC_JS_URL,
        )

    app.include_router(system.router)
    app.include_router(greetings.router)

    return app


app = create_app()
