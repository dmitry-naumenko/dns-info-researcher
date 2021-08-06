"""DNS responses."""

from dataclasses import dataclass


@dataclass
class MxResponse:
    """DNS MX reponse."""

    host: str
    priority: str
