"""add last few columns to posts table

Revision ID: 07ea9326fcb3
Revises: 9d85921f8b70
Create Date: 2022-06-28 02:02:21.719135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07ea9326fcb3'
down_revision = '9d85921f8b70'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published',sa.Boolean(),nullable=False, server_default='TRUE'),)
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False, server_default=
    sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
