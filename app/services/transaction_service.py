from sqlalchemy.orm import Session
from app.database.models import Transaction
from app.schemas.transaction import TransactionCreate
from app.services.wallet_service import update_wallet

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

    wallet = update_wallet(db, transactions=[transaction_data])

    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    db.refresh(wallet)

    return transaction

def get_all_transactions(db: Session):
    return db.query(Transaction).all()