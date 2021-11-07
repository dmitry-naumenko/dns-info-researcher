"""DNS researcher."""
from fastapi import APIRouter

from app.core.services import researcher
from app.models.schemas.responses import AAAAResponse

from ...query_parameters import domain_name_parameter

router = APIRouter()


@router.get("", response_model=list[AAAAResponse])
async def get_aaaa_records(domain_name: str = domain_name_parameter):
    """AAAA records."""
    return await researcher.get_aaaa_response(domain_name)
