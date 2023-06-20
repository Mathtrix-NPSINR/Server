from sqlalchemy import Integer, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)

    event_name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    event_tagline: Mapped[str] = mapped_column(String, nullable=False)
    event_description: Mapped[str] = mapped_column(String, nullable=False)
    event_rules: Mapped[str] = mapped_column(String, nullable=False)
    event_heads: Mapped[str] = mapped_column(String, nullable=False)
    event_icon: Mapped[str] = mapped_column(String, nullable=False)
    event_maximum_participants: Mapped[int] = mapped_column(Integer, nullable=False)

    event_teams: Mapped[list["Team"]] = relationship()
