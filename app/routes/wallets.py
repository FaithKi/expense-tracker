from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.wallet import WalletCreate
from app.services import wallet_service

router = APIRouter(
    prefix="/wallets",
    tags=["wallets"]
)

@router.get("/")
def list_wallets(db: Session = Depends(get_db)):
    return {"message": "success", "wallets": wallet_service.get_all_wallets(db)}

@router.post("/")
def create_new_wallet(wallet: WalletCreate, db: Session = Depends(get_db)):
    created_wallet = wallet_service.create_wallet(db, wallet)
    return {"message": "created", "wallet": created_wallet}