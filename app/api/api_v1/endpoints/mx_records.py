"""DNS researcher."""
from fastapi import APIRouter

from app.models.schemas.responses import MxResponse
from app.services import researcher

from ...query_parameters import domain_name_parameter

router = APIRouter()


@router.get("", response_model=list[MxResponse])
async def get_mx_records(domain_name: str = domain_name_parameter):
    """MX records."""
    return await researcher.get_mx_response(domain_name)
