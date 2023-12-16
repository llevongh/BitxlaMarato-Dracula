import random
import string
from typing import Any, Dict, Optional

from jose import jwt
from fastapi import Depends
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from app.api.deps import get_user_repo, get_jwt_issuer
from app.exceptions import UnauthorizedError
from app.core.config import CONFIG
from app.repository import UserRepository
from app.services.jwt_issuer import JWTIssuer
from app.schemas import UserCreate, UserOut

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/user/login")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def get_current_user(
        token: str = Depends(oauth2_scheme),
        jwt_issuer: JWTIssuer = Depends(get_jwt_issuer),
        user_repo: UserRepository = Depends(get_user_repo)
) -> UserCreate:
    """
     Returns Current Active User

         Parameters:
                 token (str): JWT token
                 jwt_issuer (JWTIssuer): this is for decoding token
                 user_repo (UserRepository): User repository

         Returns:
                 fetched_user (UserCreate): User object
     """

    try:
        payload = jwt.decode(
            token=token,
            key=jwt_issuer.pub_key,
            issuer=CONFIG.api.title,
            algorithms=[CONFIG.jwt.algorithm]
        )
        user: Dict[str, Any] = payload.get("user", {})
        if 'id' not in user:
            raise UnauthorizedError
    except Exception as e:
        raise UnauthorizedError

    fetched_user: Optional[UserOut] = await user_repo.get_user_by_id(
        id=user["id"]
    )
    if fetched_user is None:
        raise UnauthorizedError
    return fetched_user


def generate_verification_code(
        *,
        length: int = 6,
) -> str:
    verification_code: str = ''.join(
        random.choice(
            string.ascii_lowercase + string.digits,
        ) for _ in range(length)
    )

    return verification_code.casefold()
