"""empty message

Revision ID: 0dc5219784bf
Revises: b3f2f59a0822
Create Date: 2024-08-13 22:48:38.496536

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0dc5219784bf'
down_revision: Union[str, None] = 'b3f2f59a0822'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('building', sa.Column('clinic_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'building', 'clinic', ['clinic_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'building', type_='foreignkey')
    op.drop_column('building', 'clinic_id')
    # ### end Alembic commands ###