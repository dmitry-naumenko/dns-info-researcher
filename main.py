"""Main."""
from fastapi import FastAPI

from dns_researcher import get_mx_response
from dns_researcher.responses import MxResponse

app = FastAPI()


@app.get("/v1/get_mx_info/{domain_name}")
def get_mx_info(domain_name: str) -> dict[str, list[MxResponse]]:
    """Get mx info.

    Args:
        domain_name (str): your domain_name, for example, google.com

    Returns:
        dict[str, list[MxResponse]]: mx_info
    """
    return {"mx_info": get_mx_response(domain_name)}
