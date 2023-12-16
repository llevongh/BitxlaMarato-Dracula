from typing import List
from motor.motor_asyncio import AsyncIOMotorCollection
from pydantic import parse_obj_as
from app.schemas import PBACModel, PBACIn
from app.schemas.common.usages import UsageList
from app.services.utils import calculate_pbac
from datetime import datetime

class PBACRepository:

    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def create_pbac(self, pbac: PBACIn, user_id: str) -> PBACModel:
        pbac_dict = pbac.dict()
        pbac_dict['user_id'] = user_id
        pbac_dict['date'] = pbac_dict['date'].isoformat()

        existing_data = await self.collection.find_one({"user_id": user_id, "date": pbac_dict['date']})
        if existing_data:
            pbac_dict['usages'] += existing_data['usages']
            await self.collection.delete_one({"_id": existing_data['_id']})

        pbac_dict['usages'] = self.merge_and_sum_usages(pbac_dict['usages'])

        total_score = sum(calculate_pbac(sanitary) for sanitary in parse_obj_as(List[UsageList], pbac_dict['usages']))
        pbac_dict['score'] = total_score

        # Insert and return the new document
        inserted_doc = await self.collection.insert_one(pbac_dict)
        new_user_data = await self.collection.find_one({"_id": inserted_doc.inserted_id})
        return parse_obj_as(PBACModel, new_user_data)

    def merge_and_sum_usages(self, usages: List[dict]) -> List[dict]:
        merged = {}
        for usage in usages:
            key = (usage['sanitary_product'], usage['blood_level'])
            if key in merged:
                merged[key]['times_used'] += usage['times_used']
            else:
                merged[key] = usage.copy()
        return list(merged.values())

    async def get_pbac_by_month(self, user_id: str, start_date: datetime, end_date: datetime) -> List[PBACModel]:
        query = {
            "user_id": user_id,
            "date": {"$gte": start_date.isoformat(), "$lte": end_date.isoformat()}
        }
        pbac_records = await self.collection.find(query).to_list(None)
        return parse_obj_as(List[PBACModel], pbac_records)
