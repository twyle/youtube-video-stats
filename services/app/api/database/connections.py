import os
import sqlite3
from contextlib import contextmanager

from dotenv import load_dotenv
from flask import current_app

load_dotenv()


@contextmanager
def create_sqlite_database_connection():
    db_connection = sqlite3.connect(os.environ.get("DB"))
    try:
        yield db_connection
    finally:
        db_connection.close()
