from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)

    team_school: Mapped[str] = mapped_column(String, nullable=False)
    team_event: Mapped[str] = mapped_column(String, nullable=False)

    team_members: Mapped[list["User"]] = relationship()

    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=True)
