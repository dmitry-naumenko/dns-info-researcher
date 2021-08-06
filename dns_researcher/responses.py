"""DNS responses."""
from pydantic import BaseModel


class MxResponse(BaseModel):
    """MX response."""

    host: str
    priority: str


class AResponse(BaseModel):
    """A response."""

    host: str
    priority: str
