"""Constants."""
from enum import Enum


class DnsTypes(Enum):
    """DnsTypes."""

    MX = "MX"
    AAAA = "AAAA"
    A = "A"  # noqa: WPS111
