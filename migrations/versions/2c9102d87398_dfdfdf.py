"""dfdfdf

Revision ID: 2c9102d87398
Revises: cae94e7e5a36
Create Date: 2022-10-19 17:43:58.088976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c9102d87398'
down_revision = 'cae94e7e5a36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('role', sa.Enum('mahasiswa', 'dosen'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('dosen',
    sa.Column('nidn', sa.String(length=20), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('nidn')
    )
    op.create_table('mahasiswa',
    sa.Column('npm', sa.String(length=20), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('npm')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mahasiswa')
    op.drop_table('dosen')
    op.drop_table('user')
    # ### end Alembic commands ###
