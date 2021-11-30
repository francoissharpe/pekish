from typing import Optional

from fastapi import FastAPI

from pekish.routes import router


def create_app(version: Optional[str] = "0.0.0") -> FastAPI:

    app = FastAPI(version=version)

    app.include_router(router)

    return app
