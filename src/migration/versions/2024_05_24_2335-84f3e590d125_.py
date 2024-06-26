"""empty message

Revision ID: 84f3e590d125
Revises: d53278f002d8
Create Date: 2024-05-24 23:35:17.959879

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84f3e590d125'
down_revision: Union[str, None] = 'd53278f002d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('corpus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('clinic', sa.Column('address', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('clinic', 'address')
    op.drop_table('corpus')
    # ### end Alembic commands ###
