from ..repositories.unit_of_work import BaseUnitfWork
from ..models.user_model import User
from typing import Optional, Any
import dataclasses
from .use_case import UseCase
from flask import jsonify
from ..models.video_model import Video

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
            video = uow.repository.delete(video_id)
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
    
    
class GetAllUsersUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            users = uow.repository.list_all()
        return jsonify(users)