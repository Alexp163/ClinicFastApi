"""empty message

Revision ID: 6553c66e19a9
Revises: c8e8e3d908dc
Create Date: 2024-08-11 19:50:10.858980

"""
from typing import Sequence, Union

from sqlalchemy import create_engine, text

from database import SQLALCHEMY_DATABASE_URI

# revision identifiers, used by Alembic.
revision: str = '6553c66e19a9'
down_revision: Union[str, None] = 'c8e8e3d908dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
engine = create_engine(SQLALCHEMY_DATABASE_URI.replace("+asyncpg", ""))


def upgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE patients RENAME TO patient"))


def downgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE patient RENAME TO patients"))


