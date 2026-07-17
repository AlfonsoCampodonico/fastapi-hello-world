"""Welcome and health endpoints."""

from fastapi import APIRouter

from app import __version__
from app.models import Health, Welcome

router = APIRouter(tags=["system"])


@router.get("/", response_model=Welcome, summary="Welcome message")
def read_root() -> Welcome:
    """Say hello and point at the interactive API docs."""
    return Welcome(
        message="Hello from Laravel Cloud 👋",
        service="fastapi-hello-world",
        version=__version__,
        docs="/docs",
    )


@router.get("/health", response_model=Health, summary="Health check")
def health() -> Health:
    """Liveness probe used by the platform and load balancers."""
    return Health(status="ok", version=__version__)
