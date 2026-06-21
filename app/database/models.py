from __future__ import annotations
from datetime import datetime, UTC

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from ..utils.enums import TransactionType

class Base(DeclarativeBase):
    pass

class Wallet(Base):
    __tablename__ = "wallets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    amount: Mapped[float]
    transactions: Mapped[list[Transaction]] = relationship(back_populates="wallet")
    updated_when: Mapped[datetime] = mapped_column(
        default=datetime.now(UTC),
        onupdate=datetime.now(UTC)
    )

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    amount: Mapped[float]
    category: Mapped[str | None] = None
    type: Mapped[TransactionType]
    wallet_id: Mapped[int] = mapped_column(ForeignKey("wallets.id"))
    wallet: Mapped[Wallet] = relationship(back_populates="transactions")
    date: Mapped[datetime] = mapped_column(
        default=datetime.now(UTC),
        onupdate=datetime.now(UTC)
    )