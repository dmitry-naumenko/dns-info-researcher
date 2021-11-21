"""Caching."""
from functools import wraps

from fastapi_cache.decorator import cache as fastapi_cache

from app.core.settings.base import AppEnvTypes

from .config import get_app_settings


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
