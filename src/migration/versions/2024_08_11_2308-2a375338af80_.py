from typing import Sequence, Union

from sqlalchemy import text, create_engine

from database import SQLALCHEMY_DATABASE_URI

# revision identifiers, used by Alembic.
revision: str = '2a375338af80'
down_revision: Union[str, None] = 'b25a00c7417f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
engine = create_engine(SQLALCHEMY_DATABASE_URI.replace("+asyncpg", ""))


def upgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE clinics RENAME TO clinic;"))


def downgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE clinic RENAME TO clinics"))