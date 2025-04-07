"""phone number added

Revision ID: 4b735f614009
Revises: 
Create Date: 2025-01-10 01:28:04.765919

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b735f614009'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True))


def downgrade() -> None:
    #op.drop_column("users","phone_number")
    pass
