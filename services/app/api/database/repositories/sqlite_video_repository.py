from sqlite3 import IntegrityError
from typing import Any, Optional

from ...exceptions.exceptions import ResourceExistsException, ResourceNotExistException
from ..models.video_model import Video
from .base_repository import BaseRepository


# flake8: noqa: W291
class SQLiteVideoRepository(BaseRepository[Video]):
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
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            video_id TEXT NOT NULL UNIQUE,
            video_title TEXT NOT NULL,
            channel_title TEXT NOT NULL UNIQUE,
            video_description TEXT,
            video_thumbnail TEXT,
            video_duration TEXT,
            views_count INTEGER ,
            likes_count INTEGER,
            comments_count INTEGER,
            published_at TEXT
        )
        """
        )
        self.connection.commit()

    def add(self, video: Video) -> Video:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                """
            INSERT INTO videos (video_id, video_title, channel_title, video_description,
            video_thumbnail, video_duration, views_count, likes_count, comments_count, published_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    video.video_id,
                    video.video_title,
                    video.channel_title,
                    video.video_description,
                    video.video_thumbnail,
                    video.video_duration,
                    video.views_count,
                    video.likes_count,
                    video.comments_count,
                    video.published_at,
                ),
            )
        except IntegrityError as e:
            raise ResourceExistsException('The video already exists.') from e
        else:
            video.id = cursor.lastrowid
            return video

    def get_by_id(self, video_id: int) -> Video:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        SELECT id, video_id, video_title, channel_title, video_description, video_thumbnail, video_duration,
            views_count, likes_count, comments_count, published_at FROM videos WHERE id=?
        """,
            ((video_id,)),
        )
        row = cursor.fetchone()
        if row:
            return Video(
                id=row[0],
                video_id=row[1],
                video_title=row[2],
                channel_title=row[3],
                video_description=row[4],
                video_thumbnail=row[5],
                video_duration=row[6],
                views_count=row[7],
                likes_count=row[8],
                comments_count=row[9],
                published_at=row[10],
            )
        else:
            raise ResourceNotExistException('The video was not found.')

    def update(self, video: Video) -> Video:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        UPDATE videos SET video_id=?, video_title=?, channel_title=?, video_description=?,
        video_thumbnail=?, video_duration=?, views_count=?, likes_count=?, comments_count=?,
        published_at=? WHERE id=?
        """,
            (
                video.video_id,
                video.video_title,
                video.channel_title,
                video.video_description,
                video.video_thumbnail,
                video.video_duration,
                video.views_count,
                video.likes_count,
                video.comments_count,
                video.published_at,
                video.id,
            ),
        )
        return video

    def delete(self, video_id: int) -> None:
        cursor = self.connection.cursor()
        cursor.execute("""DELETE FROM videos WHERE id=?""", (video_id,))

    def list_all(
        self,
        limit: Optional[int] = 2,
        sort_order: Optional[str] = 'ASC',
        sort_field: Optional[str] = 'id',
        offset: Optional[int] = 0,
    ) -> list[Video]:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
        SELECT * FROM videos ORDER BY {sort_field} {sort_order} LIMIT {limit} OFFSET {offset}
        """
        )
        rows = cursor.fetchall()
        if rows:
            videos = [
                Video(
                    id=row[0],
                    video_id=row[1],
                    video_title=row[2],
                    channel_title=row[3],
                    video_description=row[4],
                    video_thumbnail=row[5],
                    video_duration=row[6],
                    views_count=row[7],
                    likes_count=row[8],
                    comments_count=row[9],
                    published_at=row[10],
                )
                for row in rows
            ]
            return videos
        return []

    def query(self, query_string: str) -> list[Video]:
        cursor = self.connection.cursor()
        cursor.execute(query_string)
        rows = cursor.fetchall()
        if rows:
            return rows
        return []
