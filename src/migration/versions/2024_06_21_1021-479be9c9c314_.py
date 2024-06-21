"""empty message

Revision ID: 479be9c9c314
Revises: ca7d9b8f7d87
Create Date: 2024-06-21 10:21:39.666346

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '479be9c9c314'
down_revision: Union[str, None] = 'ca7d9b8f7d87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    op.add_column('user', sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'updated_at')
    op.drop_column('user', 'created_at')
    # ### end Alembic commands ###
