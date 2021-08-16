"""DNS researcher."""
from fastapi import APIRouter, Query

from app.core.models.response import AAAAResponse, AResponse, MxResponse
from app.core.services import researcher
from app.core.services.constants import MAX_URL_LENGTH, MIN_URL_LENGTH

router = APIRouter()


@router.get("/mx_records", response_model=list[MxResponse], tags=["MX"])
async def get_mx_info(
    domain_name: str = Query(
        ...,
        min_length=MIN_URL_LENGTH,
        max_length=MAX_URL_LENGTH,
        example="google.com",
        summary="Get mx info by domain",
        description="Very good thing",
    )
):
    return await researcher.get_mx_response(domain_name)


@router.get("/a_records", response_model=list[AResponse], tags=["A"])
async def get_a_info(
    domain_name: str = Query(
        ...,
        min_length=MIN_URL_LENGTH,
        max_length=MAX_URL_LENGTH,
        example="google.com",
        description="Any domain name",
    )
):
    return await researcher.get_a_response(domain_name)


@router.get("/aaaa_records", response_model=list[AAAAResponse], tags=["AAAA"])
async def get_aaaa_info(
    domain_name: str = Query(
        ...,
        min_length=MIN_URL_LENGTH,
        max_length=MAX_URL_LENGTH,
        example="google.com",
        description="Any domain name",
    )
):
    return await researcher.get_aaaa_response(domain_name)
