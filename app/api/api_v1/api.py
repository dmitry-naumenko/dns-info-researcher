"""API v1 root."""
from fastapi import APIRouter

from .endpoints.a_record import router as a_record_router
from .endpoints.aaaa_record import router as aaaa_record_router
from .endpoints.mx_record import router as mx_record_router

router = APIRouter()
router.include_router(mx_record_router)
router.include_router(a_record_router)
router.include_router(aaaa_record_router)
