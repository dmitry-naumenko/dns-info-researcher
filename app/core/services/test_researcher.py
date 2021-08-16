"""Tests."""  # noqa: F401
import pytest

from ..models.response import MxResponse
from .researcher import get_mx_response


@pytest.mark.parametrize(
    "arguments",
    [
        ([".mx.mail.ru", 10], [".2mx.mail.ru", 20]),
        ([".3mx.mail.ru", 30],),
        (),
    ],
)
@pytest.mark.asyncio
async def test_get_mx_response(mocker, arguments):  # noqa: D103
    class TestClass:  # noqa: WPS431
        def __init__(self, exchange, preference):
            self.exchange = exchange
            self.preference = preference

    mocker.patch(
        "app.core.services.researcher.get_answers_from_domain",
        return_value=[TestClass(argument[0], argument[1]) for argument in arguments],
    )
    assert await get_mx_response("test.ru") == [
        MxResponse(host=argument[0], priority=argument[1]) for argument in arguments
    ]
