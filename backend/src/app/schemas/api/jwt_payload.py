from typing import Any, Dict
from datetime import datetime

from pydantic import Field, BaseModel

# App Imports
from app.core.config import CONFIG


class JWTPayload(BaseModel):
    exp: datetime = Field(title="Expiration")
    iat: datetime = Field(title="Date of issue")
    azp: str = "dashboard"
    iss: str = CONFIG.api.title
    sub: str = Field(title="User ID")
    user: Dict[str, Any] = Field(title="User Info")
    locale: str = "en"