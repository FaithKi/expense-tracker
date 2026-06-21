from enum import Enum

class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"
    ADJUSTMENT = "adjustment"

class WalletUpdateType(Enum):
    INCOME = "income"
    EXPENSE = "expense"
    ADJUSTMENT = "adjustment"
    DELETE = "delete"