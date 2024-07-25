"""empty message

Revision ID: fa6cca4ac270
Revises: 5fa4dc9e5fa2
Create Date: 2024-07-25 23:12:58.649158

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fa6cca4ac270'
down_revision: Union[str, None] = '5fa4dc9e5fa2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hospital_room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.String(), nullable=False),
    sa.Column('number_beds', sa.String(), nullable=False),
    sa.Column('nurse', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hospital_room')
    # ### end Alembic commands ###
