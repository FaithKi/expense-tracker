"""enable cascade delete on wallet->transaction

Revision ID: 6ae8efa7afeb
Revises: 96cbfbf37ac2
Create Date: 2026-06-22 16:37:33.216202

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ae8efa7afeb'
down_revision: Union[str, Sequence[str], None] = '96cbfbf37ac2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
