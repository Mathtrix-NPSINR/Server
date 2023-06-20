from sqlalchemy.orm import Session

import app.models.event as event_models
import app.schemas.event as event_schemas


def create_event(db: Session, event: event_schemas.EventCreate):
    db_event = event_models.Event(
        event_name=event.event_name,
        event_tagline=event.event_tagline,
        event_description=event.event_description,
        event_rules=event.event_rules,
        event_heads=event.event_heads,
        event_icon=event.event_icon,
        event_maximum_participants=event.event_maximum_participants
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

    if event.event_tagline is not None:
        db_event.event_tagline = event.event_tagline

    if event.event_description is not None:
        db_event.event_description = event.event_description

    if event.event_rules is not None:
        db_event.event_rules = event.event_rules

    if event.event_heads is not None:
        db_event.event_heads = event.event_heads

    if event.event_icon is not None:
        db_event.event_icon = event.event_icon

    if event.event_maximum_participants is not None:
        db_event.event_maximum_participants = event.event_maximum_participants

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
