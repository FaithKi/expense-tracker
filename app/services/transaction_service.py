from sqlalchemy.orm import Session
from app.database.models import Transaction
from app.schemas.transaction import TransactionBulkCreate, TransactionCreate
from app.services.wallet_service import update_wallet

from datetime import date

from app.utils.enums import TransactionType

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

def get_transactions_by_wallet(db: Session, wallet_id: int):
    return db.query(Transaction).filter(Transaction.wallet_id == wallet_id).all()

def delete_transaction_by_id(db: Session, transaction_id: int):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not transaction:
        return (False, None)
    wallet = transaction.wallet
    print(f"Deleting transaction: {transaction}, associated wallet: {wallet}")
    match transaction.type:
        case TransactionType.INCOME:
            wallet.amount -= transaction.amount
        case TransactionType.EXPENSE:
            wallet.amount += transaction.amount
        case TransactionType.ADJUSTMENT:
            wallet.amount -= transaction.amount
    db.delete(transaction)
    db.commit()
    return (True, wallet.amount)