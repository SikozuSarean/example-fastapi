"""add content column to posts table

Revision ID: 1b860fdd2c44
Revises: aca6e98939f3
Create Date: 2023-09-08 12:09:21.801065

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b860fdd2c44'
down_revision: Union[str, None] = 'aca6e98939f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
