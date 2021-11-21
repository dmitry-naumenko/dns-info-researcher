"""App settings."""

import logging
from typing import Any, Dict, List, Tuple

from app.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    """App settings."""

    debug: bool = False
    description: str = "A tool for getting DNS information."
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str
    version: str = "0.1.0"

    api_prefix: str = "/api"
    api_v1_str = "/api/v1"

    allowed_hosts: List[str] = ["*"]

    logging_level: int = logging.INFO
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    cache_time: int = 1

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        """Fastapi kwargs.

        Returns:
            Dict[str, Any]: Fastapi kwargs
        """
        return {
            "description": self.description,
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
