from sqlalchemy.orm import Session

import app.models.user as user_models
import app.schemas.user as user_schemas


def create_user(db: Session, user: user_schemas.UserCreate):
    db_user = user_models.User(
        user_name=user.user_name,
        user_email=user.user_email,
        user_phone=user.user_phone,
        user_school=user.user_school,
        user_attendance=user.user_attendance,
        team_id=user.team_id,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def read_user(db: Session, user_id: int):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()

    return db_user


def update_user(db: Session, user_id: int, user: user_schemas.UserUpdate):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()

    if user.user_name is not None:
        db_user.user_name = user.user_name

    if user.user_email is not None:
        db_user.user_email = user.user_email

    if user.user_phone is not None:
        db_user.user_phone = user.user_phone

    if user.user_school is not None:
        db_user.user_school = user.user_school

    if user.user_attendance is not None:
        db_user.user_attendance = user.user_attendance

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()

    name = db_user.user_name

    db.delete(db_user)
    db.commit()

    return f"Deleted {name}!"


def update_user_attendance(db: Session, user_id: int):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()

    db_user.user_attendance = True

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return f"{db_user.user_name} was marked present!"
