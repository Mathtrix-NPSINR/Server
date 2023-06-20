from app.schemas.team import Team
from pydantic import BaseModel, HttpUrl


class EventBase(BaseModel):
    event_name: str | None = None
    event_tagline: str | None = None
    event_description: str | None = None
    event_rules: str | None = None
    event_heads: str | None = None
    event_icon: HttpUrl | None = None
    event_maximum_participants: int | None = None

    event_teams: list[Team] | None = None


class EventCreate(EventBase):
    event_name: str
    event_tagline: str
    event_description: str
    event_rules: str
    event_heads: str
    event_icon: HttpUrl
    event_maximum_participants: int


class EventUpdate(EventBase):
    event_name: str | None = None
    event_tagline: str | None = None
    event_description: str | None = None
    event_rules: str | None = None
    event_heads: str | None = None
    event_icon: HttpUrl | None = None
    event_maximum_participants: int


class EventInDBBase(EventBase):
    id: int

    class Config:
        orm_mode = True


class Event(EventInDBBase):
    pass


class EventDetails(BaseModel):
    id: int
    event_name: str
    event_tagline: str
    event_description: str
    event_rules: str
    event_heads: str
    event_icon: HttpUrl
    event_maximum_participants: int

    class Config:
        orm_mode = True

    # event_teams: None
