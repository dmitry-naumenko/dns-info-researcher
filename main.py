"""Main."""
from fastapi import FastAPI, Query

from dns_researcher import get_mx_response
from dns_researcher.constants import MAX_URL_LENGTH, MIN_URL_LENGTH
from dns_researcher.responses import MxResponse

app = FastAPI()


@app.get("/v1/get_mx_info/")
def get_mx_info(
    domain_name: str = Query(
        ...,
        min_length=MIN_URL_LENGTH,
        max_length=MAX_URL_LENGTH,
        example="google.com",
        description="Any domain name",
    )
) -> dict[str, list[MxResponse]]:
    return {"mx_info": get_mx_response(domain_name)}
