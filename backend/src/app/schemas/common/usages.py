from typing import Optional, Dict, Any

from pydantic import EmailStr, BaseModel, Field, root_validator
from app.schemas.enums.sanitary import SanitaryProductType, BloodLevel, CentSize


class UsageList(BaseModel):
    sanitary_product: SanitaryProductType
    blood_level: Optional[BloodLevel] = None
    cent_size: Optional[CentSize] = None
    times_used: int
