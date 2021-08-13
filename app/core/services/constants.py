"""Constants."""
from enum import Enum
from typing import Final

MIN_URL_LENGTH: Final[int] = 5
MAX_URL_LENGTH: Final[int] = 50


class DnsTypes(Enum):
    """DnsTypes."""

    MX = "MX"
    A = "A"  # noqa: WPS111
