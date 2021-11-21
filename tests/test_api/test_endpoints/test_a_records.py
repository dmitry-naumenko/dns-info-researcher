"""Tests."""
import pytest
from fastapi import FastAPI, status
from httpx import AsyncClient

from app.core.config import get_app_settings
from app.models.schemas.responses import AResponse

settings = get_app_settings()


@pytest.mark.asyncio
async def test_a_records(mocker, app: FastAPI, async_client: AsyncClient):
    """Test a_records."""
    return_value = [AResponse(record="test")]
    mocker.patch(
        "app.api.api_v1.endpoints.a_records.get_a_response", return_value=return_value
    )
    url = app.url_path_for("a_records:get-a-records")

    response = await async_client.get(f"{url}?domain_name=test.com")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [return_value[0].dict()]
