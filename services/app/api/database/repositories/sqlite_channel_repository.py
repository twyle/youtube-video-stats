from .base_repository import BaseRepository
from typing import Any, Optional
from ..models.channel_model import Channel
from sqlite3 import IntegrityError
from ...exceptions.exceptions import (
    ResourceExistsException, ResourceNotExistException
)

class SQLiteChannelRepository(BaseRepository[Channel]):
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
        CREATE TABLE IF NOT EXISTS channels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            channel_id TEXT NOT NULL UNIQUE,
            channel_title TEXT NOT NULL UNIQUE,
            channel_description TEXT,
            channel_thumbnail TEXT,
            custom_url TEXT,
            views_count INTEGER ,
            videos_count INTEGER,
            subscribers_count INTEGER,
            published_at TEXT
        )
        """
        )
        self.connection.commit()
        
    def add(self, channel: Channel) -> Channel:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
            """
            INSERT INTO channels (channel_id, channel_title, channel_description, channel_thumbnail, 
            custom_url, views_count, videos_count, subscribers_count, published_at) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (channel.channel_id, channel.channel_title, channel.channel_description, 
             channel.channel_thumbnail, channel.custom_url, channel.views_count, 
             channel.videos_count, channel.subscribers_count, channel.published_at)
            )
        except IntegrityError as e:
            raise ResourceExistsException('The Channel already exists.') from e
        else:
            channel.id = cursor.lastrowid
            return channel
        
    def get_by_id(self, channel_id: int) -> Channel:
        cursor = self.connection.cursor()
        cursor.execute(
        """
        SELECT id, channel_id, channel_title, channel_description, channel_thumbnail, 
        custom_url, views_count, videos_count, subscribers_count, published_at FROM channels 
        WHERE id=?
        """,
        ((channel_id,))
        )
        row = cursor.fetchone()
        if row:
            return Channel(
                id=row[0],
                channel_id=row[1],
                channel_title=row[2],
                channel_description=row[3],
                channel_thumbnail=row[4],
                custom_url=row[5],
                views_count=row[6],
                videos_count=row[7],
                subscribers_count=row[8],
                published_at=row[9]
            )
        else:
            raise ResourceNotExistException('The Channel was not found.')
    
    def update(self, channel: Channel) -> Channel:
        cursor = self.connection.cursor()
        cursor.execute(
        """
        UPDATE channels SET channel_id=?, channel_title=?, channel_description=?, 
        channel_thumbnail=?, custom_url=?, views_count=?, videos_count=?, subscribers_count=?,
        published_at=? WHERE id=?
        """,
        (channel.channel_id, channel.channel_title, channel.channel_description, 
         channel.channel_thumbnail, channel.custom_url, channel.views_count, channel.videos_count, 
         channel.subscribers_count, channel.published_at, channel.id)
        )
        return channel
    
    def delete(self, channel_id: int) -> None:
        cursor = self.connection.cursor()
        cursor.execute(
            """DELETE FROM channels WHERE id=?""",
            (channel_id,)
        )
    
        
    def list_all(self, limit: Optional[int] = 2, sort_order: Optional[str] = 'ASC', 
                 sort_field: Optional[str] = 'id', offset: Optional[int] = 0) -> list[Channel]:
        cursor = self.connection.cursor()
        cursor.execute(
        f"""
        SELECT * FROM channels ORDER BY {sort_field} {sort_order} LIMIT {limit} OFFSET {offset}
        """
        )
        rows = cursor.fetchall()
        if rows:
            Channels = [
                Channel(
                    id=row[0],
                    channel_id=row[1],
                    channel_title=row[2],
                    channel_description=row[3],
                    channel_thumbnail=row[4],
                    custom_url=row[5],
                    views_count=row[6],
                    videos_count=row[7],
                    subscribers_count=row[8],
                    published_at=row[9]
            )
                for row in rows
            ]
            return Channels 
        return []
    
    def query(self, query_string: str) -> list[Channel]:
        cursor = self.connection.cursor()
        cursor.execute(query_string)
        rows = cursor.fetchall()
        if rows:
            return rows
        return []