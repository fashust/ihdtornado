"""users - add avatar field

Revision ID: 24a0bf271ee
Revises: 3fb0f9f51f
Create Date: 2014-07-17 14:46:05.928903

"""

# revision identifiers, used by Alembic.
revision = '24a0bf271ee'
down_revision = '3fb0f9f51f'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils as su


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar', su.URLType(), nullable=True,
                                     default=None))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar')
    ### end Alembic commands ###
