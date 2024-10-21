"""Initial migration

Revision ID: d921df2bd2a8
Revises: 
Create Date: 2024-10-20 14:30:48.220226

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd921df2bd2a8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_posts_id', table_name='posts')
    op.drop_table('posts')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key'),
    sa.UniqueConstraint('username', name='users_username_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('content', sa.VARCHAR(length=500), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='posts_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='posts_pkey'),
    sa.UniqueConstraint('title', name='posts_title_key')
    )
    op.create_index('ix_posts_id', 'posts', ['id'], unique=False)
    # ### end Alembic commands ###
