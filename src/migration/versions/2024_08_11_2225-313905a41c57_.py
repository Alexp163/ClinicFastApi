"""empty message

Revision ID: 313905a41c57
Revises: b870a89f022a
Create Date: 2024-08-11 22:25:43.381188

"""
from typing import Sequence, Union

from sqlalchemy import create_engine, text

from database import SQLALCHEMY_DATABASE_URI

# revision identifiers, used by Alembic.
revision: str = '313905a41c57'
down_revision: Union[str, None] = 'b870a89f022a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

engine = create_engine(SQLALCHEMY_DATABASE_URI.replace("+asyncpg", ""))


def upgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE users RENAME TO user;"))


def downgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE user RENAME TO users;"))
