
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'fee9a20486c6'
down_revision: Union[str, None] = 'a4f67601f4b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('clinics', 'clinic')


def downgrade() -> None:
    op.rename_table('clinic', 'clinics')
