from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

class TransactionCreate(BaseModel):
    type: Literal["deposit", "withdraw"]
    amount: float = Field(..., gt=0)

class TransactionOut(BaseModel):
    id: int
    account_id: int
    type: str
    amount: float
    created_at: datetime

    class Config:
        orm_mode = True
