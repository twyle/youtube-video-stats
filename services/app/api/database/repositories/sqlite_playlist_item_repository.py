from sqlite3 import IntegrityError
from typing import Any, Optional

from ...exceptions.exceptions import ResourceExistsException, ResourceNotExistException
from ..models.playlist_item_model import PlaylistItemModel
from .base_repository import BaseRepository


# flake8: noqa: W291
class SQLitePlaylistItemRepository(BaseRepository[PlaylistItemModel]):
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
        CREATE TABLE IF NOT EXISTS playlist_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            playlist_item_id TEXT NOT NULL UNIQUE,
            playlist_id TEXT NOT NULL,
            channel_adder_id TEXT NOT NULL,
            video_owner_channel_id TEXT NOT NULL,
            video_id TEXT NOT NULL,
            privacy_status TEXT,
            position INTEGER,
            date_added TEXT,
            FOREIGN KEY (playlist_id) REFERENCES playlists (playlist_id)
            ON UPDATE cascade
            ON DELETE cascade,
            FOREIGN KEY (video_owner_channel_id) REFERENCES channels (video_owner_channel_id)
            ON UPDATE cascade
            ON DELETE cascade,
            FOREIGN KEY (channel_adder_id) REFERENCES channels (channel_adder_id)
            ON UPDATE cascade
            ON DELETE cascade,
            FOREIGN KEY (video_id) REFERENCES videos (video_id)
            ON UPDATE cascade
            ON DELETE cascade
        )
        """
        )
        self.connection.commit()

    def add(self, playlist_item: PlaylistItemModel) -> PlaylistItemModel:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                """
            INSERT INTO playlist_items (playlist_item_id, channel_adder_id, video_owner_channel_id,
            playlist_id, video_id, position, privacy_status, date_added)
            VALUES (?, ?, ?, ?, ?, ?,?, ?)
            """,
                (
                    playlist_item.playlist_item_id,
                    playlist_item.channel_adder_id,
                    playlist_item.video_owner_channel_id,
                    playlist_item.playlist_id,
                    playlist_item.video_id,
                    playlist_item.position,
                    playlist_item.privacy_status,
                    playlist_item.date_added,
                ),
            )
        except IntegrityError as e:
            print(e)
            raise ResourceExistsException("The Playlist already exists.") from e
        else:
            playlist_item.id = cursor.lastrowid
            return playlist_item

    def get_by_id(self, playlist_item_id: int) -> PlaylistItemModel:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        SELECT id, playlist_item_id, channel_adder_id, video_owner_channel_id, playlist_id,
        video_id, position, privacy_status, date_added FROM playlist_items WHERE id=?
        """,
            ((playlist_item_id,)),
        )
        row = cursor.fetchone()
        if row:
            return PlaylistItemModel(
                id=row[0],
                playlist_item_id=row[1],
                channel_adder_id=row[2],
                video_owner_channel_id=row[3],
                playlist_id=row[4],
                video_id=row[5],
                position=row[6],
                privacy_status=row[7],
                date_added=row[8],
            )
        else:
            raise ResourceNotExistException("The playlist was not found.")

    def update(self, playlist_item: PlaylistItemModel) -> PlaylistItemModel:
        cursor = self.connection.cursor()
        cursor.execute(
            """
        UPDATE playlist_item SET playlist_item_id=?, channel_adder_id=?, video_owner_channel_id=?,
        playlist_id=?, video_id=?, position=?, privacy_status=?, date_added=? WHERE id=?
        """,
            (
                playlist_item.playlist_item_id,
                playlist_item.channel_adder_id,
                playlist_item.video_owner_channel_id,
                playlist_item.playlist_id,
                playlist_item.video_id,
                playlist_item.position,
                playlist_item.privacy_status,
                playlist_item.date_added,
                playlist_item.id,
            ),
        )
        return playlist_item

    def delete(self, playlist_item_id: int) -> None:
        cursor = self.connection.cursor()
        cursor.execute("""DELETE FROM playlist_items WHERE id=?""", (playlist_item_id,))

    def list_all(
        self,
        limit: Optional[int] = 2,
        sort_order: Optional[str] = "ASC",
        sort_field: Optional[str] = "id",
        offset: Optional[int] = 0,
    ) -> list[PlaylistItemModel]:
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
         SELECT id, playlist_item_id, channel_adder_id, video_owner_channel_id, playlist_id,
        video_id, position, privacy_status, date_added FROM playlist_items ORDER BY
        {sort_field} {sort_order} LIMIT {limit} OFFSET {offset}
        """
        )
        rows = cursor.fetchall()
        if rows:
            playlist_items = [
                PlaylistItemModel(
                    id=row[0],
                    playlist_item_id=row[1],
                    channel_adder_id=row[2],
                    video_owner_channel_id=row[3],
                    playlist_id=row[4],
                    video_id=row[5],
                    position=row[6],
                    privacy_status=row[7],
                    date_added=row[8],
                )
                for row in rows
            ]
            return playlist_items
        return []

    def query(self, query_string: str) -> list[PlaylistItemModel]:
        cursor = self.connection.cursor()
        cursor.execute(query_string)
        rows = cursor.fetchall()
        if rows:
            return rows
        return []
