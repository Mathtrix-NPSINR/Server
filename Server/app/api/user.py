from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.mail import send_email
from app.core.qr_code import create_qr_code
from app.crud.user import create_user, delete_user, read_user, update_user
from app.schemas.user import User, UserCreate, UserUpdate

router = APIRouter()


@router.post("/", response_model=User)
async def create_user_endpoint(*, db: Session = Depends(get_db), user: UserCreate):
    try:
        db_user = create_user(db=db, user=user)

        qr_code_path = create_qr_code(id=db_user.id)

        send_email(
            target_email=[user.user_email],
            subject="You have successfully registered",
            body=f"Welcome, {user.user_name}! Thank you for registering for Mathtrix! On the day of the event, "
            f"you'll need to show this QR code at the registration desk to complete your registration on the "
            f"day of the event. Please save this QR code as it cannot be issued again.",
            attachments=[qr_code_path],
        )

        return db_user

    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail=f"A user with the email {user.user_email} already exists!",
        )


@router.get("/{user_id}", response_model=User)
async def get_user_endpoint(*, db: Session = Depends(get_db), user_id: int):
    db_user = read_user(db=db, user_id=user_id)

    if not db_user:
        raise HTTPException(
            status_code=404, detail=f"A user with the id {user_id} does not exist!"
        )

    return db_user


@router.put("/{user_id}", response_model=User)
async def update_user_endpoint(
    *, db: Session = Depends(get_db), user_id: int, user: UserUpdate
):
    db_user = read_user(db=db, user_id=user_id)

    if not db_user:
        raise HTTPException(
            status_code=404, detail=f"A user with the id {user_id} does not exist!"
        )

    return update_user(db=db, user_id=user_id, user=user)


@router.delete("/{user_id}")
async def delete_user_endpoint(*, db: Session = Depends(get_db), user_id: int):
    db_user = read_user(db=db, user_id=user_id)

    if not db_user:
        raise HTTPException(
            status_code=404, detail=f"A user with the id {user_id} does not exist!"
        )

    return delete_user(db=db, user_id=user_id)
