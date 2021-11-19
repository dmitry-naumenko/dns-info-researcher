"""DNS researcher."""
from fastapi import APIRouter

from app.models.schemas.responses import AAAAResponse
from app.services import researcher

from ...query_parameters import domain_name_parameter

router = APIRouter()


@router.get(
    "",
    response_model=list[AAAAResponse],
    summary="Get AAAA records",
    description="AAAA records are DNS records that use an IPv6 address to connect a domain to a website",
)
async def get_aaaa_records(domain_name: str = domain_name_parameter):
    """AAAA records."""
    return await researcher.get_aaaa_response(domain_name)
