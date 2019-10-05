"""empty message

Revision ID: 28dc12a66370
Revises: 
Create Date: 2019-09-29 15:51:55.934048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28dc12a66370'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('following',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('following_id', sa.Integer(), nullable=True),
    sa.Column('followed_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('follower_id', 'following_id', name='_follower_following_uc')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('following')
    # ### end Alembic commands ###