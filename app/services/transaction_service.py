from sqlalchemy.orm import Session
from app.database.models import Transaction
from app.schemas.transaction import TransactionCreate

from datetime import date


def create_transaction(
    db: Session,
    transaction_data: TransactionCreate
):
    transaction = Transaction(
        name=transaction_data.name,
        amount=transaction_data.amount,
        category=transaction_data.category,
        type=transaction_data.type,
        wallet_id=transaction_data.wallet_id
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction

def get_all_transactions(db: Session):
    return db.query(Transaction).all()