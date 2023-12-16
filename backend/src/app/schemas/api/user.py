from typing import Any, Dict, Optional
from datetime import datetime

from pydantic import Field, EmailStr, BaseModel, root_validator
from pydantic.utils import GetterDict


class UserOut(BaseModel):
    id: str = Field(title="User ID")  # noqa
    email: Optional[str] = Field(title="User Email")
    first_name: Optional[str] = Field(title="User Fiest Name")
    last_name: Optional[str] = Field(title="User Last Name")
    status: str = Field(title="User Status")

    class Config:
        orm_mode = True


class UserIn(BaseModel):
    email: EmailStr = Field(title="User Email")
    password: str = Field(title="User Password")

    first_name: str = Field(title="User First Name")
    last_name: str = Field(title="User Last Name")


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(title="User Password")


class UserForgotPasswordIn(BaseModel):
    email: EmailStr = Field(title="User Email")


class UserResetPasswordIn(BaseModel):
    password1: str = Field(title="New password" )
    password2: str = Field(title="New password")


class UserChangePasswordIn(BaseModel):
    old_password: str = Field(title="Old password")
    password1: str = Field(title="New password")
    password2: str = Field(title="New password")
