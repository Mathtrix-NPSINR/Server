from fastapi import Depends, HTTPException, Security, status
from fastapi.security import APIKeyQuery
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.crud.api_key import read_api_key

api_key = APIKeyQuery(name="api-key", auto_error=False)


def get_api_key(api_key: str = Security(api_key), db: Session = Depends(get_db)) -> str:
    db_api_key = read_api_key(db=db, key=api_key)

    if not db_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key!",
        )

    return db_api_key
