"""empty message

Revision ID: dad803fb7cfb
Revises: f290721078cb
Create Date: 2024-08-15 22:04:45.009273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dad803fb7cfb'
down_revision: Union[str, None] = 'f290721078cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient', sa.Column('patient_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'patient', 'patient', ['patient_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'patient', type_='foreignkey')
    op.drop_column('patient', 'patient_id')
    # ### end Alembic commands ###