"""set up database

Revision ID: 44a54c2bda72
Revises: 
Create Date: 2023-06-06 20:23:29.151583

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '44a54c2bda72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_index('description')
        batch_op.drop_index('title')

    op.drop_table('task')
    with op.batch_alter_table('team_member', schema=None) as batch_op:
        batch_op.drop_index('user_id')

    op.drop_table('team_member')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('username')

    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('password_hash', mysql.VARCHAR(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index('username', ['username'], unique=False)

    op.create_table('team_member',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('task_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('team_name', mysql.VARCHAR(length=120), nullable=True),
    sa.Column('task_name', mysql.VARCHAR(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('team_member', schema=None) as batch_op:
        batch_op.create_index('user_id', ['user_id'], unique=False)

    op.create_table('task',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('description', mysql.VARCHAR(length=500), nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('team_name', mysql.VARCHAR(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.create_index('title', ['title'], unique=False)
        batch_op.create_index('description', ['description'], unique=False)

    # ### end Alembic commands ###
