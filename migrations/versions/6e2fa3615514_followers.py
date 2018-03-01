"""followers

Revision ID: 6e2fa3615514
Revises: 0d4e565d0b3d
Create Date: 2018-03-01 12:17:48.097226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e2fa3615514'
down_revision = '0d4e565d0b3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
