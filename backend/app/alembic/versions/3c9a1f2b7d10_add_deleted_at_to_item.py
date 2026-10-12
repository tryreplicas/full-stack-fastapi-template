"""Add deleted_at to Item for soft delete

Revision ID: 3c9a1f2b7d10
Revises: fe56fa70289e
Create Date: 2026-10-12 01:10:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c9a1f2b7d10'
down_revision = 'fe56fa70289e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('item', sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True))
    op.create_index(op.f('ix_item_deleted_at'), 'item', ['deleted_at'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_item_deleted_at'), table_name='item')
    op.drop_column('item', 'deleted_at')
