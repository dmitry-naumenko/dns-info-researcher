"""Main."""
from fastapi import FastAPI, Query

from dns_researcher import get_a_response, get_mx_response
from dns_researcher.constants import MAX_URL_LENGTH, MIN_URL_LENGTH
from dns_researcher.responses import MxResponse, AResponse

app = FastAPI()


@app.get("/v1/get_mx_info/", response_model=list[MxResponse])
def get_mx_info(
        domain_name: str = Query(
            ...,
            min_length=MIN_URL_LENGTH,
            max_length=MAX_URL_LENGTH,
            example="google.com",
            description="Any domain name",
        )
):
    return get_mx_response(domain_name)


@app.get("/v1/get_a_info/", response_model=list[AResponse])
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
