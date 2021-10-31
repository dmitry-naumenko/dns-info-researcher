"""DNS researcher."""
from fastapi import APIRouter

from app.core.models.response import AAAAResponse
from app.core.services import researcher

from ..query_parameters import domain_name_parameter

router = APIRouter()


@router.get("/aaaa_records", response_model=list[AAAAResponse], tags=["AAAA"])
async def get_aaaa_records(domain_name: str = domain_name_parameter):
    """AAAA records."""
    return await researcher.get_aaaa_response(domain_name)
