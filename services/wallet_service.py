from sqlalchemy.orm import Session
from app.database.models import Wallet
from app.schemas.wallet import WalletCreate

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