from .sqlite_request_handler import SQLiteRequestHandlerFactory
from ..repositories.sqlite_video_repository import SQLiteVideoRepository
from ..repositories.base_repository import BaseRepository
from ..usecases.use_case import UseCase
from ..usecases.video_usecases import AddVideoUseCase
from ..models.video_model import Video

class AddVideoSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[Video]:
        return SQLiteVideoRepository()
    
    def get_use_case(self) -> UseCase:
        return AddVideoUseCase()