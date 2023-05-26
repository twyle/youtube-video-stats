from .base_repository import BaseRepository
from typing import Any, Optional
from ..models.user_model import User
from sqlite3 import IntegrityError
from ...exceptions.exceptions import ResourceExistsException, ResourceNotExistException

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
            date_updated TEXT,
            account_activated INTEGER,
            role TEXT
        )
        """
        )
        self.connection.commit()
        
    def add(self, user: User) -> User:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
            """
            INSERT INTO users (first_name, last_name, email_address, password, date_registered, 
            date_updated, account_activated, role) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (user.first_name, user.last_name, user.email_address, user.password, 
             user.date_registered, user.date_updated, user.account_activated, user.role)
            )
        except IntegrityError as e:
            raise ResourceExistsException('The user already exists.') from e
        else:
            user.id = cursor.lastrowid
            return user
        
    def get_by_id(self, user_id: int) -> User:
        cursor = self.connection.cursor()
        cursor.execute(
        """
        SELECT id, first_name, last_name, email_address, password, date_registered, date_updated, 
        account_activated, role FROM users WHERE id=?
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
                password=row[4],
                date_registered=row[5],
                date_updated=row[6],
                account_activated=row[7],
                role=row[8]
            )
        raise ResourceNotExistException('The given user does not exist.')
    
    def get_by_email(self, user_email: str) -> User:
        cursor = self.connection.cursor()
        cursor.execute(
        """
        SELECT id, first_name, last_name, email_address, password, date_registered, date_updated, 
        account_activated, role FROM users WHERE email_address=?
        """,
        ((user_email,))
        )
        row = cursor.fetchone()
        if row:
            return User(
                id=row[0],
                first_name=row[1],
                last_name=row[2],
                email_address=row[3],
                password=row[4],
                date_registered=row[5],
                date_updated=row[6],
                account_activated=row[7],
                role=row[8]
            )
        raise ResourceNotExistException('The given user does not exist.')
    
    def update(self, user: User) -> User:
        cursor = self.connection.cursor()
        cursor.execute(
        """
        UPDATE users SET first_name=?, last_name=?, email_address=?, password=?, account_activated=?
        , role=? WHERE id=?
        """,
        (user.first_name, user.last_name, user.email_address, user.password, user.account_activated, 
         user.role, user.id)
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
                    password=row[4],
                    date_registered=row[5],
                    date_updated=row[6],
                    account_activated=row[7],
                    role=row[8]
                )
                for row in rows
            ]
            return users
        return []
    
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
                    password=row[4],
                    date_registered=row[5],
                    date_updated=row[6],
                    account_activated=row[7],
                    role=row[8]
                )
                for row in rows
            ]
        return users if users else []