"""empty message

Revision ID: 89d483518ab8
Revises: dad803fb7cfb
Create Date: 2024-08-15 22:15:20.868066

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89d483518ab8'
down_revision: Union[str, None] = 'dad803fb7cfb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient', sa.Column('hospital_room_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'patient', 'hospital_room', ['hospital_room_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'patient', type_='foreignkey')
    op.drop_column('patient', 'hospital_room_id')
    # ### end Alembic commands ###
