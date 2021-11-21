"""Tests."""
from typing import Final, Tuple

import pytest
from fastapi import status

from app.core.config import get_app_settings

settings = get_app_settings()

TOO_BIG_DOMAIN_NAME: Final[str] = "{long_text}.ru".format(long_text="a" * 100)
TOO_SMALL_DOMAIN_NAME: Final[str] = "y.ru"
EMPTY_DOMAIN_NAME: Final[str] = ""
INVALID_DOMAIN_NAMES: Tuple[str, str, str] = (
    TOO_BIG_DOMAIN_NAME,
    TOO_SMALL_DOMAIN_NAME,
    EMPTY_DOMAIN_NAME,
)


@pytest.mark.parametrize(
    "api_method_name, api_function_name",
    [
        ("mx_records", "get_mx_response"),
        ("a_records", "get_a_response"),
        ("aaaa_records", "get_aaaa_response"),
    ],
)
def test_get_records_with_valid_domain(
    client, mocker, api_method_name, api_function_name
):
    """Test get records with valid domain."""
    mocker.patch(
        f"app.services.researcher.{api_function_name}",
        return_value=[],
    )
    response = client.get(
        f"{settings.api_v1_str}/{api_method_name}/?domain_name=valid_domain_length.com"
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []  # noqa: WPS520


@pytest.mark.parametrize("domain_name", INVALID_DOMAIN_NAMES)
def test_get_mx_info_invalid_domain_length(app, client, domain_name):
    """Test get MX info invalid domain length."""
    url = app.url_path_for("a_records:get-a-records")
    response = client.get(f"{url}?domain_name={domain_name}")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
