"""Models."""
from pydantic import BaseModel


class Response(BaseModel):
    """Response."""

    host: str
    priority: str


class MxResponse(Response):
    """MX response."""

    class Config:
        schema_extra = {
            "example": {"host": "alt4.aspmx.l.google.com.", "priority": "50"}
        }


class SimpleRecord(BaseModel):
    """A response."""

    record: str


class AResponse(SimpleRecord):
    """A response."""

    class Config:
        schema_extra = {"example": {"record": "74.125.131.113"}}


class AAAAResponse(SimpleRecord):
    """AAAA response."""

    class Config:
        schema_extra = {"example": {"record": "2a00:1450:4010:c02::71"}}
