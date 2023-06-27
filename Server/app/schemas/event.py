from app.schemas.team import Team
from pydantic import BaseModel


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


class EventDetails(BaseModel):
    id: int
    event_name: str

    class Config:
        orm_mode = True

    # event_teams: None
