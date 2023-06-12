from fastapi import APIRouter

from app.api import team


api_router = APIRouter(prefix="/api")
api_router.include_router(team.router, prefix="/team", tags=["team"])
