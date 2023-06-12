from pydantic import BaseModel

from app.schemas.user import User


class TeamBase(BaseModel):
    team_name: str | None = None
    team_school: str | None = None
    team_event: str | None = None

    team_members: list[User] | None = None


class TeamCreate(TeamBase):
    team_name: str
    team_school: str
    team_event: str


class TeamUpdate(TeamBase):
    team_name: str | None = None
    team_school: str | None = None
    team_event: str | None = None


class TeamInDBBase(TeamBase):
    id: int

    class Config:
        orm_mode = True


class Team(TeamInDBBase):
    pass
