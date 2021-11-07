"""API v1 root."""
from fastapi import APIRouter

from ..endpoints import a_records, aaaa_records, mx_records

router = APIRouter()
router.include_router(mx_records.router, prefix="/mx_records", tags=["mx records"])
router.include_router(a_records.router, prefix="/a_records", tags=["a records"])
router.include_router(
    aaaa_records.router, prefix="/aaaa_records", tags=["aaaa records"]
)
