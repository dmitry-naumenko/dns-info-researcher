"""Config."""
from functools import lru_cache, wraps
from typing import Dict, Type

from fastapi_cache.decorator import cache as fastapi_cache

from app.core.settings.app import AppSettings
from app.core.settings.base import AppEnvTypes, BaseAppSettings
from app.core.settings.development import DevAppSettings
from app.core.settings.production import ProdAppSettings
from app.core.settings.test import TestAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
    AppEnvTypes.test: TestAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    """Get app settings.

    Returns:
        AppSettings: settings
    """
    app_env = BaseAppSettings().app_env
    config = environments[app_env]

    return config()


def do_nothing(expire: int):
    """Do nothing decorator.

    Args:
        expire (int): expire

    Returns:
        decorator
    """

    def wrapper(func):
        @wraps(func)
        async def inner(*args, **kwargs):
            return await func(*args, **kwargs)

        return inner

    return wrapper


cache = do_nothing if get_app_settings().app_env == AppEnvTypes.test else fastapi_cache
