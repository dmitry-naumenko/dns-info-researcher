"""DNS responses."""
from pydantic import BaseModel


class MxResponse(BaseModel):
    """MX response."""

    host: str
    priority: str
