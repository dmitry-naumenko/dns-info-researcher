"""Production settings."""
from app.core.settings.app import AppSettings


class ProdAppSettings(AppSettings):
    """Prod settings."""

    cache_time = 120
