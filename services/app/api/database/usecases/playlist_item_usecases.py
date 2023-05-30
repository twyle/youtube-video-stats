from ..repositories.unit_of_work import BaseUnitfWork
from typing import Optional, Any
import dataclasses
from .use_case import UseCase
from flask import jsonify
from ..models.playlist_item_model import PlaylistItemModel
from .querie_mixin import QueryMixin
from ...exceptions.exceptions import ResourceExistsException

class AddPlaylistItemUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            # add channel
            # add playlist
            # add video
            playlist_item = PlaylistItemModel(
                playlist_item_id=data['playlist_item_id'],
                channel_adder_id=data['channel_adder_id'],
                video_owner_channel_id=data['video_owner_channel_id'],
                playlist_id=data['playlist_id'],
                video_id=data['video_id'],
                position=data['position'],
                privacy_status=data['privacy_status'],
                date_added=data['date_added']
            )
            uow.repository.add(playlist_item)
        return dataclasses.asdict(playlist_item)
    

class GetPlaylistItemUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            playlist_item_id = data['playlist_item_id']
            playlist_item = uow.repository.get_by_id(playlist_item_id)
        return dataclasses.asdict(playlist_item)
    
class DeletePlaylistItemUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            playlist_item_id = data['playlist_item_id']
            playlist_item = uow.repository.get_by_id(playlist_item_id)
            uow.repository.delete(playlist_item_id)
        return dataclasses.asdict(playlist_item)
    

class UpdatePlaylistItemUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            playlist_item_id = data['playlist_item_id']
            playlist_item = uow.repository.get_by_id(playlist_item_id)
            if data.get('position'):
                playlist_item.position = data.get('position')
            if data.get('privacy_status'):
                playlist_item.privacy_status = data.get('privacy_status')
            if data.get('date_added'):
                playlist_item.date_added = data.get('date_added')
            uow.repository.update(playlist_item)
        return dataclasses.asdict(playlist_item)
    
    
class GetPlaylistItemsUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            sort_field = 'id'
            limit = 10
            offset = 0
            sort_order = 'ASC'
            if data.get('sort_field'):
                sort_field = data.get('sort_field')
            if data.get('limit'):
                limit = data.get('limit')
            if data.get('offset'):
                offset = data.get('offset')
            if data.get('sort_order'):
                sort_order = data.get('sort_order')
            playlist_items = uow.repository.list_all(sort_field=sort_field, limit=limit, offset=offset,
                                             sort_order=sort_order)
        return jsonify(playlist_items)
    
    
class AddManyPlaylistItemsUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            playlist_item_data_list: list[dict[str, str|int]] = data['playlist_items']
            playlist_items_added: int = 0
            for data in playlist_item_data_list:
                playlist_item = PlaylistItemModel(
                    playlist_item_id=data['playlist_item_id'],
                    channel_adder_id=data['channel_adder_id'],
                    video_owner_channel_id=data['video_owner_channel_id'],
                    playlist_id=data['playlist_id'],
                    video_id=data['video_id'],
                    position=data['position'],
                    privacy_status=data['privacy_status'],
                    date_added=data['date_added']
                )
                try:
                    uow.repository.add(playlist_item)
                    playlist_items_added += 1
                except ResourceExistsException:
                    pass
        return {'playlist items Added': playlist_items_added}
    
    
class QueryPlaylistItemUseCase(QueryMixin, UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            playlist_items = []
            query_data = {
                'query': {
                    'channel_id': {
                        'eq': data['channel_id']
                    }
                },
                'fields': ['id', 'playlist_id', 'playlist_title','channel_id']
            }
            print(query_data)
            # playlist_data_list = uow.repository.query(self.generate_query(query_data))
            q = f"""
            SELECT id, playlist_id, playlist_title, channel_id FROM playlists WHERE channel_id = '{data['channel_id']}' ORDER BY id ASC LIMIT 10 OFFSET 0
            """
            playlist_data_list = uow.repository.query(q)
            if playlist_data_list:
                for playlist_data in playlist_data_list:
                    d = {}
                    for i, item in enumerate(playlist_data):
                        d[query_data['fields'][i]] = item
                    playlists.append(d)
        return jsonify(playlists)