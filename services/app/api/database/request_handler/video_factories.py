from .sqlite_request_handler import SQLiteRequestHandlerFactory
from ..repositories.sqlite_video_repository import SQLiteVideoRepository
from ..repositories.base_repository import BaseRepository
from ..usecases.use_case import UseCase
from ..usecases.video_usecases import (
    AddVideoUseCase, GetVideoUseCase, UpdateVideoUseCase, DeleteVideoUseCase
)
from ..models.video_model import Video

class VideoSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[Video]:
        return SQLiteVideoRepository()    
    
    
class AddVideoSQLiteFactory(VideoSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return AddVideoUseCase()    
    

class GetVideoSQLiteFactory(VideoSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return GetVideoUseCase()
    
class UpdateVideoSQLiteFactory(VideoSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return UpdateVideoUseCase()
    
class DeleteVideoSQLiteFactory(VideoSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return DeleteVideoUseCase() 