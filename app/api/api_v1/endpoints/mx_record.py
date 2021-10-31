"""DNS researcher."""
from fastapi import APIRouter

from app.core.models.response import MxResponse
from app.core.services import researcher

from ...query_parameters import domain_name_parameter

router = APIRouter()


@router.get("/mx_records", response_model=list[MxResponse], tags=["MX"])
async def get_mx_records(domain_name: str = domain_name_parameter):
    """MX records."""
    return await researcher.get_mx_response(domain_name)
