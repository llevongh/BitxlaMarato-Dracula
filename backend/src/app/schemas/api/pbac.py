from typing import Optional, List

from pydantic import EmailStr, BaseModel, Field, root_validator, validator
from datetime import datetime
from app.schemas.common import UsageList


class PBACIn(BaseModel):
    date: datetime = Field(...)
    usages: List[Optional[UsageList]]

    @validator('date', pre=True)
    def parse_date(cls, value):
        if isinstance(value, datetime):
            return value
        elif isinstance(value, str):
            return datetime.strptime(value, '%d-%m-%Y')  # This format ensures only day, month, and year are used
        raise ValueError("Invalid date format")


class PBACOut(BaseModel):
    id: str = Field(title="PBAC ID")  # noqa
    user_id: str
    date: datetime = Field(...)
    usages: List[Optional[UsageList]]
    score: int

    class Config:
        orm_mode = True
