from app.core.db import get_db
from app.crud.event import create_event, delete_event, read_event, update_event
from app.schemas.event import Event, EventCreate, EventUpdate
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=Event)
async def create_event_endpoint(*, db: Session = Depends(get_db), event: EventCreate):
    try:
        return create_event(db=db, event=event)

    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail=f"A event with the name {event.event_name} already exists!",
        )


@router.get("/{event_id}", response_model=Event)
async def get_event_endpoint(*, db: Session = Depends(get_db), event_id: int):
    db_event = read_event(db=db, event_id=event_id)

    if not db_event:
        raise HTTPException(
            status_code=404, detail=f"A event with the id {event_id} does not exist!"
        )

    return db_event


@router.put("/{event_id}", response_model=Event)
async def update_event_endpoint(
    *, db: Session = Depends(get_db), event_id: int, event: EventUpdate
):
    db_event = read_event(db=db, event_id=event_id)

    if not db_event:
        raise HTTPException(
            status_code=404, detail=f"A event with the id {event_id} does not exist!"
        )

    return update_event(db=db, event_id=event_id, event=event)


@router.delete("/{event_id}")
async def delete_event_endpoint(*, db: Session = Depends(get_db), event_id: int):
    db_event = read_event(db=db, event_id=event_id)

    if not db_event:
        raise HTTPException(
            status_code=404, detail=f"A with the event id {event_id} does not exist!"
        )

    return delete_event(db=db, event_id=event_id)
