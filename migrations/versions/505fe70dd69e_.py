"""empty message

Revision ID: 505fe70dd69e
Revises: 22446c128767
Create Date: 2025-05-21 09:06:08.711010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '505fe70dd69e'
down_revision = '22446c128767'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.add_column(sa.Column('post_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'post', ['post_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('post_id')

    # ### end Alembic commands ###
