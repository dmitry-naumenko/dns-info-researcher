"""Tests."""  # noqa: F401
import pytest
from dns import resolver

from app.models.schemas.responses import AAAAResponse, AResponse, MxResponse
from app.services import researcher
from app.services.constants import DnsTypes


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
        "app.services.researcher.get_answers_from_domain",
        return_value=[TestClass(argument[0], argument[1]) for argument in arguments],
    )
    assert await researcher.get_mx_response("test.ru") == [
        MxResponse(host=argument[0], priority=argument[1]) for argument in arguments
    ]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "function, model, result_record",
    [
        (researcher.get_a_response, AResponse, "64.233.165.101"),
        (researcher.get_aaaa_response, AAAAResponse, "2a00:1450:4010:c08::66"),
    ],
)
async def test_get_record_type_response(  # noqa: D103
    mocker, function, model, result_record
):
    mocker.patch(
        "app.services.researcher.get_answers_from_domain",
        return_value=[result_record],
    )
    assert await function("test.ru") == [model(record=result_record)]


@pytest.mark.asyncio
async def test_get_answers_from_domain_exception_noanswer(mocker):
    mocker.patch("dns.asyncresolver.resolve", side_effect=resolver.NoAnswer)
    assert await researcher.get_answers_from_domain("google1.com", DnsTypes.A) == []


@pytest.mark.asyncio
async def test_get_answers_from_domain_exception_nxdomain(mocker):
    mocker.patch("dns.asyncresolver.resolve", side_effect=resolver.NXDOMAIN)
    assert (
        await researcher.get_answers_from_domain("go123123ogle1.com", DnsTypes.A) == []
    )
