from fastapi import FastAPI
from loguru import logger

from app.api import api_router
from app.core.db import Base, engine
from app.core.settings import settings

logger.add("mathtrix.log", enqueue=True)

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router)
