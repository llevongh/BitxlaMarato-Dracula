from app.db.client import get_collection
from app.core.config import CONFIG
from app.repository import UserRepository, PBACRepository
from app.services.jwt_issuer import JWTIssuer


def get_jwt_issuer() -> JWTIssuer:
    return JWTIssuer()


def get_user_repo() -> UserRepository:
    return UserRepository(
        collection=get_collection(
            collection_name=CONFIG.mongo.configs_collection
        )
    )


def get_pbac_repo() -> PBACRepository:
    return PBACRepository(
        collection=get_collection(
            collection_name='pbac'
        )
    )
