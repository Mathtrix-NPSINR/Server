import secrets

from sqlalchemy.orm import Session

import app.models.api_key as api_key_models


def create_api_key(db: Session, user: str):
    db_api_key = api_key_models.APIKey(user=user, key=secrets.token_urlsafe(16))

    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)

    return db_api_key


def read_api_key(db: Session, key: str):
    db_api_key = (
        db.query(api_key_models.APIKey).filter(api_key_models.APIKey.key == key).first()
    )

    return db_api_key
