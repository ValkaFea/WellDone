"""Добавлено уникальное ограничение на id_well и id_tag

Revision ID: c9cf24632e91
Revises: 9fdacf59bb28
Create Date: 2025-02-17 13:28:22.859711

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9cf24632e91'
down_revision: Union[str, None] = '9fdacf59bb28'
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
