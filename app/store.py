"""A tiny thread-safe, in-memory greeting store.

State resets on restart — that's fine for a demo. Swap this out for a real
database (and dependency-inject it into the routers) when you need persistence.
"""

from __future__ import annotations

from datetime import datetime, timezone
from itertools import count
from threading import Lock

from app.models import Greeting, GreetingCreate


class GreetingStore:
    def __init__(self) -> None:
        self._items: dict[int, Greeting] = {}
        self._ids = count(1)
        self._lock = Lock()
        # Seed with the greeting this whole app exists to deliver.
        self.add(GreetingCreate(message="Hello from Laravel Cloud 👋", language="en"))

    def add(self, data: GreetingCreate) -> Greeting:
        with self._lock:
            greeting = Greeting(
                id=next(self._ids),
                message=data.message,
                language=data.language,
                created_at=datetime.now(timezone.utc),
            )
            self._items[greeting.id] = greeting
            return greeting

    def list(self) -> list[Greeting]:
        with self._lock:
            return list(self._items.values())

    def get(self, greeting_id: int) -> Greeting | None:
        with self._lock:
            return self._items.get(greeting_id)


store = GreetingStore()
