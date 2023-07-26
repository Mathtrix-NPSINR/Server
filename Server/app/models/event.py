from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)

    event_name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    event_teams: Mapped[list["Team"]] = relationship()
