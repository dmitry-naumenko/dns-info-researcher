"""Main."""
from fastapi import FastAPI

from .api.api_v1.api import router as api_router
from .core.config import API_V1_STR, PROJECT_NAME

app = FastAPI(title=PROJECT_NAME, description="Get DNS records")
app.include_router(api_router, prefix=API_V1_STR)
