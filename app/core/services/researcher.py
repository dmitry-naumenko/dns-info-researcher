"""Researcher."""

from dns import asyncresolver, resolver

from ..models.response import AAAAResponse, AResponse, MxResponse
from .constants import DnsTypes


async def get_answers_from_domain(domain: str, dns_record_type: DnsTypes) -> list:
    """Get answers from domain.

    Args:
        domain (str): [description]
        dns_record_type (DnsTypes): [description]

    Returns:
        list: [description]
    """
    try:
        return list(await asyncresolver.resolve(domain, dns_record_type.value))
    except resolver.NoAnswer:
        return []
    except resolver.NXDOMAIN:
        return []


async def get_mx_response(domain: str) -> list[MxResponse]:
    """Get mx response.

    Args:
        domain (str): domain name

    Returns:
        list[MxResponse]: result
    """
    answers: list = await get_answers_from_domain(domain, DnsTypes.MX)
    return [
        MxResponse(host=str(rdata.exchange), priority=rdata.preference)
        for rdata in answers
    ]


async def get_a_response(domain: str) -> list[AResponse]:
    """Get a response.

    Args:
        domain (str): domain name

    Returns:
        list[AResponse]: result
    """
    answers: list = await get_answers_from_domain(domain, DnsTypes.A)
    return [AResponse(record=str(record)) for record in answers]


async def get_aaaa_response(domain: str) -> list[AAAAResponse]:
    """Get AAAA response.

    Args:
        domain (str): domain name

    Returns:
        list[AAAAResponse]: result
    """
    answers: list = await get_answers_from_domain(domain, DnsTypes.AAAA)
    return [AAAAResponse(record=str(record)) for record in answers]
