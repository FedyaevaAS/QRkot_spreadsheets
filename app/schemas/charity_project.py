from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Extra, Field, PositiveInt, validator


class CharityProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt = Field(..., example=1)


class CharityProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]
    full_amount: Optional[PositiveInt]

    @validator('name', 'description')
    def values_cannot_be_empty_or_null(cls, value):
        if not value or value.isspace() or value is None:
            raise ValueError('Все поля должны быть заполнены!')
        return value

    class Config:
        extra = Extra.forbid


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
