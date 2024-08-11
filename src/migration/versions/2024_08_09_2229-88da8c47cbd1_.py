"""empty message

Revision ID: 88da8c47cbd1
Revises: d05bf549c514
Create Date: 2024-08-09 22:29:24.423029

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '88da8c47cbd1'
down_revision: Union[str, None] = 'd05bf549c514'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('doctors', 'doctor')


def downgrade() -> None:
    op.rename_table('doctor', 'doctors')
