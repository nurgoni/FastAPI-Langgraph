"""change_id_to_uuid

Revision ID: 151461579a81
Revises: 1bb0adbfa81f
Create Date: 2025-06-03 14:53:44.829235

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import uuid


# revision identifiers, used by Alembic.
revision: str = '151461579a81'
down_revision: Union[str, None] = '1bb0adbfa81f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add a new UUID column
    op.add_column('users', sa.Column('uuid_id', postgresql.UUID(as_uuid=True), nullable=True))
    
    # Create a connection to execute SQL
    connection = op.get_bind()
    
    # Update existing rows with new UUIDs
    connection.execute(sa.text(
        "UPDATE users SET uuid_id = uuid_generate_v4();"
    ))
    
    # Make the new column not nullable
    op.alter_column('users', 'uuid_id', nullable=False)
    
    # Drop the old ID column and primary key constraint
    op.drop_constraint('users_pkey', 'users', type_='primary')
    op.drop_column('users', 'id')
    
    # Rename the new column to 'id'
    op.alter_column('users', 'uuid_id', new_column_name='id')
    
    # Add primary key constraint to the new id column
    op.create_primary_key('users_pkey', 'users', ['id'])


def downgrade() -> None:
    # Add old integer ID column
    op.add_column('users', sa.Column('int_id', sa.Integer(), nullable=True))
    
    # Create sequence for ID
    op.execute('CREATE SEQUENCE users_id_seq')
    op.execute('ALTER TABLE users ALTER COLUMN int_id SET DEFAULT nextval(\'users_id_seq\')')
    
    # Fill in sequential IDs
    op.execute('UPDATE users SET int_id = nextval(\'users_id_seq\')')
    
    # Make int_id not nullable
    op.alter_column('users', 'int_id', nullable=False)
    
    # Drop the UUID column and its primary key
    op.drop_constraint('users_pkey', 'users', type_='primary')
    op.drop_column('users', 'id')
    
    # Rename int_id back to id
    op.alter_column('users', 'int_id', new_column_name='id')
    
    # Recreate primary key
    op.create_primary_key('users_pkey', 'users', ['id'])
    
    # Set the sequence owned by the id column
    op.execute('ALTER SEQUENCE users_id_seq OWNED BY users.id')
