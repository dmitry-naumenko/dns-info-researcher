"""Models."""
from pydantic import BaseModel


class Response(BaseModel):
    """Response."""

    host: str
    priority: str


class MxResponse(Response):
    """MX response."""

    host: str
    priority: str


class SimpleRecord(BaseModel):
    """A response."""

    record: str


class AResponse(SimpleRecord):
    """A response."""


class AAAAResponse(SimpleRecord):
    """AAAA response."""
