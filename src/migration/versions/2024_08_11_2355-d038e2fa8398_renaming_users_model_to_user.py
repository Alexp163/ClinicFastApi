
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'd038e2fa8398'
down_revision: Union[str, None] = '8b085d410575'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('users', 'user')


def downgrade() -> None:
    op.rename_table('user', 'users')
