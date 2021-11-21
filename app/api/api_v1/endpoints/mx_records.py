"""DNS researcher."""
from fastapi import APIRouter

from app.core.config import cache
from app.models.schemas.responses import MxResponse
from app.services import researcher

from ....core.config import get_app_settings
from ...query_parameters import domain_name_parameter

settings = get_app_settings()

router = APIRouter()


@router.get(
    "",
    response_model=list[MxResponse],
    summary="Get MX records",
    description="A DNS MX record directs email to a mail server. ",
    name="mx_records:get-mx-records",
)
@cache(expire=settings.cache_time)
async def get_mx_records(domain_name: str = domain_name_parameter):
    """Get MX records."""
    return await researcher.get_mx_response(domain_name)
