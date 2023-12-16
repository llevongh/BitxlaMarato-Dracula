from typing import Dict

from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.schemas.enums import StrEnum


class Code(StrEnum):
    UserNotFound = "UserNotFound"
    Unauthorized = "Unauthorized"
    UserExists = "UserExists"
    PasswordNotEqual = "PasswordNotEqual"
    PasswordSame = "PasswordSame"
    InvalidOldPassword = "InvalidOldPassword"


class APIError(Exception):
    __slots__ = ('code', 'message', 'status_code')

    def __init__(self, code: Code, message: str, status_code: int = 400):
        self.code = code
        self.message = message
        self.status_code = status_code

    def to_dict(self) -> Dict[str, str]:
        return {
            'code': self.code,
            'message': self.message,
        }


async def api_error_handler(_: Request, error: APIError) -> JSONResponse:
    return JSONResponse(
        status_code=error.status_code,
        content=error.to_dict()
    )


class UserNotFoundError(APIError):
    def __init__(self) -> None:
        super().__init__(
            code=Code.UserNotFound,
            message="User not found",
            status_code=status.HTTP_404_NOT_FOUND
        )


class UnauthorizedError(APIError):
    def __init__(self) -> None:
        super().__init__(
            code=Code.Unauthorized,
            message='Not authorized',
            status_code=status.HTTP_401_UNAUTHORIZED
        )


class UserExistsError(APIError):
    def __init__(self) -> None:
        super().__init__(
            code=Code.UserExists,
            message='User with this email already exists',
            status_code=status.HTTP_409_CONFLICT
        )


class PasswordNotEqualError(APIError):
    def __init__(self) -> None:
        super().__init__(
            code=Code.PasswordNotEqual,
            message='Passwords do not match',
            status_code=status.HTTP_409_CONFLICT
        )


class PasswordSameError(APIError):
    def __init__(self) -> None:
        super().__init__(
            code=Code.PasswordSame,
            message='New password should not be the same as the old password',
            status_code=status.HTTP_400_BAD_REQUEST
        )


class InvalidOldPasswordError(APIError):
    def __init__(self) -> None:
        super().__init__(
            code=Code.InvalidOldPassword,
            message='Old password is not valid',
            status_code=status.HTTP_401_UNAUTHORIZED
        )
