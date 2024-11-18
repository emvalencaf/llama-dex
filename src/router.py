from fastapi import APIRouter

# modules
from dex.router import router as dex_router

api_router = APIRouter()

api_router.include_router(router=dex_router,
                          prefix='/dex')