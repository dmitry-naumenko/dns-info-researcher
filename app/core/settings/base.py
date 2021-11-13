"""Base settings."""
from enum import Enum

from pydantic import BaseSettings


class AppEnvTypes(Enum):
    """App types."""

    prod = "prod"
    dev = "dev"
    test = "test"


class BaseAppSettings(BaseSettings):
    """Base app settings."""

    app_env: AppEnvTypes = AppEnvTypes.prod

    class Config:
        case_sensitive = False
