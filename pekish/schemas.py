"""Schemas module."""
from pydantic import BaseModel


class Status(BaseModel):
    """Status message schema."""

    message: str
