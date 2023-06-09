from ..models.video_model import Video
from ..repositories.base_repository import BaseRepository
from ..repositories.sqlite_video_repository import SQLiteVideoRepository
from ..usecases.use_case import UseCase
from ..usecases.video_usecases import (
    AddManyVideoUseCase,
    AddVideoUseCase,
    DeleteVideoUseCase,
    GetVideosUseCase,
    GetVideoUseCase,
    QueryVideoUseCase,
    UpdateVideoUseCase,
)
from .sqlite_request_handler import SQLiteRequestHandlerFactory


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


class GetVideosSQLiteFactory(VideoSQLiteFactory):
    def get_use_case(self) -> UseCase:
        return GetVideosUseCase()


class AddManyVideosSQLiteFactory(VideoSQLiteFactory):
    def get_use_case(self) -> UseCase:
        return AddManyVideoUseCase()


class QueryVideosSQLiteFactory(VideoSQLiteFactory):
    def get_use_case(self) -> UseCase:
        return QueryVideoUseCase()
