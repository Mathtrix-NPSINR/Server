from fastapi import APIRouter, Depends, HTTPException, Security
from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from yagmail.oauth2 import base64

from app.core.api_key import get_api_key
from app.core.db import get_db
from app.core.mail import send_email
from app.core.qr_code import create_qr_code
from app.crud.user import (
    create_user,
    delete_user,
    read_user,
    update_user,
    update_user_attendance,
)
from app.schemas.user import User, UserCreate, UserUpdate

router = APIRouter()


@router.post("/", response_model=User)
async def create_user_endpoint(
        *, db: Session = Depends(get_db), api_key=Security(get_api_key), user: UserCreate
):
    try:
        db_user = create_user(db=db, user=user)

        if db_user.user_attendance is True:
            logger.info(
                f"{api_key.user} registered a new user on spot with the user id {db_user.id}"
            )
            return db_user

        qr_code_path = create_qr_code(id=db_user.id)

        send_email(
            target_email=[user.user_email],
            subject="You have successfully registered",
            body=f"Welcome, {user.user_name}! Thank you for registering for Mathtrix! On the day of the event, "
                 f"you'll need to show this QR code at the registration desk to complete your registration on site. "
                 f"Please save this QR code as it cannot be issued again.",
            attachments=[qr_code_path],
        )

        logger.info(
            f"{api_key.user} registered a new user with the user id {db_user.id}"
        )

        return db_user

    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail=f"A user with the email {user.user_email} already exists!",
        )


@router.get("/", response_model=User)
async def get_user_endpoint(
        *, db: Session = Depends(get_db), api_key=Security(get_api_key), user_id: int
):
    db_user = read_user(db=db, user_id=user_id)

    if not db_user:
        raise HTTPException(
            status_code=404, detail=f"A user with the id {user_id} does not exist!"
        )

    logger.info(f"{api_key.user} read the details of user id {db_user.id}")

    return db_user


@router.put("/", response_model=User)
async def update_user_endpoint(
        *,
        db: Session = Depends(get_db),
        user_id: int,
        api_key=Security(get_api_key),
        user: UserUpdate,
):
    db_user = read_user(db=db, user_id=user_id)

    if not db_user:
        raise HTTPException(
            status_code=404, detail=f"A user with the id {user_id} does not exist!"
        )

    logger.info(f"{api_key.user} updated the details of user id {db_user.id}")

    return update_user(db=db, user_id=user_id, user=user)


@router.delete("/")
async def delete_user_endpoint(
        *, db: Session = Depends(get_db), api_key=Security(get_api_key), user_id: int
):
    db_user = read_user(db=db, user_id=user_id)

    if not db_user:
        raise HTTPException(
            status_code=404, detail=f"A user with the id {user_id} does not exist!"
        )

    logger.info(f"{api_key.user} deleted user id {db_user.id}")

    return delete_user(db=db, user_id=user_id)


@router.put("/attendance")
async def update_user_attendance_endpoint(
        *,
        db: Session = Depends(get_db),
        api_key=Security(get_api_key),
        user_id_encoded: str,
):
    user_id = int(base64.b64decode(user_id_encoded.encode("utf-8")).decode("utf-8"))

    db_user = read_user(db=db, user_id=user_id)

    if not db_user:
        raise HTTPException(
            status_code=404, detail=f"A user with the id {user_id} does not exist!"
        )

    logger.info(f"{api_key.user} updated the attendance of {db_user.user_name}")

    return update_user_attendance(db=db, user_id=user_id)
