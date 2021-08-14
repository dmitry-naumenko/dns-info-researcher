import pytest
from fastapi import status

from app.core.config import API_V1_STR


def test_get_mx_info_valid(client, mocker):
    mocker.patch(
        "app.api.api_v1.endpoints.dns_researcher.get_mx_response",
        return_value=[],
    )
    response = client.get(f"{API_V1_STR}/mx_records/?domain_name=google.com")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


@pytest.mark.parametrize(
    "domain_name",
    ["y.ru", "{long_text}.ru".format(long_text="a" * 100), "", None],
)
def test_get_mx_info_invalid_domain_length(client, mocker, domain_name):
    response = client.get(f"{API_V1_STR}/a_records/?domain_name={domain_name}")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
