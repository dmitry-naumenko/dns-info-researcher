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


class AResponse(Response):
    """A response."""

    host: str
    priority: str
