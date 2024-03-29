"""Updated attribute

Revision ID: a9e2cf1012f6
Revises: de92d05fc0ef
Create Date: 2023-05-02 09:07:44.075123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9e2cf1012f6'
down_revision = 'de92d05fc0ef'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_items_description', table_name='items')
    op.drop_index('ix_items_title', table_name='items')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_items_title', 'items', ['title'], unique=False)
    op.create_index('ix_items_description', 'items', ['description'], unique=False)
    # ### end Alembic commands ###
