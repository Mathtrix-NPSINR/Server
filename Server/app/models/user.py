from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)

    user_name: Mapped[str] = mapped_column(String, nullable=False)
    user_email: Mapped[str] = mapped_column(String, nullable=False)
    user_phone: Mapped[str] = mapped_column(String, nullable=False)
    user_school: Mapped[str] = mapped_column(String, nullable=False)
    user_attendance: Mapped[bool] = mapped_column(Boolean, nullable=False)

    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=True)
