from typing import Optional, Dict, Any
from motor.motor_asyncio import AsyncIOMotorCollection
from passlib.context import CryptContext
from pydantic import parse_obj_as
from app.schemas import UserCreate, UserModel
from bson import ObjectId

class UserRepository:

    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection: AsyncIOMotorCollection = collection

    async def get_user(self, email: str) -> Optional[UserModel]:

        user_data = await self.collection.find_one({'email': email})
        if user_data:
            return parse_obj_as(UserModel, user_data)
        return None

    async def get_user_by_id(self, id: str) -> Optional[UserModel]:
        user_data = await self.collection.find_one({"_id": ObjectId(id)})
        if user_data:
            return parse_obj_as(UserModel, user_data)
        return None

    async def create_user(self, user: UserCreate) -> UserModel:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hashed_password = pwd_context.hash(user.password)
        user_data = user.dict()
        user_data["password"] = hashed_password
        inserted_doc = await self.collection.insert_one(user_data)
        new_user_data = await self.collection.find_one({"_id": inserted_doc.inserted_id})
        return parse_obj_as(UserModel, new_user_data)
