from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection

# App Imports
from app.core.config import CONFIG


def get_mongo_client() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(
        host=CONFIG.mongo.host,
        port=CONFIG.mongo.port,
        username=CONFIG.mongo.username,
        password=CONFIG.mongo.password
    )


def get_db() -> AsyncIOMotorDatabase:
    client: AsyncIOMotorClient = get_mongo_client()
    return client[CONFIG.mongo.db]


def get_collection(collection_name: str) -> AsyncIOMotorCollection:
    db: AsyncIOMotorDatabase = get_db()
    return db[collection_name]
