from typing import Sequence, Union

from sqlalchemy import text, create_engine

from database import SQLALCHEMY_DATABASE_URI

# revision identifiers, used by Alembic.
revision: str = 'a02d213a2da6'
down_revision: Union[str, None] = '25b08d12471a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
engine = create_engine(SQLALCHEMY_DATABASE_URI.replace("+asyncpg", ""))


def upgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE doctors RENAME TO doctor;"))


def downgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE doctor RENAME TO doctors;"))

