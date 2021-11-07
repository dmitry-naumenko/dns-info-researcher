"""Main."""
from fastapi import FastAPI

from .api.api_v1.api import router as api_router
from .core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, description="Get DNS records")
app.include_router(api_router, prefix=settings.API_V1_STR)
