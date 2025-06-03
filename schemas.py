from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TradeCreate(BaseModel):
    ticker: str
    price: float = Field(..., gt=0)
    quantity: int = Field(..., gt=0)
    side: str = Field(..., pattern="^(buy|sell)$")  # Use pattern, not regex
    timestamp: Optional[datetime] = None

class TradeOut(TradeCreate):
    id: int

    class Config:
        orm_mode = True
