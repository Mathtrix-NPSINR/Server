from fastapi import APIRouter

from app.api import event, team, user

api_router = APIRouter(prefix="/api")
api_router.include_router(event.router, prefix="/event", tags=["event"])
api_router.include_router(team.router, prefix="/team", tags=["team"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
