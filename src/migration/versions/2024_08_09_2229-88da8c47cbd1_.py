from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '88da8c47cbd1'
down_revision: Union[str, None] = 'd05bf549c514'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('doctors', 'doctor')


def downgrade() -> None:
    op.rename_table('doctor', 'doctors')
