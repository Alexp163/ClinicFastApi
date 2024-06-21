"""empty message

Revision ID: 6523278fa0ae
Revises: 62a8d40d2c68
Create Date: 2024-06-18 22:56:11.943323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '6523278fa0ae'
down_revision: Union[str, None] = '62a8d40d2c68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('clinic', 'name',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.alter_column('clinic', 'address',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('clinic', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('now()'))
    op.alter_column('clinic', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('clinic', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('clinic', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text('now()'))
    op.alter_column('clinic', 'address',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('clinic', 'name',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    # ### end Alembic commands ###
