from pydantic import Field, BaseModel


class TokenOut(BaseModel):
    type: str = "Bearer"  # noqa
    access_token: str = Field(title="Access token")
    refresh_token: str = Field(title="Token to generate a new access token")


class RefreshTokenIn(BaseModel):
    grant_type: str = "refresh_token"
    refresh_token: str = Field(title="Token to generate a new access token")


class DetailOut(BaseModel):
    detail: str = Field(title="Detail")
