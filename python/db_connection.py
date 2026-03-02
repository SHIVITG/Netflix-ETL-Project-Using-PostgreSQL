"""Helper module for creating a PostgreSQL connection using SQLAlchemy."""
import os
from sqlalchemy import create_engine


def get_engine(user=None, password=None, host="localhost", port=5432, dbname=None):
    """Return an SQLAlchemy engine for the specified credentials.

    Credentials can be supplied through parameters or environment variables:
    PGUSER, PGPASSWORD, PGHOST, PGPORT, PGDATABASE.
    """
    user = user or os.getenv("PGUSER")
    password = password or os.getenv("PGPASSWORD")
    host = host or os.getenv("PGHOST", "localhost")
    port = port or os.getenv("PGPORT", 5432)
    dbname = dbname or os.getenv("PGDATABASE")

    if not all([user, password, dbname]):
        raise ValueError("Database credentials (user, password, dbname) are required")

    url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    return create_engine(url)


if __name__ == "__main__":
    # quick smoke test
    engine = get_engine()
    print("Engine created:", engine)
