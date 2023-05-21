from .base_repository import BaseRepository
from typing import Any, Optional
from ..models.user_model import User
from sqlite3 import IntegrityError

class SQLiteUserRepository(BaseRepository[User]):
    def __init__(self, connection: Optional[Any] = None) -> None:
        self.__connection = connection
        
    @property
    def connection(self) -> Any:
        return self.__connection
    
    @connection.setter
    def connection(self, connection: Any) -> None:
        self.__connection = connection
        self.__create_table()
              
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
        try:
            cursor.execute(
            """
            INSERT INTO users (first_name, last_name, email_address, password, date_registered) VALUES (?, ?, ?, ?, ?)
            """,
            (user.first_name, user.last_name, user.email_address, user.password, user.date_registered)
            )
        except IntegrityError as e:
            raise ValueError('The user already exists.') from e
        else:
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
                id=row[0],
                first_name=row[1],
                last_name=row[2],
                email_address=row[3],
                password=row[4]
            )
        return None
    
    def update(self, user: User) -> User:
        cursor = self.connection.cursor()
        cursor.execute(
        """
        UPDATE users SET first_name=?, last_name=?, email_address=?, password=? WHERE id=?
        """,
        (user.first_name, user.last_name, user.email_address, user.password, user.id)
        )
        return user
    
    def delete(self, user_id: int) -> None:
        cursor = self.connection.cursor()
        cursor.execute(
            """DELETE FROM users WHERE id=?""",
            (user_id,)
        )
        
    def list_all(self) -> list[User]:
        cursor = self.connection.cursor()
        cursor.execute(
        """
        SELECT * FROM users
        """
        )
        rows = cursor.fetchall()
        if rows:
            users = [
                User(
                    id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    email_address=row[3],
                    password=row[4]
                )
                for row in rows
            ]
        return users if users else []
    
    def query(self, query_string: str) -> list[User]:
        cursor = self.connection.cursor()
        cursor.execute(query_string)
        rows = cursor.fetchall()
        if rows:
            users = [
                User(
                    id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    email_address=row[3],
                    password=row[4]
                )
                for row in rows
            ]
        return users if users else []