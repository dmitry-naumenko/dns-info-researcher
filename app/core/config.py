"""Configs."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings."""

    API_V1_STR = "/api/v1"
    PROJECT_NAME: str

    class Config:
        case_sensitive = True


settings = Settings()
