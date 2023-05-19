from .base_repository import BaseRepository
from typing import Any
from ..models.user_model import User

class SQLiteUserRepository(BaseRepository[User]):
    def __init__(self, connection: Any) -> None:
        self.__connection = connection
        self.__create_table()
        
    @property
    def connection(self) -> Any:
        return self.__connection
    
    @connection.setter
    def connection(self, connection: Any) -> None:
        self.__connection = connection
        
        
    def __create_table(self) -> None:
        cursor = self.connection.cursor()
        cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email_address TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            date_registered TEXT NOT NULL,
            date_updated TEXT
        )
        """
        )
        self.connection.commit()
        
    def add(self, user: User) -> User:
        cursor = self.connection.cursor()
        cursor.execute(
        """
        INSERT INTO users (first_name, last_name, email_address, password, date_registered) VALUES (?, ?, ?, ?, ?)
        """,
        (user.first_name, user.last_name, user.email_address, user.password, user.date_registered)
        )
        user.id = cursor.lastrowid
        return user
        
    def get_by_id(self, user_id: int) -> User:
        cursor = self.connection.cursor()
        cursor.execute(
        """
        SELECT id, first_name, last_name, email_address, password FROM users WHERE id=?
        """,
        ((user_id,))
        )
        row = cursor.fetchone()
        if row:
            return User(
                id=row[1],
                first_name=row[2],
                last_name=row[3],
                email_address=row[4],
                password=row[5]
            )
        return None
    
    def update(self, user: User) -> User:
        cursor = self.connection.cursor()
        cursor.execute(
        """
        UPDATE users SET first_name=?, last_name=?, email_address=?, password=? WHERE id=?
        """,
        (user.first_name, user.last_name, user.email_address, user.password)
        )
        return user
    
    def delete(self, user_id: int) -> User:
        cursor = self.connection.cursor()
        cursor.execute(
            """DELETE FROM users WHERE id=?""",
            (user_id,)
        )
        