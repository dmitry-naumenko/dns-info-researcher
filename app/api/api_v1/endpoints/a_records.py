"""DNS researcher."""
from fastapi import APIRouter

from app.models.schemas.responses import AResponse
from app.services import researcher

from ...query_parameters import domain_name_parameter

router = APIRouter()


@router.get("", response_model=list[AResponse])
async def get_a_records(domain_name: str = domain_name_parameter):
    """Get A records."""
    return await researcher.get_a_response(domain_name)
