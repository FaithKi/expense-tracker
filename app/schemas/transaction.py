from pydantic import BaseModel
from datetime import date

from app.utils.enums import TransactionType

class TransactionBase(BaseModel):
    name: str
    amount: float
    category: str | None = None
    type: TransactionType

class TransactionCreate(TransactionBase):
    wallet_id: int

class TransactionBulkCreate(BaseModel):
    transactions: list[TransactionBase]
    wallet_id: int