"""empty message

Revision ID: 14a732d9582a
Revises: 951ca93bd571
Create Date: 2024-06-21 00:07:04.679615

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '14a732d9582a'
down_revision: Union[str, None] = '951ca93bd571'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('corpus', 'name',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.alter_column('corpus', 'profile',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.alter_column('corpus', 'year_release',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('corpus', 'floors',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('corpus', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('now()'))
    op.alter_column('corpus', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('user', 'age',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('user', 'address',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('user', 'address',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('user', 'age',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('corpus', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('corpus', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text('now()'))
    op.alter_column('corpus', 'floors',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('corpus', 'year_release',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('corpus', 'profile',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.alter_column('corpus', 'name',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    # ### end Alembic commands ###
