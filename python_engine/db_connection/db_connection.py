"""
Database Connection Module

This module provides database connection functionality for the Netflix ETL project.
It handles PostgreSQL connections using SQLAlchemy ORM.
"""

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
import pandas as pd


class DatabaseConnection:
    """
    A class to manage PostgreSQL database connections.
    
    This class encapsulates database connection details and provides
    methods to create and retrieve database engines.
    
    Attributes:
        user (str): Database user name
        password (str): Database password
        host (str): Database host address
        port (int): Database port number
        dbname (str): Database name
    """
    
    def __init__(self, user: str = "postgres", password: str = "postgres",
                 host: str = "localhost", port: int = 5432,
                 dbname: str = "netflix_db"):
        """
        Initialize database connection parameters.
        
        Args:
            user (str, optional): Database user name. Defaults to "postgres".
            password (str, optional): Database password. Defaults to "postgres".
            host (str, optional): Database host address. Defaults to "localhost".
            port (int, optional): Database port number. Defaults to 5432.
            dbname (str, optional): Database name. Defaults to "netflix_db".
        """
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.dbname = dbname
        self._engine = None
    
    def get_engine(self) -> Engine:
        """
        Create and return a SQLAlchemy database engine.
        
        The engine is cached after first creation to avoid creating
        multiple connections.
        
        Returns:
            Engine: SQLAlchemy engine object for database operations.
        """
        if self._engine is None:
            # Build PostgreSQL connection URL
            url = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
            self._engine = create_engine(url)
        return self._engine
    
    def execute_query(self, query: str) -> pd.DataFrame:
        """
        Execute a SQL query and return results as a DataFrame.
        
        Args:
            query (str): SQL query to execute.
            
        Returns:
            pd.DataFrame: Query results as a pandas DataFrame.
        """
        engine = self.get_engine()
        return pd.read_sql(query, engine)


# Legacy function for backward compatibility
def get_engine() -> Engine:
    """
    Get a database engine using default connection parameters.
    
    This function is maintained for backward compatibility.
    Use DatabaseConnection class for new code.
    
    Returns:
        Engine: SQLAlchemy engine object.
    """
    db_conn = DatabaseConnection()
    return db_conn.get_engine()


if __name__ == "__main__":
    # Test the database connection
    db_connection = DatabaseConnection()
    engine = db_connection.get_engine()
    print("Engine created:", engine)
    
    # Test query execution
    df = db_connection.execute_query("SELECT * FROM netflix_titles")
    print(f"Number of records: {len(df)}")