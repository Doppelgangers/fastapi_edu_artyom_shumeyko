from datetime import datetime

import sqlalchemy
from sqlalchemy import MetaData, Table, Column

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", sqlalchemy.Integer, primary_key=True),
    Column("name", sqlalchemy.String, nullable=False),
    Column("premissions", sqlalchemy.JSON),
)

user = Table(
    "users",
    metadata,
    Column("id", sqlalchemy.Integer, primary_key=True),
    Column("username"),
    Column("password"),
    Column("date_registered", sqlalchemy.TIMESTAMP, default=datetime.utcnow),
    Column("role_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("roles.id")),
)
