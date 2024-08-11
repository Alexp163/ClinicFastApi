"""empty message

Revision ID: d05bf549c514
Revises: a02d213a2da6
Create Date: 2024-08-09 22:17:49.625322

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy import text, create_engine
from sqlalchemy.dialects import postgresql

from database import SQLALCHEMY_DATABASE_URI

# revision identifiers, used by Alembic.
revision: str = 'd05bf549c514'
down_revision: Union[str, None] = 'a02d213a2da6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
engine = create_engine(SQLALCHEMY_DATABASE_URI.replace("+asyncpg", ""))


def upgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE doctors RENAME TO doctor;"))


def downgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE doctor RENAME TO doctors;"))
