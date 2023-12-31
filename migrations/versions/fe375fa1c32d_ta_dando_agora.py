"""ta dando agora

Revision ID: fe375fa1c32d
Revises: 1a3498493247
Create Date: 2023-11-14 21:34:26.276952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe375fa1c32d'
down_revision = '1a3498493247'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=60), nullable=True))
        batch_op.alter_column('body',
               existing_type=sa.VARCHAR(length=140),
               type_=sa.String(length=300),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('body',
               existing_type=sa.String(length=300),
               type_=sa.VARCHAR(length=140),
               existing_nullable=True)
        batch_op.drop_column('title')

    # ### end Alembic commands ###
