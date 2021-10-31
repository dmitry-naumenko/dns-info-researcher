"""DNS researcher."""
from fastapi import APIRouter

from app.core.models.response import AResponse
from app.core.services import researcher

from ..query_parameters import domain_name_parameter

router = APIRouter()


@router.get("/a_records", response_model=list[AResponse], tags=["A"])
async def get_a_records(domain_name: str = domain_name_parameter):
    """Get A records."""
    return await researcher.get_a_response(domain_name)
