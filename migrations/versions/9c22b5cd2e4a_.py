"""empty message

Revision ID: 9c22b5cd2e4a
Revises: af39e3a74e06
Create Date: 2019-07-10 15:53:23.009142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c22b5cd2e4a'
down_revision = 'af39e3a74e06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('taxi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lon', sa.String(length=64), nullable=True),
    sa.Column('lat', sa.String(length=64), nullable=True),
    sa.Column('timestamp', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('taxi')
    # ### end Alembic commands ###