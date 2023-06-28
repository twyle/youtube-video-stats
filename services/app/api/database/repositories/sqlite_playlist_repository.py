from sqlite3 import IntegrityError
from typing import Any, Optional

from ...exceptions.exceptions import ResourceExistsException, ResourceNotExistException
from ..models.playlist_model import Playlist
from .base_repository import BaseRepository


# flake8: noqa: W291
class SQLitePlaylistRepository(BaseRepository[Playlist]):
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
        CREATE TABLE IF NOT EXISTS playlists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            playlist_id TEXT NOT NULL UNIQUE,
            channel_id TEXT NOT NULL,
            playlist_title TEXT NOT NULL,
            playlist_description TEXT,
            playlist_thumbnail TEXT,
            videos_count INTEGER,
            published_at TEXT,
            FOREIGN KEY (channel_id) REFERENCES channels (channel_id)
            ON UPDATE cascade
            ON DELETE cascade
        )
        """
        )
        self.connection.commit()

    def add(self, playlist: Playlist) -> Playlist:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                """
            INSERT INTO playlists (playlist_id, playlist_title, playlist_description,
            playlist_thumbnail, videos_count, published_at, channel_id)
            VALUES (?, ?, ?, ?, ?, ?,?)
            """,
                (
                    playlist.playlist_id,
                    playlist.playlist_title,
                    playlist.playlist_description,
                    playlist.playlist_thumbnail,
                    playlist.videos_count,
                    playlist.published_at,
                    playlist.channel_id,
                ),
            )
        except IntegrityError as e:
            print(e)
            raise ResourceExistsException("The Playlist already exists.") from e
        else:
            playlist.id = cursor.lastrowid
            return playlist

    def get_by_id(self, playlist_id: int) -> Playlist:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        SELECT id, playlist_id, playlist_title, playlist_description, playlist_thumbnail,
        videos_count, published_at, channel_id FROM playlists WHERE id=?
        """,
            ((playlist_id,)),
        )
        row = cursor.fetchone()
        if row:
            return Playlist(
                id=row[0],
                playlist_id=row[1],
                playlist_title=row[2],
                playlist_description=row[3],
                playlist_thumbnail=row[4],
                videos_count=row[5],
                published_at=row[6],
                channel_id=row[7],
            )
        else:
            raise ResourceNotExistException("The playlist was not found.")

    def update(self, playlist: Playlist) -> Playlist:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        UPDATE playlists SET playlist_id=?, playlist_title=?, playlist_description=?,
        playlist_thumbnail=?, videos_count=?, published_at=?, channel_id=? WHERE id=?
        """,
            (
                playlist.playlist_id,
                playlist.playlist_title,
                playlist.playlist_description,
                playlist.playlist_thumbnail,
                playlist.videos_count,
                playlist.published_at,
                playlist.channel_id,
                playlist.id,
            ),
        )
        return playlist

    def delete(self, playlist_id: int) -> None:
        cursor = self.connection.cursor()
        cursor.execute("""DELETE FROM playlists WHERE id=?""", (playlist_id,))

    def list_all(
        self,
        limit: Optional[int] = 2,
        sort_order: Optional[str] = "ASC",
        sort_field: Optional[str] = "id",
        offset: Optional[int] = 0,
    ) -> list[Playlist]:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
         SELECT id, playlist_id, playlist_title, playlist_description, playlist_thumbnail,
        videos_count, published_at, channel_id FROM playlists ORDER BY
        {sort_field} {sort_order} LIMIT {limit} OFFSET {offset}
        """
        )
        rows = cursor.fetchall()
        if rows:
            playlists = [
                Playlist(
                    id=row[0],
                    playlist_id=row[1],
                    playlist_title=row[2],
                    playlist_description=row[3],
                    playlist_thumbnail=row[4],
                    videos_count=row[5],
                    published_at=row[6],
                    channel_id=row[7],
                )
                for row in rows
            ]
            return playlists
        return []

    def query(self, query_string: str) -> list[Playlist]:
        cursor = self.connection.cursor()
        cursor.execute(query_string)
        rows = cursor.fetchall()
        if rows:
            return rows
        return []
