from fastapi import APIRouter

from app.api.v1.endpoints.user import router as user_router
from app.api.v1.endpoints.pbac import router as pbac_router

api_router = APIRouter()

api_router.include_router(
    prefix='/user',
    router=user_router,
    tags=['user']
)

api_router.include_router(
    prefix='/pbac',
    router=pbac_router,
    tags=['pbac']
)
