"""empty message

Revision ID: 4a16e57b6b05
Revises: 
Create Date: 2018-10-03 16:20:43.779202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a16e57b6b05'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('email_address', sa.String(length=50), nullable=True),
    sa.Column('user_type', sa.Enum('superuser', 'adminuser', 'normaluser', name='myenum'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_address'),
    sa.UniqueConstraint('username')
    )
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contacts')
    op.drop_table('users')
    # ### end Alembic commands ###