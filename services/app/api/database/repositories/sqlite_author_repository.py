# noqa: ignore=W291
from sqlite3 import IntegrityError
from typing import Any, Optional

from ...exceptions.exceptions import ResourceExistsException, ResourceNotExistException
from ..models.author_model import CommentAuthor
from .base_repository import BaseRepository


# flake8: noqa: W291
class SQLiteCommentAuthorRepository(BaseRepository[CommentAuthor]):
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
        CREATE TABLE IF NOT EXISTS comment_authors (
            author_id INTEGER PRIMARY KEY AUTOINCREMENT,
            author_display_name TEXT NOT NULL UNIQUE,
            author_profile_image_url TEXT,
            author_channel_url TEXT,
            author_channel_id TEXT,
            FOREIGN KEY (author_channel_id) REFERENCES channels (channel_id)
            ON DELETE cascade
            ON UPDATE cascade
        )
        """
        )
        self.connection.commit()

    def add(self, comment_author: CommentAuthor) -> CommentAuthor:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                """
            INSERT INTO comment_authors (author_display_name, author_profile_image_url,
            author_channel_url, author_channel_id) VALUES (?, ?, ?, ?)
            """,
                (
                    comment_author.author_display_name,
                    comment_author.author_profile_image_url,
                    comment_author.author_channel_url,
                    comment_author.author_channel_id,
                ),
            )
        except IntegrityError as e:
            raise ResourceExistsException("The comment_author already exists.") from e
        else:
            comment_author.author_id = cursor.lastrowid
            return comment_author

    def get_by_id(self, comment_author_id: int) -> CommentAuthor:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        SELECT author_id, author_display_name, author_profile_image_url, author_channel_url,
        author_channel_id FROM comment_authors WHERE author_id=?
        """,
            ((comment_author_id,)),
        )
        row = cursor.fetchone()
        if row:
            return CommentAuthor(
                author_id=row[0],
                author_display_name=row[1],
                author_profile_image_url=row[2],
                author_channel_url=row[3],
                author_channel_id=row[4],
            )
        raise ResourceNotExistException("The given comment author does not exist.")

    def get_by_email(self, author_display_name: str) -> CommentAuthor:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        SELECT id, author_display_name, author_profile_image_url, author_channel_url,
        author_channel_id FROM comment_authors WHERE author_display_name=?
        """,
            ((author_display_name,)),
        )
        row = cursor.fetchone()
        if row:
            return CommentAuthor(
                author_id=row[0],
                author_display_name=row[1],
                author_profile_image_url=row[2],
                author_channel_url=row[3],
                author_channel_id=row[4],
            )
        raise ResourceNotExistException("The given comment author does not exist.")

    def update(self, comment_author: CommentAuthor) -> CommentAuthor:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        UPDATE comment_authors SET author_display_name=?, author_profile_image_url=?,
        author_channel_url=?, author_channel_id=? WHERE author_id=?
        """,
            (
                comment_author.author_display_name,
                comment_author.author_profile_image_url,
                comment_author.author_channel_url,
                comment_author.author_channel_id,
                comment_author.author_id,
            ),
        )
        return comment_author

    def delete(self, author_id: int) -> None:
        cursor = self.connection.cursor()
        cursor.execute("""DELETE FROM comment_authors WHERE author_id=?""", (author_id,))

    def list_all(self) -> list[CommentAuthor]:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        SELECT author_id, author_display_name, author_profile_image_url, author_channel_url,
        author_channel_id FROM comment_authors;
        """
        )
        rows = cursor.fetchall()
        if rows:
            comment_authors = [
                CommentAuthor(
                    author_id=row[0],
                    author_display_name=row[1],
                    author_profile_image_url=row[2],
                    author_channel_url=row[3],
                    author_channel_id=row[4],
                )
                for row in rows
            ]
            return comment_authors
        return []

    def query(self, query_string: str) -> list[CommentAuthor]:
        cursor = self.connection.cursor()
        cursor.execute(query_string)
        rows = cursor.fetchall()
        if rows:
            comment_authors = [
                CommentAuthor(
                    author_id=row[0],
                    author_display_name=row[1],
                    author_profile_image_url=row[2],
                    author_channel_url=row[3],
                    author_channel_id=row[4],
                )
                for row in rows
            ]
        return comment_authors if comment_authors else []
