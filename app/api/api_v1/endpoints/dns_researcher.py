"""DNS researcher."""
from fastapi import APIRouter, Query

from app.core.models.response import AResponse, MxResponse
from app.core.services.constants import MAX_URL_LENGTH, MIN_URL_LENGTH
from app.core.services.researcher import get_a_response, get_mx_response

router = APIRouter()


@router.get("/get_mx_info", response_model=list[MxResponse], tags=["MX"])
def get_mx_info(
    domain_name: str = Query(
        ...,
        min_length=MIN_URL_LENGTH,
        max_length=MAX_URL_LENGTH,
        example="google.com",
        summary="Get mx info by domain",
        description="Very good thing",
    )
):
    return get_mx_response(domain_name)


@router.get("/get_a_info", response_model=list[AResponse])
def get_a_info(
    domain_name: str = Query(
        ...,
        min_length=MIN_URL_LENGTH,
        max_length=MAX_URL_LENGTH,
        example="google.com",
        description="Any domain name",
    )
):
    return get_a_response(domain_name)
