"""Allow null in data_vendor_id

Revision ID: 50acdfd3805b
Revises: 5e66ce2dfa17
Create Date: 2024-01-02 21:28:57.760686

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50acdfd3805b'
down_revision: Union[str, None] = '5e66ce2dfa17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('security_daily_price', 'data_vendor_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('security_daily_price', 'data_vendor_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
