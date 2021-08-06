import pytest
from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_mx_info_valid(mocker):
    mocker.patch(
        "main.get_mx_response",
        return_value=[],
    )
    response = client.get("/v1/get_mx_info/?domain_name=google.com")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


@pytest.mark.parametrize(
    "domain_name",
    ["y.ru", "{long_text}.ru".format(long_text="a" * 100), "", None],
)
def test_get_mx_info_invalid_domain_length(mocker, domain_name):
    response = client.get(f"/v1/get_mx_info/?domain_name={domain_name}")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
