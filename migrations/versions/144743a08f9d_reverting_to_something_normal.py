"""reverting to something normal

Revision ID: 144743a08f9d
Revises: 3c0e045cf9cb
Create Date: 2024-01-02 21:43:33.458858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '144743a08f9d'
down_revision: Union[str, None] = '3c0e045cf9cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('security_daily_price', 'id')
    op.drop_column('security_minute_price', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('security_minute_price', sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('security_daily_price', sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###