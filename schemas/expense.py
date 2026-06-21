from pydantic import BaseModel
from datetime import date

class UpdateItem(BaseModel):
    name: str
    amount: float
    category: str | None = None
    date: date

class ExpenseItem(UpdateItem):
    pass

class IncomeItem(UpdateItem):
    pass

class ManualAdjustment(UpdateItem):
    pass

class Wallet(BaseModel):
    name: str
    amount: float
    last_updated_by: UpdateItem
    last_updated_when: date