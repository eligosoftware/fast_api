"""added content column to posts table

Revision ID: e59edd53e147
Revises: 3397442bad34
Create Date: 2022-06-20 16:54:44.835644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e59edd53e147'
down_revision = '3397442bad34'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
