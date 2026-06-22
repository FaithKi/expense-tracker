from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.wallet import WalletCreate
from app.services.wallet_service import create_wallet, delete_wallet_by_id, get_all_wallets, get_wallet_by_id, update_wallet

router = APIRouter(
    prefix="/wallets",
    tags=["wallets"]
)

@router.get("/")
def list_wallets(db: Session = Depends(get_db)):
    return {"message": "success", "wallets": get_all_wallets(db)}

@router.post("/")
def create_new_wallet(wallet: WalletCreate, db: Session = Depends(get_db)):
    created_wallet = create_wallet(db, wallet)
    return {"message": "created", "wallet": created_wallet}

@router.get("/{wallet_id}")
def get_wallet(wallet_id: int, db: Session = Depends(get_db)):
    wallet = get_wallet_by_id(db, wallet_id)
    if wallet:
        return {"message": "success", "wallet": wallet}
    else:
        return {"message": "wallet not found"}
    
@router.delete("/{wallet_id}")
def delete_wallet(wallet_id: int, db: Session = Depends(get_db)):
    result = delete_wallet_by_id(db, wallet_id)
    if result:
        return {"message": "deleted"}
    else:
        return {"message": "wallet not found"}