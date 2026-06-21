from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.transaction import TransactionCreate
from app.services.transaction_service import create_transaction, get_all_transactions
from app.services.wallet_service import update_wallet

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.get("/")
def list_transactions(db: Session = Depends(get_db)):
    return {"message": "success", "transactions": get_all_transactions(db)}

@router.post("/")
def create_new_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    created = create_transaction(db,transaction)
    update_wallet(db, transactions=[transaction])
    return {"message": "created", "transaction": created}