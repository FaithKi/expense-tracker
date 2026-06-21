from pydantic import BaseModel
from datetime import date

class WalletCreate(BaseModel):
    name: str
    amount: float