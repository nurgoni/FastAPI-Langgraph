"""add_uuid_extension

Revision ID: 1bb0adbfa81f
Revises: aade2d1f17bf
Create Date: 2025-06-03 14:53:44.829235

"""
from typing import Sequence, Union
from alembic import op


# revision identifiers, used by Alembic.
revision: str = '1bb0adbfa81f'
down_revision: Union[str, None] = 'aade2d1f17bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')


def downgrade() -> None:
    op.execute('DROP EXTENSION IF EXISTS "uuid-ossp"')
