
from typing import Sequence, Union

from sqlalchemy import text, create_engine

from database import SQLALCHEMY_DATABASE_URI

# revision identifiers, used by Alembic.
revision: str = 'c8e8e3d908dc'
down_revision: Union[str, None] = '88da8c47cbd1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
engine = create_engine(SQLALCHEMY_DATABASE_URI.replace("+asyncpg", ""))


def upgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE buildings RENAME TO building;"))


def downgrade() -> None:
    with engine.connect() as con:
        con.execute(text("ALTER TABLE building RENAME TO building;"))
