from sqlite3 import IntegrityError
from typing import Any, Optional

from ...exceptions.exceptions import ResourceExistsException, ResourceNotExistException
from ..models.comment_model import Comment
from .base_repository import BaseRepository


# flake8: noqa: W291
class SQLiteCommentRepository(BaseRepository[Comment]):
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
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            video_id TEXT NOT NULL,
            comment_id TEXT NOT NULL UNIQUE,
            comment_text TEXT,
            parent_id TEXT,
            like_count INTEGER,
            published_at TEXT,
            updated_at TEXT,
            FOREIGN KEY (video_id) references videos (video_id)
            ON UPDATE cascade
            ON DELETE cascade
        )
        """
        )
        self.connection.commit()

    def add(self, comment: Comment) -> Comment:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                """
            INSERT INTO comments (video_id, comment_id, comment_text, parent_id, like_count,
            published_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    comment.video_id,
                    comment.comment_id,
                    comment.comment_text,
                    comment.parent_id,
                    comment.like_count,
                    comment.published_at,
                    comment.updated_at,
                ),
            )
        except IntegrityError as e:
            raise ResourceExistsException('The comment already exists.') from e
        else:
            comment.id = cursor.lastrowid
            return comment

    def get_by_id(self, comment_id: int) -> Comment:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        SELECT id, video_id, comment_id, comment_text, parent_id,
        like_count, published_at, updated_at FROM comments WHERE id=?
        """,
            ((comment_id,)),
        )
        row = cursor.fetchone()
        if row:
            return Comment(
                id=row[0],
                video_id=row[1],
                comment_id=row[2],
                comment_text=row[3],
                parent_id=row[4],
                like_count=row[5],
                published_at=row[6],
                updated_at=row[7],
            )
        else:
            raise ResourceNotExistException('The Comment was not found.')

    def update(self, comment: Comment) -> Comment:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        UPDATE comments SET video_id=?, comment_id=?, comment_text=?,
        parent_id=?, like_count=?, published_at=?, updated_at=? WHERE id=?
        """,
            (
                comment.video_id,
                comment.comment_id,
                comment.comment_text,
                comment.parent_id,
                comment.like_count,
                comment.published_at,
                comment.updated_at,
                comment.id,
            ),
        )
        return comment

    def delete(self, comment_id: int) -> None:
        cursor = self.connection.cursor()
        cursor.execute("""DELETE FROM comments WHERE id=?""", (comment_id,))

    def list_all(
        self,
        limit: Optional[int] = 2,
        sort_order: Optional[str] = 'ASC',
        sort_field: Optional[str] = 'id',
        offset: Optional[int] = 0,
    ) -> list[Comment]:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
        SELECT * FROM comments ORDER BY {sort_field} {sort_order} LIMIT {limit} OFFSET {offset}
        """
        )
        rows = cursor.fetchall()
        if rows:
            comments = [
                Comment(
                    id=row[0],
                    video_id=row[1],
                    comment_id=row[2],
                    comment_text=row[3],
                    parent_id=row[4],
                    like_count=row[5],
                    published_at=row[6],
                    updated_at=row[7],
                )
                for row in rows
            ]
            return comments
        return []

    def query(self, query_string: str) -> list[Comment]:
        cursor = self.connection.cursor()
        cursor.execute(query_string)
        rows = cursor.fetchall()
        if rows:
            return rows
        return []
