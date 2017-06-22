"""empty message

Revision ID: 709df432cc5b
Revises: e0e7a65c8673
Create Date: 2017-06-22 10:33:56.868000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '709df432cc5b'
down_revision = 'e0e7a65c8673'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
