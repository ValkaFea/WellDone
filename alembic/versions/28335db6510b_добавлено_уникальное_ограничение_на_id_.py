"""Добавлено уникальное ограничение на id_well и id_tag

Revision ID: 28335db6510b
Revises: c9cf24632e91
Create Date: 2025-02-17 13:30:41.511819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28335db6510b'
down_revision: Union[str, None] = 'c9cf24632e91'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
