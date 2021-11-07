"""Tests."""
from typing import Final, Tuple

import pytest
from fastapi import status

from ....core.config import settings

TOO_BIG_DOMAIN_NAME: Final[str] = "{long_text}.ru".format(long_text="a" * 100)
TOO_SMALL_DOMAIN_NAME: Final[str] = "y.ru"
EMPTY_DOMAIN_NAME = ""
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
        f"app.core.services.researcher.{api_function_name}",
        return_value=[],
    )
    response = client.get(
        f"{settings.API_V1_STR}/{api_method_name}/?domain_name=valid_domain_length.com"
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []  # noqa: WPS520


@pytest.mark.parametrize("domain_name", INVALID_DOMAIN_NAMES)
def test_get_mx_info_invalid_domain_length(client, domain_name):
    """Test get MX info invalid domain length."""
    # TODO: add all methods checking, not only MX
    response = client.get(
        f"{settings.API_V1_STR}/mx_records/?domain_name={domain_name}"
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
