from ..repositories.unit_of_work import BaseUnitfWork
from typing import Optional, Any
import dataclasses
from .use_case import UseCase
from flask import jsonify
from ..models.channel_model import Channel
from .querie_mixin import QueryMixin
from ...exceptions.exceptions import ResourceExistsException

class AddChannelUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            channel = Channel(
                channel_id=data['channel_id'],
                channel_title=data['channel_title'],
                channel_description=data['channel_description'],
                channel_thumbnail=data['channel_thumbnail'],
                custom_url=data['custom_url'],
                views_count=data['views_count'],
                subscribers_count=data['subscribers_count'],
                videos_count=data['videos_count'],
                published_at=data['published_at']
            )
            uow.repository.add(channel)
        return dataclasses.asdict(channel)
    

class GetChannelUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            channel_id = data['channel_id']
            channel = uow.repository.get_by_id(channel_id)
        return dataclasses.asdict(channel)
    
class DeleteChannelUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            channel_id = data['channel_id']
            channel = uow.repository.get_by_id(channel_id)
            uow.repository.delete(channel_id)
        return dataclasses.asdict(channel)
    

class UpdateChannelUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            channel_id = data['channel_id']
            channel = uow.repository.get_by_id(channel_id)
            if data.get('channel_title'):
                channel.channel_title = data.get('channel_title')
            if data.get('subscribers_count'):
                channel.subscribers_count = data.get('subscribers_count')
            if data.get('videos_count'):
                channel.videos_count = data.get('videos_count')
            if data.get('channel_description'):
                channel.channel_description = data.get('channel_description')
            if data.get('custom_url'):
                channel.custom_url = data.get('custom_url')
            if data.get('channel_id'):
                channel.channel_id = data.get('channel_id')
            if data.get('channel_thumbnail'):
                channel.channel_thumbnail = data.get('channel_thumbnail')
            if data.get('views_count'):
                channel.views_count = data.get('views_count')
            if data.get('published_at'):
                channel.published_at = data.get('published_at')
            uow.repository.update(channel)
        return dataclasses.asdict(channel)
    
    
class GetChannelsUseCase(UseCase):
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
            channels = uow.repository.list_all(sort_field=sort_field, limit=limit, offset=offset,
                                             sort_order=sort_order)
        return jsonify(channels)
    
    
class AddManyChannelsUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            channel_data_list: list[dict[str, str|int]] = data['channels']
            channels_added: int = 0
            for data in channel_data_list:
                channel = Channel(
                    channel_id=data['channel_id'],
                    channel_title=data['channel_title'],
                    channel_description=data['channel_description'],
                    channel_thumbnail=data['channel_thumbnail'],
                    custom_url=data['custom_url'],
                    views_count=data['views_count'],
                    subscribers_count=data['subscribers_count'],
                    videos_count=data['videos_count'],
                    published_at=data['published_at']
                )
                try:
                    uow.repository.add(channel)
                    channels_added += 1
                except ResourceExistsException:
                    pass
        return {'Channels Added': channels_added}
    
    
class QueryChannelUseCase(QueryMixin, UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            channels = []
            query_data = {
                'query': {
                    'channel_id': {
                        'eq': data['channel_id']
                    }
                },
                'fields': ['playlist_title','channel_title']
            }
            print(query_data)
            q = f"""
            SELECT playlist_title, channel_title from playlists inner join channels on 
            channels.channel_id = playlists.channel_id where channels.channel_id = '{data['channel_id']}';
            """
            channel_data_list = uow.repository.query(q)
            if channel_data_list:
                for channel_data in channel_data_list:
                    d = {}
                    for i, item in enumerate(channel_data):
                        d[query_data['fields'][i]] = item
                    channels.append(d)
        return jsonify(channels) 