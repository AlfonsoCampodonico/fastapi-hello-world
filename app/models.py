"""Pydantic models. These double as the OpenAPI schema shown at /docs."""

from datetime import datetime

from pydantic import BaseModel, Field


class Welcome(BaseModel):
    """Root welcome response."""

    message: str = Field(..., examples=["Hello from Laravel Cloud 👋"])
    service: str = Field(..., examples=["fastapi-hello-world"])
    version: str = Field(..., examples=["1.0.0"])
    docs: str = Field(..., description="Path to the interactive API docs.", examples=["/docs"])


class Health(BaseModel):
    """Health-check response."""

    status: str = Field(..., examples=["ok"])
    version: str = Field(..., examples=["1.0.0"])


class Greeting(BaseModel):
    """A greeting stored by the API."""

    id: int = Field(..., description="Unique identifier.", examples=[1])
    message: str = Field(..., description="The greeting text.", examples=["Hello from Laravel Cloud 👋"])
    language: str = Field(..., description="ISO 639-1 language code.", examples=["en"])
    created_at: datetime = Field(..., description="Creation time (UTC).")


class GreetingCreate(BaseModel):
    """Payload for creating a greeting."""

    message: str = Field(
        ...,
        min_length=1,
        max_length=280,
        description="The greeting text.",
        examples=["Bonjour depuis Laravel Cloud"],
    )
    language: str = Field(
        default="en",
        min_length=2,
        max_length=5,
        description="ISO 639-1 language code.",
        examples=["fr"],
    )


class Message(BaseModel):
    """Generic message response (used for errors)."""

    detail: str = Field(..., examples=["Greeting 42 not found"])
