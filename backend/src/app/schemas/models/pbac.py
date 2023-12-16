from typing import Optional, Dict, Any, List

from pydantic import EmailStr, BaseModel, Field, root_validator, validator
from pydantic.utils import GetterDict
from datetime import datetime
from app.schemas.common.usages import UsageList


class PBACModel(BaseModel):
    id: str = Field(title="PBAC ID")  # noqa
    user_id: str
    date: datetime = Field(...)
    usages: List[Optional[UsageList]]
    score: int

    class Config:
        orm_mode = True

    @root_validator(pre=True)
    def set_recognizable_id(cls, obj: GetterDict) -> Dict[str, Any]:
        pbac_dict = dict(obj.items())
        pbac_dict['id'] = str(obj['_id'])
        return pbac_dict
