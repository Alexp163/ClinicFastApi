from typing import Sequence, Union

from alembic import op


revision: str = 'b3f2f59a0822'
down_revision: Union[str, None] = 'd038e2fa8398'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('buildings', 'building')


def downgrade() -> None:
    op.rename_table('building', 'buildings')
