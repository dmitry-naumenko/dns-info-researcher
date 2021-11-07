"""Main."""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .api.api_v1.api import router as api_router
from .core.config import get_app_settings


def get_application() -> FastAPI:
    """Get application.

    Returns:
        FastAPI: an app obj
    """
    settings = get_app_settings()

    app = FastAPI(**settings.fastapi_kwargs)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix=settings.api_v1_str)

    return app


app = get_application()
