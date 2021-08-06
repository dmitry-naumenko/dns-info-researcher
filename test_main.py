from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_mx_info(mocker):
    mocker.patch(
        "main.get_mx_response",
        return_value=[],
    )
    response = client.get("/v1/get_mx_info/?domain_name=google.com")
    assert response.status_code == 200
    assert response.json() == []
