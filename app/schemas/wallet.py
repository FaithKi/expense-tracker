from pydantic import BaseModel

class WalletCreate(BaseModel):
    name: str
    amount: float