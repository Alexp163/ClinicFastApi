"""empty message

Revision ID: 564fba7115bf
Revises: fdb6f4eb15af
Create Date: 2024-08-15 21:37:38.942891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '564fba7115bf'
down_revision: Union[str, None] = 'fdb6f4eb15af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'patient', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'patient', type_='foreignkey')
    op.drop_column('patient', 'user_id')
    # ### end Alembic commands ###