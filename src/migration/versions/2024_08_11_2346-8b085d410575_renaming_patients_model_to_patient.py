from typing import Sequence, Union

from alembic import op


revision: str = '8b085d410575'
down_revision: Union[str, None] = 'fee9a20486c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('patients', 'patient')


def downgrade() -> None:
    op.rename_table('patient', 'patients')
