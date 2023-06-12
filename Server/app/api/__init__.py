from fastapi import APIRouter

from app.api import team, user

api_router = APIRouter(prefix="/api")
api_router.include_router(team.router, prefix="/team", tags=["team"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
