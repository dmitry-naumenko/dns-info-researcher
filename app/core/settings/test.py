"""Test settings."""
import logging

from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    """Test settings."""

    debug: bool = True

    title: str = "Random"

    logging_level: int = logging.DEBUG
