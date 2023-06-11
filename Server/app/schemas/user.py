from pydantic import BaseModel, EmailStr, constr


class UserBase(BaseModel):
    user_name: str | None = None
    user_email: EmailStr | None = None
    user_phone: constr(
        regex="^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
    ) | None = None
    user_school: str | None = None
    user_attendance: bool | None = None

    team_id: int | None = None


class UserCreate(UserBase):
    user_name: str
    user_email: EmailStr
    user_phone: constr(
        regex="^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
    )
    user_school: str
    user_attendance: bool = False

    team_id: int


class UserUpdate(UserBase):
    user_name: str | None = None
    user_email: EmailStr | None = None
    user_phone: constr(
        regex="^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
    ) | None = None
    user_school: str | None = None
    user_attendance: bool | None = None


class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass
