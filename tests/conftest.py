# flake8: noqa

from os import environ

import pytest
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import AsyncClient

environ["APP_ENV"] = "test"


@pytest.fixture
def app() -> FastAPI:
    """App."""
    from app.main import get_application  # type: ignore

    return get_application()


@pytest.fixture(scope="module")
def client():
    """Sync client."""
    from app.main import app

    with TestClient(app) as client_obj:
        yield client_obj


@pytest.fixture
async def initialized_app(app: FastAPI):
    """Initialized app."""
    async with LifespanManager(app):
        yield app


@pytest.fixture
async def async_client(initialized_app: FastAPI):
    """Async client."""
    async with AsyncClient(
        app=initialized_app,
        base_url="http://testserver",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client
