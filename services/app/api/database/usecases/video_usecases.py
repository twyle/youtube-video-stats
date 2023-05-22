from ..repositories.unit_of_work import BaseUnitfWork
from ..models.user_model import User
from typing import Optional, Any
import dataclasses
from .use_case import UseCase
from flask import jsonify
from ..models.video_model import Video
from .queries import QueryMixin

class AddVideoUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            video = Video(
                video_id=data['video_id'],
                video_title=data['video_title'],
                channel_title=data['channel_title'],
                video_description=data['video_description'],
                video_thumbnail=data['video_thumbnail'],
                video_duration=data['video_duration'],
                views_count=data['views_count'],
                likes_count=data['likes_count'],
                comments_count=data['comments_count']
            )
            uow.repository.add(video)
        return dataclasses.asdict(video)
    

class GetVideoUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            video_id = data['video_id']
            video = uow.repository.get_by_id(video_id)
        return dataclasses.asdict(video)
    
class DeleteVideoUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            video_id = data['video_id']
            video = uow.repository.get_by_id(video_id)
            uow.repository.delete(video_id)
        return dataclasses.asdict(video)
    

class UpdateVideoUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            id = int(data['id'])
            video = uow.repository.get_by_id(id)
            if data.get('channel_title'):
                video.channel_title = data.get('channel_title')
            if data.get('comments_count'):
                video.comments_count = data.get('comments_count')
            if data.get('likes_count'):
                video.likes_count = data.get('likes_count')
            if data.get('video_description'):
                video.video_description = data.get('video_description')
            if data.get('video_duration'):
                video.video_duration = data.get('video_duration')
            if data.get('video_id'):
                video.video_id = data.get('video_id')
            if data.get('video_thumbnail'):
                video.video_thumbnail = data.get('video_thumbnail')
            if data.get('video_title'):
                video.video_title = data.get('video_title')
            if data.get('views_count'):
                video.views_count = data.get('views_count')
            uow.repository.update(video)
        return dataclasses.asdict(video)
    
    
class GetVideosUseCase(UseCase):
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
            videos = uow.repository.list_all(sort_field=sort_field, limit=limit, offset=offset,
                                             sort_order=sort_order)
        return jsonify(videos)
    
    
class AddManyVideoUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            video_data_list = data['videos']
            for video_data in video_data_list:
                video = Video(
                    video_id=video_data['video_id'],
                    video_title=video_data['video_title'],
                    channel_title=video_data['channel_title'],
                    video_description=video_data['video_description'],
                    video_thumbnail=video_data['video_thumbnail'],
                    video_duration=video_data['video_duration'],
                    views_count=video_data['views_count'],
                    likes_count=video_data['likes_count'],
                    comments_count=video_data['comments_count']
                )
                uow.repository.add(video)
        return {'Videos Added': f'{len(video_data_list)}'}
    
    
class QueryVideoUseCase(QueryMixin, UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            print(data)
            self.print_yay()
        # return dataclasses.asdict(video)
        return {'Success': 'Queried database.'}