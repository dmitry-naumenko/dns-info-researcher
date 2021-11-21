"""Tests."""
import pytest
from fastapi import FastAPI, status
from httpx import AsyncClient

from app.core.config import get_app_settings

settings = get_app_settings()


@pytest.mark.asyncio
async def test_a_records(app: FastAPI, async_client: AsyncClient):
    """Test a_records."""
    url = app.url_path_for("a_records:get-a-records")
    response = await async_client.get(f"{url}?domain_name=google.com")
    assert response.status_code == status.HTTP_200_OK
    assert "record" in response.json()[0]


@pytest.mark.asyncio
async def test_aaaa_records(app: FastAPI, async_client: AsyncClient):
    """Test a_records."""
    url = app.url_path_for("aaaa_records:get-aaaa-records")
    response = await async_client.get(f"{url}?domain_name=google.com")
    assert response.status_code == status.HTTP_200_OK
    assert "record" in response.json()[0]


@pytest.mark.asyncio
async def test_mx_records(app: FastAPI, async_client: AsyncClient):
    """Test a_records."""
    url = app.url_path_for("mx_records:get-mx-records")
    response = await async_client.get(f"{url}?domain_name=google.com")
    assert response.status_code == status.HTTP_200_OK
    assert "host" in response.json()[0]
