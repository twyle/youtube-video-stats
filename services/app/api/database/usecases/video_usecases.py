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
    

class GetUserUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            user_id = data['user_id']
            user = uow.repository.get_by_id(user_id)
        return dataclasses.asdict(user)
    
class DeleteUserUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            user_id = data['user_id']
            user = uow.repository.delete(user_id)
        return dataclasses.asdict(user)
    

class UpdateUserUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            user_id = data['user_id']
            user = uow.repository.delete(user_id)
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            if data.get('last_name'):
                user.last_name = data.get('last_name')
            if data.get('email_address'):
                user.email_address = data.get('email_address')
            if data.get('password'):
                user.password = data.get('password')
            uow.repository.update(user)
        return dataclasses.asdict(user)
    
    
class GetAllUsersUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            users = uow.repository.list_all()
        return jsonify(users)