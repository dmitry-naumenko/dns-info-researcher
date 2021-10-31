"""Tests."""
import pytest
from fastapi import status

from app.core.config import API_V1_STR


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
        f"{API_V1_STR}/{api_method_name}/?domain_name=valid_domain_length.com"
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []  # noqa: WPS520


@pytest.mark.parametrize(
    "domain_name",
    ["y.ru", "{long_text}.ru".format(long_text="a" * 100), "", None],
)
def test_get_mx_info_invalid_domain_length(client, mocker, domain_name):
    """Test get MX info invalid domain length."""
    response = client.get(f"{API_V1_STR}/mx_records/?domain_name={domain_name}")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
