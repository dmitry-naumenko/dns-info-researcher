"""Main."""
import aioredis
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from starlette.middleware.cors import CORSMiddleware

from app.core.settings.base import AppEnvTypes

from .api.api_v1.endpoints.api import router as api_router
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


@app.on_event("startup")
async def startup():  # pragma: no cover
    """Set up statrup."""
    if get_app_settings().app_env == AppEnvTypes.test:
        return
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf8", decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
