"""Health endpoints."""
from fastapi import APIRouter

from pekish import schemas


router = APIRouter()


@router.get("/ping", response_model=schemas.Status)
def ping() -> schemas.Status:
    """Return a Status based on the health of the app.

    Returns:
        schemas.Status: The status of the app.
    """
    return schemas.Status(message="ok")
