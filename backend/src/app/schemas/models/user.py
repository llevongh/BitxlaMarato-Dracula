from typing import Optional, Dict, Any

from pydantic import EmailStr, BaseModel, Field, root_validator
from pydantic.utils import GetterDict

from app.schemas.enums.user import UserStatusTypeEnum


class UserUpdate(BaseModel):
    email: EmailStr
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    status: UserStatusTypeEnum


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    status: UserStatusTypeEnum = UserStatusTypeEnum.PENDING


class UserModel(BaseModel):
    id: str = Field(title="User ID")  # noqa
    email: Optional[str] = Field(title="User Email")
    first_name: Optional[str] = Field(title="User Fiest Name")
    last_name: Optional[str] = Field(title="User Last Name")
    status: str = Field(title="User Status")
    password: str

    class Config:
        orm_mode = True

    @root_validator(pre=True)
    def set_recognizable_id(cls, obj: GetterDict) -> Dict[str, Any]:
        user_dict = dict(obj.items())
        user_dict['id'] = str(obj['_id'])
        return user_dict
