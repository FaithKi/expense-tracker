from sqlalchemy.orm import Session
from app.database.models import Transaction
from app.schemas.transaction import TransactionBulkCreate, TransactionCreate
from app.services.wallet_service import update_wallet

from datetime import date

def get_all_transactions(db: Session):
    return db.query(Transaction).all()

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
    wallet = update_wallet(db, transactions=[transaction_data], wallet_id=transaction_data.wallet_id)

    db.commit()
    db.refresh(transaction)
    db.refresh(wallet)

    return transaction, wallet

def create_bulk_transaction(
        db:Session,
        transactions_data: TransactionBulkCreate
):
    transactions = []
    for transaction_data in transactions_data.transactions:
        transaction = Transaction(
            name=transaction_data.name,
            amount=transaction_data.amount,
            category=transaction_data.category,
            type=transaction_data.type,
            wallet_id=transactions_data.wallet_id
        )

        transactions.append(transaction)

    db.add_all(transactions)
    wallet = update_wallet(db, transactions=transactions_data.transactions, wallet_id=transactions_data.wallet_id)
    db.flush()
    db.commit()
    db.refresh(wallet)

    created_transactions = db.query(Transaction).filter(Transaction.id.in_([t.id for t in transactions])).all()

    return  created_transactions, wallet