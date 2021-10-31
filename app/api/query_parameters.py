"""Query parameters."""

from fastapi import Query

from app.api.constants import MAX_URL_LENGTH, MIN_URL_LENGTH

domain_name_parameter = Query(
    ...,
    min_length=MIN_URL_LENGTH,
    max_length=MAX_URL_LENGTH,
    example="google.com",
)
