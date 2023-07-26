from pydantic import BaseModel

from app.schemas.team import Team


class EventBase(BaseModel):
    event_name: str | None = None
    event_teams: list[Team] | None = None


class EventCreate(EventBase):
    event_name: str


class EventUpdate(EventBase):
    event_name: str | None = None


class EventInDBBase(EventBase):
    id: int

    class Config:
        orm_mode = True


class Event(EventInDBBase):
    pass
