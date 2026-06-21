from sqlalchemy.orm import Session
from app.database.models import Wallet
from app.schemas.wallet import WalletCreate
from app.schemas.transaction import TransactionCreate
from app.utils.enums import TransactionType

def create_wallet(
        db: Session,
        wallet_data: WalletCreate
):
    wallet = Wallet(
        name=wallet_data.name,
        amount=wallet_data.amount
    )

    db.add(wallet)
    db.commit()
    db.refresh(wallet)

    return wallet

def get_all_wallets(db: Session):
    return db.query(Wallet).all()

def update_wallet(db: Session, transactions: list[TransactionCreate], wallet_id: int | None = None):
    try:
        if not wallet_id:
            wallet_id = transactions[0].wallet_id
        for transaction in transactions:
            wallet = db.query(Wallet).filter(Wallet.id == wallet_id).with_for_update().first()
            if transaction.type == TransactionType.INCOME:
                wallet.amount += transaction.amount
            elif transaction.type == TransactionType.EXPENSE:
                wallet.amount -= transaction.amount
            elif transaction.type == TransactionType.ADJUSTMENT:
                wallet.amount += transaction.amount
            else:
                print(f"Unknown transaction type: {transaction.type}")
                raise ValueError(f"Unknown transaction type: {transaction.type}")

        return wallet
    except Exception as e:
        db.rollback()
        raise e