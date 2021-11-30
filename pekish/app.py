"""App module."""
from typing import Optional

from fastapi import FastAPI

from pekish.routes import router


def create_app(version: Optional[str] = "0.0.0") -> FastAPI:
    """Create an application.

    Args:
        version (Optional[str], optional): Version of the application.
            Defaults to "0.0.0".

    Returns:
        FastAPI: The created application.
    """
    app = FastAPI(version=version)

    app.include_router(router)

    return app
