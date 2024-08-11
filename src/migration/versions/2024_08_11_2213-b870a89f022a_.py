"""empty message

Revision ID: b870a89f022a
Revises: 6faaac4c603b
Create Date: 2024-08-11 22:13:23.262163

"""
from typing import Sequence, Union

from sqlalchemy import create_engine, text

from database import SQLALCHEMY_DATABASE_URI

# revision identifiers, used by Alembic.
revision: str = 'b870a89f022a'
down_revision: Union[str, None] = '6faaac4c603b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
engine = create_engine(SQLALCHEMY_DATABASE_URI.replace("+asyncpg", ""))


def upgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE patients RENAME TO patient;"))


def downgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE patient RENAME TO patients;"))

