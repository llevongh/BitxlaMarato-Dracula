import logging
import datetime
from typing import Optional, Dict, Any

from fastapi import Depends, APIRouter, status

from app.schemas import (
    UserOut,
    TokenOut,
    UserCreate,
    UserLogin,
    UserIn,
    UserModel
)
from app.api.deps import (
    get_user_repo,
    get_jwt_issuer,
)
from app.exceptions import (
    UnauthorizedError,
    UserExistsError
)
from app.core.config import CONFIG
from app.repository.user import UserRepository
from app.services.security import (
    verify_password,
    get_current_user
)
from app.services.jwt_issuer import JWTIssuer

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/login",
    response_model=TokenOut,
    status_code=status.HTTP_200_OK,
    summary='Login',
    description='User authorization',
    operation_id='LoginUser',
    response_description='The user has been authorized',
    response_model_exclude_none=True
)
async def login(
        user_login: UserLogin,
        user_repo: UserRepository = Depends(get_user_repo),
        jwt_issuer: JWTIssuer = Depends(get_jwt_issuer),
) -> TokenOut:
    fetched_user: Optional[UserModel] = await user_repo.get_user(
        email=user_login.email
    )
    if fetched_user is None or not verify_password(
            user_login.password, fetched_user.password
    ):

        raise UnauthorizedError

    user = {
        "id": fetched_user.id,
        "display_name": f"{fetched_user.first_name} {fetched_user.last_name}",
        "username": fetched_user.email,
        "first_name": fetched_user.first_name,
        "last_name": fetched_user.last_name,
        "email": fetched_user.email,
        "status": fetched_user.status
    }

    return TokenOut(
        access_token=jwt_issuer.create_access_token(
            exp_delta=datetime.timedelta(
                minutes=CONFIG.jwt.access_token_expire_minutes
            ),
            user=user
        ),
        refresh_token=jwt_issuer.create_refresh_token(fetched_user.id),
    )


@router.post(
    "/register",
    response_model=TokenOut,
    status_code=status.HTTP_200_OK,
    summary='Register',
    description='Регистрация нового пользователя',
    operation_id='RegisterUser',
    response_description='Пользователь зарегистрирован',
    response_model_exclude_none=True
)
async def register(
        user_in: UserIn,
        user_repo: UserRepository = Depends(get_user_repo),
        jwt_issuer: JWTIssuer = Depends(get_jwt_issuer),
) -> Optional[TokenOut]:
    fetched_user: Optional[UserModel] = await user_repo.get_user(
        email=user_in.email
    )

    """if User exists and  User's status  is ACTIVE OR INACTIVE , You can not register"""
    if fetched_user:
        raise UserExistsError

    new_user: Optional[UserModel] = await user_repo.create_user(
        user=UserCreate(
            **user_in.dict()
        )) if fetched_user is None else fetched_user

    return TokenOut(
        access_token=jwt_issuer.create_access_token(
            exp_delta=datetime.timedelta(minutes=CONFIG.jwt.access_token_expire_minutes),
            user=new_user.dict()
        ),
        refresh_token=jwt_issuer.create_refresh_token(new_user.id)
    )


@router.get(
    "/me",
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
    summary='GetMe',
    description="Get information about the current user",
    operation_id='GetMe',
    response_description='User information has been received',
    response_model_exclude_none=True
)
async def me(
        auth_user: UserOut = Depends(get_current_user)
) -> Optional[UserOut]:
    return auth_user

# @router.post(
#     "/forgot-password",
#     response_model=DetailOut,
#     status_code=status.HTTP_202_ACCEPTED,
#     summary='ForgotPassword',
#     description="Password recovery",
#     operation_id='ForgotPassword',
#     response_description='A password reset link has been sent to your email',
#     response_model_exclude_none=True
# )
# async def forgot_password(
#         email_in: UserForgotPasswordIn,
#         async_session: AsyncSession = Depends(get_async_session),
#         user_repo: UserRepository = Depends(get_user_repo),
#         redis_client: Redis = Depends(get_redis_client)
# ) -> DetailOut:
#     fetched_user: Optional[UserModel] = await user_repo.get_existing_user(
#         async_session=async_session,
#         email=email_in.email
#     )
#
#     if fetched_user is None:
#         raise UserNotFoundError
#
#     reset_pass_token: str = str(uuid.uuid4())
#     print(reset_pass_token)
#     params = {
#         'user_email': f"{fetched_user.email}"
#     }
#
#     redis_client.setex(
#         name=reset_pass_token,
#         time=CONFIG.verification_code_exp,
#         value=json.dumps(params, ensure_ascii=False)
#     )
#     return DetailOut(
#         detail="A password reset link has been sent to your email"
#     )
#
#
# @router.post(
#     "/change-password",
#     response_model=DetailOut,
#     status_code=status.HTTP_200_OK,
#     summary='ChangeUserPassword',
#     description="Change User password",
#     operation_id='ChangeUserPassword',
#     response_description='Password has been successfully changed',
#     response_model_exclude_none=True
# )
# async def change_password(
#         password_in: UserChangePasswordIn,
#         auth_user: UserModel = Depends(get_current_user),
#         async_session: AsyncSession = Depends(get_async_session),
#         user_repo: UserRepository = Depends(get_user_repo),
# ) -> DetailOut:
#     if password_in.password1 != password_in.password2:
#         raise PasswordNotEqualError
#
#     if password_in.old_password == password_in.password2:
#         raise PasswordSameError
#
#     if not verify_password(password_in.old_password, auth_user.password):
#         raise InvalidOldPasswordError
#
#     auth_user.password = get_password_hash(password_in.password1)
#     await async_session.commit()
#
#     return DetailOut(
#         detail="Password has been successfully changed"
#     )
