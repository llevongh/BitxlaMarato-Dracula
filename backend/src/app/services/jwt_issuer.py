# Standard Library
import datetime
from typing import Any, Dict

import pydantic
from jose import jwt

# App Imports
from app.schemas import JWTPayload
from app.core.config import CONFIG


class JWTIssuer:
    def __init__(self):
        self.prv_key = CONFIG.jwt.private_key
        self.pub_key = CONFIG.jwt.public_key

    def create_access_token(
            self,
            *,
            user: Dict[str, Any],
            exp_delta: datetime.timedelta = None,
    ) -> str:
        data = JWTPayload(
            exp=datetime.datetime.utcnow() + datetime.timedelta(weeks=3000),
            iat=datetime.datetime.utcnow(),
            sub=user['id'],
            user=user,
            locale="en"
        )

        return jwt.encode(
            data.dict(exclude_none=True),
            key=self.prv_key,
            algorithm=CONFIG.jwt.algorithm
        )

    def create_refresh_token(self, sub: str) -> str:
        payload = {
            "sub": sub
        }
        return jwt.encode(payload, key=self.prv_key, algorithm=CONFIG.jwt.algorithm)
