"""create users table

Revision ID: 9b301ea549d4
Revises: 
Create Date: 2024-04-01 23:21:23.231685+09:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b301ea549d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
         sa.Column('id', sa.Integer, primary_key=True),
         sa.Column('username', sa.String(128), nullable=False),
         sa.Column('created_at', sa.DateTime, nullable=False),
         sa.Column('is_admin', sa.Boolean, nullable=False),
     )



def downgrade():
    op.drop_table('users')
