import dataclasses
from typing import Any, Optional

from flask import jsonify

from ...exceptions.exceptions import ResourceExistsException
from ..models.playlist_model import Playlist
from ..repositories.unit_of_work import BaseUnitfWork
from .querie_mixin import QueryMixin
from .use_case import UseCase


class AddPlaylistUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            playlist = Playlist(
                playlist_id=data["playlist_id"],
                playlist_title=data["playlist_title"],
                playlist_description=data["playlist_description"],
                playlist_thumbnail=data["playlist_thumbnail"],
                videos_count=data["videos_count"],
                published_at=data["published_at"],
                channel_id=data["channel_id"],
            )
            uow.repository.add(playlist)
        return dataclasses.asdict(playlist)


class GetPlaylistUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            playlist_id = data["playlist_id"]
            playlist = uow.repository.get_by_id(playlist_id)
        return dataclasses.asdict(playlist)


class DeletePlaylistUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            playlist_id = data["playlist_id"]
            playlist = uow.repository.get_by_id(playlist_id)
            uow.repository.delete(playlist_id)
        return dataclasses.asdict(playlist)


class UpdatePlaylistUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            playlist_id = data["playlist_id"]
            playlist = uow.repository.get_by_id(playlist_id)
            if data.get("playlist_title"):
                playlist.playlist_title = data.get("playlist_title")
            if data.get("videos_count"):
                playlist.videos_count = data.get("videos_count")
            if data.get("playlist_description"):
                playlist.playlist_description = data.get("playlist_description")
            if data.get("playlist_id"):
                playlist.playlist_id = data.get("playlist_id")
            if data.get("playlist_thumbnail"):
                playlist.playlist_thumbnail = data.get("playlist_thumbnail")
            if data.get("published_at"):
                playlist.published_at = data.get("published_at")
            uow.repository.update(playlist)
        return dataclasses.asdict(playlist)


class GetPlaylistsUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            sort_field = "id"
            limit = 10
            offset = 0
            sort_order = "ASC"
            if data.get("sort_field"):
                sort_field = data.get("sort_field")
            if data.get("limit"):
                limit = data.get("limit")
            if data.get("offset"):
                offset = data.get("offset")
            if data.get("sort_order"):
                sort_order = data.get("sort_order")
            playlists = uow.repository.list_all(
                sort_field=sort_field, limit=limit, offset=offset, sort_order=sort_order
            )
        return jsonify(playlists)


class AddManyPlaylistsUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            playlist_data_list: list[dict[str, str | int]] = data["playlists"]
            playlists_added: int = 0
            for data in playlist_data_list:
                playlist = Playlist(
                    playlist_id=data["playlist_id"],
                    playlist_title=data["playlist_title"],
                    playlist_description=data["playlist_description"],
                    playlist_thumbnail=data["playlist_thumbnail"],
                    videos_count=data["videos_count"],
                    published_at=data["published_at"],
                    channel_id=data["channel_id"],
                )
                try:
                    uow.repository.add(playlist)
                    playlists_added += 1
                except ResourceExistsException:
                    pass
        return {"playlists Added": playlists_added}


# flake8: noqa: W291
class QueryPlaylistUseCase(QueryMixin, UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            playlists = []
            query_data = {
                "query": {"channel_id": {"eq": data["channel_id"]}},
                "fields": ["id", "playlist_id", "playlist_title", "channel_id"],
            }
            print(query_data)
            # playlist_data_list = uow.repository.query(self.generate_query(query_data))
            q = f"""
            SELECT id, playlist_id, playlist_title, channel_id FROM playlists WHERE channel_id =
            '{data['channel_id']}' ORDER BY id ASC LIMIT 10 OFFSET 0
            """
            playlist_data_list = uow.repository.query(q)
            if playlist_data_list:
                for playlist_data in playlist_data_list:
                    d = {}
                    for i, item in enumerate(playlist_data):
                        d[query_data["fields"][i]] = item
                    playlists.append(d)
        return jsonify(playlists)
