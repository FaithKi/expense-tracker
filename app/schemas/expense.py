from pydantic import BaseModel
from datetime import date

from app.utils.transaction_types import TransactionType

class Transaction(BaseModel):
    name: str
    amount: float
    category: str | None = None
    type: TransactionType
    date: date

class Wallet(BaseModel):
    name: str
    amount: float
    last_updated_by: Transaction
    last_updated_when: date