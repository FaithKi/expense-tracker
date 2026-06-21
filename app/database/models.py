from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import date

from ..utils.transaction_types import TransactionType

class Base(DeclarativeBase):
    pass

class Wallet(Base):
    __tablename__ = "wallets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    amount: Mapped[float]
    last_updated_by: Mapped[Transaction] = relationship()
    last_updated_when: Mapped[date]

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    amount: Mapped[float]
    category: Mapped[str | None] = None
    type: Mapped[TransactionType]
    wallet: Mapped[Wallet] = relationship()
    date: Mapped[date]