"""create post table

Revision ID: 3397442bad34
Revises: 
Create Date: 2022-06-20 16:41:26.310658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3397442bad34'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer, nullable=False, primary_key=True),
    sa.Column('title',sa.String,nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
