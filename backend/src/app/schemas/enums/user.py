from app.schemas.enums.base import StrEnum


class UserStatusTypeEnum(StrEnum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
