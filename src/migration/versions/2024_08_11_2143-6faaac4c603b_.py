"""empty message

Revision ID: 6faaac4c603b
Revises: 6553c66e19a9
Create Date: 2024-08-11 21:43:46.934286

"""
from typing import Sequence, Union

from sqlalchemy import text, create_engine

from database import SQLALCHEMY_DATABASE_URI

# revision identifiers, used by Alembic.
revision: str = '6faaac4c603b'
down_revision: Union[str, None] = '6553c66e19a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
engine = create_engine(SQLALCHEMY_DATABASE_URI.replace("+asyncpg", ""))


def upgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE patients RENAME TO patient;"))


def downgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE patient RENAME TO patients;"))
