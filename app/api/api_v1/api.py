"""API v1 root."""
from fastapi import APIRouter

from .endpoints.dns_researcher import router as dns_router

router = APIRouter()
router.include_router(dns_router)
