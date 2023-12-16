import logging
from typing import List
from datetime import date, timedelta, datetime
from app.api.deps import get_pbac_repo
from app.repository import PBACRepository

from fastapi import Depends, APIRouter, status

from app.schemas import (
    PBACIn,
    PBACOut,
    PBACModel,
    UserOut
)

from app.services.security import (
    get_current_user
)

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "",
    response_model=PBACOut,
    status_code=status.HTTP_200_OK,
    summary='CreatePBAC',
    description='Create PBAC Score',
    operation_id='CreatePBAC',
    response_description='PBAC Score was created',
    response_model_exclude_none=True
)
async def create_pbac_score(
        pbac_in: PBACIn,
        auth_user: UserOut = Depends(get_current_user),
        pbac_repo: PBACRepository = Depends(get_pbac_repo),
) -> PBACOut:
    return await pbac_repo.create_pbac(pbac=pbac_in, user_id=auth_user.id)


@router.get(
    "/current-month",
    response_model=List[PBACOut],
    status_code=status.HTTP_200_OK,
    summary='GetPBACByCurrentMonth',
    description='Get current Month PBAC Score',
    operation_id='GetPBACByCurrentMonth',
    response_description='List PBAC Score',
    response_model_exclude_none=True
)
async def get_pbac_entries_for_month(
        auth_user: UserOut = Depends(get_current_user),
        pbac_repo: PBACRepository = Depends(get_pbac_repo),
) -> List[PBACOut]:
    today = datetime.today()
    first_day_of_month = date(today.year, today.month, 1)

    if today.month == 12:
        last_day_of_month = datetime(today.year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day_of_month = datetime(today.year, today.month + 1, 1) - timedelta(days=1)

    return await pbac_repo.get_pbac_by_month(
        user_id=auth_user.id,
        start_date=first_day_of_month,
        end_date=last_day_of_month
    )
