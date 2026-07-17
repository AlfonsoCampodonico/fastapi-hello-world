"""Create and read greetings (backed by the in-memory store)."""

from fastapi import APIRouter, HTTPException, status

from app.models import Greeting, GreetingCreate, Message
from app.store import store

router = APIRouter(prefix="/api/v1/greetings", tags=["greetings"])


@router.get("", response_model=list[Greeting], summary="List greetings")
def list_greetings() -> list[Greeting]:
    """Return every greeting. Seeded with a hello from Laravel Cloud."""
    return store.list()


@router.post(
    "",
    response_model=Greeting,
    status_code=status.HTTP_201_CREATED,
    summary="Create a greeting",
)
def create_greeting(payload: GreetingCreate) -> Greeting:
    """Add a new greeting to the store and return it."""
    return store.add(payload)


@router.get(
    "/{greeting_id}",
    response_model=Greeting,
    summary="Get a greeting",
    responses={status.HTTP_404_NOT_FOUND: {"model": Message, "description": "Greeting not found"}},
)
def get_greeting(greeting_id: int) -> Greeting:
    """Fetch a single greeting by id, or return 404 if it does not exist."""
    greeting = store.get(greeting_id)
    if greeting is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Greeting {greeting_id} not found",
        )
    return greeting
