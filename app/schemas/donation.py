from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, PositiveInt


class DonationtCreate(BaseModel):
    full_amount: PositiveInt = Field(..., example=1)
    comment: Optional[str]


class DonationtDB(DonationtCreate):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationsAllDB(DonationtDB):
    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]
