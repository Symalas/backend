"""kelas

Revision ID: f76f4a23e221
Revises: 2c9102d87398
Create Date: 2022-10-20 13:00:14.730760

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f76f4a23e221'
down_revision = '2c9102d87398'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lecturer',
    sa.Column('nidn', sa.String(length=20), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('nidn')
    )
    op.create_table('student',
    sa.Column('npm', sa.String(length=20), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('npm')
    )
    op.create_table('student_class',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('code', sa.String(length=7), nullable=False),
    sa.Column('npm', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['npm'], ['student.npm'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('class_member',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('npm', sa.String(length=20), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('pending', 'accepted'), nullable=False),
    sa.Column('role', sa.Enum('member', 'admin', 'super_admin'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['student_class.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['npm'], ['student.npm'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('mahasiswa')
    op.drop_table('dosen')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dosen',
    sa.Column('nidn', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=250), nullable=False),
    sa.Column('userid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], name='dosen_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('nidn'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('mahasiswa',
    sa.Column('npm', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=250), nullable=False),
    sa.Column('userid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], name='mahasiswa_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('npm'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('class_member')
    op.drop_table('student_class')
    op.drop_table('student')
    op.drop_table('lecturer')
    # ### end Alembic commands ###
