from sqlalchemy.orm import Session

import app.models.event as event_models
import app.schemas.event as event_schemas


def create_event(db: Session, event: event_schemas.EventCreate):
    db_event = event_models.Event(
        event_name=event.event_name,
    )

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event


def read_event(db: Session, event_id: int | None):
    if event_id is None:
        db_events = db.query(event_models.Event).all()

        return db_events

    db_event = (
        db.query(event_models.Event).filter(event_models.Event.id == event_id).first()
    )

    return db_event


def update_event(db: Session, event_id: int, event: event_schemas.EventUpdate):
    db_event = (
        db.query(event_models.Event).filter(event_models.Event.id == event_id).first()
    )

    if event.event_name is not None:
        db_event.event_name = event.event_name

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event


def delete_event(db: Session, event_id: int):
    db_event = (
        db.query(event_models.Event).filter(event_models.Event.id == event_id).first()
    )

    event_name = db_event.event_name

    db.delete(db_event)
    db.commit()

    return f"Deleted {event_name}!"
