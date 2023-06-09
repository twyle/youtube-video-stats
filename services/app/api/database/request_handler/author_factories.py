from ..models.author_model import CommentAuthor
from ..repositories.base_repository import BaseRepository
from ..repositories.sqlite_author_repository import SQLiteCommentAuthorRepository
from ..usecases.author_use_cases import (
    CreateCommentAuthorUseCase,
    DeleteCommentAuthorUseCase,
    GetAllCommentAuthorsUseCase,
    GetCommentAuthorUseCase,
    UpdateCommentAuthorUseCase,
)
from ..usecases.use_case import UseCase
from .sqlite_request_handler import SQLiteRequestHandlerFactory


class AddCommentAuthorSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[CommentAuthor]:
        return SQLiteCommentAuthorRepository()

    def get_use_case(self) -> UseCase:
        return CreateCommentAuthorUseCase()


class GetCommentAuthorSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[CommentAuthor]:
        return SQLiteCommentAuthorRepository()

    def get_use_case(self) -> UseCase:
        return GetCommentAuthorUseCase()


class UpdateCommentAuthorSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[CommentAuthor]:
        return SQLiteCommentAuthorRepository()

    def get_use_case(self) -> UseCase:
        return UpdateCommentAuthorUseCase()


class DeleteCommentAuthorSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[CommentAuthor]:
        return SQLiteCommentAuthorRepository()

    def get_use_case(self) -> UseCase:
        return DeleteCommentAuthorUseCase()


class ListCommentAuthorsSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[CommentAuthor]:
        return SQLiteCommentAuthorRepository()

    def get_use_case(self) -> UseCase:
        return GetAllCommentAuthorsUseCase()
