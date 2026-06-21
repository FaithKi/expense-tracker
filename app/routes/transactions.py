from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.transaction import TransactionCreate, TransactionBulkCreate
from app.services.transaction_service import create_transaction, get_all_transactions, create_bulk_transaction, get_transactions_by_wallet

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.get("/")
def list_transactions(db: Session = Depends(get_db)):
    return {"message": "success", "transactions": get_all_transactions(db)}

@router.post("/")
def create_new_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    created, wallet = create_transaction(db,transaction)
    return {"message": "created", "transaction": created, "wallet": wallet}

@router.post("/bulk")
def create_multiple_transactions(transactions: TransactionBulkCreate, db: Session = Depends(get_db)):
    created_transactions, wallet = create_bulk_transaction(db, transactions_data=transactions)
    return {"message": "created", "transactions": created_transactions, "wallet": wallet}

@router.get("/wallet/{wallet_id}")
def list_transactions_by_wallet(wallet_id: int, db: Session = Depends(get_db)):
    return {"message": "success", "transactions": get_transactions_by_wallet(db, wallet_id)}