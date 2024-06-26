"""empty message

Revision ID: e7f94d434d88
Revises: fd6617963ac6
Create Date: 2024-05-07 18:45:17.440139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7f94d434d88'
down_revision = 'fd6617963ac6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('daily_loop_exercises',
    sa.Column('daily_loop_id', sa.Integer(), nullable=False),
    sa.Column('exercise_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['daily_loop_id'], ['daily_loop.id'], ),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercises.id'], ),
    sa.PrimaryKeyConstraint('daily_loop_id', 'exercise_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('daily_loop_exercises')
    # ### end Alembic commands ###
