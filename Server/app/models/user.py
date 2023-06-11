from sqlalchemy import Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)

    user_name: Mapped[str] = mapped_column(String, nullable=False)
    user_email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    user_phone: Mapped[str] = mapped_column(String, nullable=False)
    user_school: Mapped[str] = mapped_column(String, nullable=False)
    user_attendance: Mapped[bool] = mapped_column(Boolean, nullable=False)

    team_id: Mapped[str] = mapped_column(ForeignKey("teams.id"))
    team: Mapped["Team"] = relationship(back_populates="team_members")
