from fastapi import APIRouter, Depends, Security
from loguru import logger
from sqlalchemy.orm import Session

from app.core.api_key import get_api_key
from app.core.db import get_db
from app.crud.api_key import create_api_key

router = APIRouter()


@router.post("/", response_model=dict)
async def create_api_key_endpoint(*, db: Session = Depends(get_db), user: str):
    logger.info(f"Creating a new API key for {user}!")
    return create_api_key(db=db, user=user).__dict__


@router.get("/")
async def check_api_key_endpoint(*, api_key=Security(get_api_key)):
    logger.info(f"{api_key.user} has successfully logged in!")
    return api_key
