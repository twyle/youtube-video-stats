from contextlib import contextmanager
import sqlite3

@contextmanager
def create_sqlite_database_connection():
    db_connection = sqlite3.connect('data.db')
    try:
        yield db_connection
    finally:
        db_connection.close()