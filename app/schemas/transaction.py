from pydantic import BaseModel
from datetime import date

from app.utils.enums import TransactionType

class TransactionCreate(BaseModel):
    name: str
    amount: float
    category: str | None = None
    type: TransactionType
    wallet_id: int