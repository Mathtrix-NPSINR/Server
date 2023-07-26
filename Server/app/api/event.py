from fastapi import APIRouter, Depends, HTTPException, Security
from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.api_key import get_api_key
from app.core.db import get_db
from app.crud.event import create_event, delete_event, read_event, update_event
from app.schemas.event import Event, EventCreate, EventUpdate

router = APIRouter()


@router.post("/", response_model=Event)
async def create_event_endpoint(
        *,
        db: Session = Depends(get_db),
        api_key=Security(get_api_key),
        event: EventCreate,
):
    try:
        db_event = create_event(db=db, event=event)

        logger.info(
            f"{api_key.user} created a new event with the event id {db_event.id}"
        )

        return db_event

    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail=f"A event with the name {event.event_name} already exists!",
        )


@router.get("/", response_model=Event | list[Event])
async def get_event_endpoint(
        *,
        db: Session = Depends(get_db),
        api_key=Security(get_api_key),
        event_id: int | None = None,
):
    db_event = read_event(db=db, event_id=event_id)

    if not db_event:
        raise HTTPException(
            status_code=404, detail=f"An event with the id {event_id} does not exist!"
        )

    if event_id is None:
        logger.info(f"{api_key.user} read the details of all events")

    else:
        logger.info(f"{api_key.user} read the details of the event id {db_event.id}")

    return db_event


@router.put("/", response_model=Event)
async def update_event_endpoint(
        *,
        db: Session = Depends(get_db),
        api_key=Security(get_api_key),
        event_id: int,
        event: EventUpdate,
):
    db_event = read_event(db=db, event_id=event_id)

    if not db_event:
        raise HTTPException(
            status_code=404, detail=f"An event with the id {event_id} does not exist!"
        )

    logger.info(f"{api_key.user} updated the details of the event id {db_event.id}")

    return update_event(db=db, event_id=event_id, event=event)


@router.delete("/")
async def delete_event_endpoint(
        *,
        db: Session = Depends(get_db),
        api_key=Security(get_api_key),
        event_id: int,
):
    db_event = read_event(db=db, event_id=event_id)

    if not db_event:
        raise HTTPException(
            status_code=404,
            detail=f"An event with the event id {event_id} does not exist!",
        )

    logger.info(f"{api_key.user} deleted the event id {db_event.id}")

    return delete_event(db=db, event_id=event_id)
