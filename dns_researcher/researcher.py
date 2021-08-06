"""Researcher."""

from dns import resolver

from dns_researcher.constants import DnsTypes
from dns_researcher.responses import MxResponse


def get_answers_from_domain(domain: str, dns_record_type: DnsTypes) -> resolver.Answer:
    """Get answers from domain.

    Args:
        domain (str): [description]
        dns_record_type (DnsTypes): [description]

    Returns:
        resolver.Answer: [description]
    """
    return resolver.query(domain, dns_record_type.value)


def get_mx_response(domain: str) -> list[MxResponse]:
    """Get mx response.

    Args:
        domain (str): domain name

    Returns:
        list[MxResponse]: result
    """
    answers = get_answers_from_domain(domain, DnsTypes.mx)
    return [
        MxResponse(host=str(rdata.exchange), priority=rdata.preference)
        for rdata in answers
    ]
