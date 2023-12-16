from app.schemas.enums.base import StrEnum


class BloodLevel(StrEnum):
    LIGHT = 'Light'
    MEDIUM = 'Medium'
    HEAVY = 'Heavy'


class SanitaryProductType(StrEnum):
    PADS = 'Pads'
    TAMPONS = 'Tampons'
    CLOTS = 'Clots'
    FLOODING = 'Flooding'


class CentSize(StrEnum):
    SMALL = 'Small'
    LARGE = 'Large'
