"""empty message

Revision ID: 438160281087
Revises: aa21fcfd003a
Create Date: 2017-04-27 03:06:26.262445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '438160281087'
down_revision = 'aa21fcfd003a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('item', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('item', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
