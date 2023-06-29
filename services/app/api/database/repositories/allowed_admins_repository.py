from sqlite3 import IntegrityError
from typing import Any, Optional

from ...exceptions.exceptions import ResourceExistsException, ResourceNotExistException
from ..models.allowed_admin_model import AllowedAdmin
from .base_repository import BaseRepository


# flake8: noqa: W291
class SQLiteAllowedAdminRepository(BaseRepository[AllowedAdmin]):
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
        CREATE TABLE IF NOT EXISTS allowed_admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email_address TEXT NOT NULL UNIQUE
        )
        """
        )
        self.connection.commit()

    def add(self, email: str) -> str:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                """
            INSERT INTO allowed_admins (email_address) VALUES (?)
            """,
                (email),
            )
        except IntegrityError as e:
            raise ResourceExistsException(f"The email address {email} already exists.") from e
        else:
            return email

    def get_by_id(self, id: int) -> AllowedAdmin:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        SELECT id, email_address FROM allowed_admins WHERE id=?
        """,
            ((id,)),
        )
        row = cursor.fetchone()
        if row:
            return AllowedAdmin(id=row[0], email_address=row[1])
        raise ResourceNotExistException(f"The given admin  email does not exist.")

    def get_by_email(self, email: str) -> AllowedAdmin:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        SELECT id, email_address FROM allowed_admins WHERE email_address=?
        """,
            ((email,)),
        )
        row = cursor.fetchone()
        if row:
            return AllowedAdmin(id=row[0], email_address=row[1])
        return None

    def update(self, allowed_admin: AllowedAdmin) -> AllowedAdmin:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        UPDATE allowed_admins SET email_address=? WHERE id=?
        """,
            (
                allowed_admin.email_address,
                allowed_admin.id,
            ),
        )
        return allowed_admin

    def delete(self, id: int) -> None:
        cursor = self.connection.cursor()
        cursor.execute("""DELETE FROM allowed_admins WHERE id=?""", (id,))

    def list_all(self) -> list[AllowedAdmin]:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        SELECT * FROM allowed_admins
        """
        )
        rows = cursor.fetchall()
        if rows:
            allowed_admins = [AllowedAdmin(id=row[0], email_address=row[1]) for row in rows]
            return allowed_admins
        return []

    def query(self, query_string: str) -> list[AllowedAdmin]:
        return super().query(query_string)
