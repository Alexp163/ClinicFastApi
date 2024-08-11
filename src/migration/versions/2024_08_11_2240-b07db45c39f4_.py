"""empty message

Revision ID: b07db45c39f4
Revises: 313905a41c57
Create Date: 2024-08-11 22:40:18.250344

"""
from typing import Sequence, Union

from sqlalchemy import text, create_engine

from database import SQLALCHEMY_DATABASE_URI

# revision identifiers, used by Alembic.
revision: str = 'b07db45c39f4'
down_revision: Union[str, None] = '313905a41c57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
engine = create_engine(SQLALCHEMY_DATABASE_URI.replace("+asyncpg", ""))


def upgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE patients RENAME TO patient;"))


def downgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE patient RENAME TO patients;"))
