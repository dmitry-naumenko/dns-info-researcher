"""DNS researcher."""
from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.models.schemas.responses import AResponse
from app.services import researcher

from ....core.config import settings
from ...query_parameters import domain_name_parameter

router = APIRouter()


@router.get(
    "",
    response_model=list[AResponse],
    summary="Get A records",
    description="An A record is a type of DNS record "
    "that points a domain to an IP address",
)
@cache(expire=settings.cache_time)
async def get_a_records(domain_name: str = domain_name_parameter):
    """Get A records."""
    return await researcher.get_a_response(domain_name)
