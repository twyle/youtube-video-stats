from .sqlite_request_handler import SQLiteRequestHandlerFactory
from ..repositories.sqlite_comment_repository import SQLiteCommentRepository
from ..repositories.base_repository import BaseRepository
from ..usecases.use_case import UseCase
from ..usecases.comment_usecases import (
    AddCommentUseCase, GetCommentUseCase, UpdateCommentUseCase, DeleteCommentUseCase, 
    GetCommentsUseCase, AddManyCommentsUseCase, QueryCommentUseCase
)
from ..models.comment_model import Comment

class CommentSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[Comment]:
        return SQLiteCommentRepository()    
    
    
class AddCommentSQLiteFactory(CommentSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return AddCommentUseCase()    
    

class GetCommentSQLiteFactory(CommentSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return GetCommentUseCase()
    
class UpdateCommentSQLiteFactory(CommentSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return UpdateCommentUseCase()
    
class DeleteCommentSQLiteFactory(CommentSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return DeleteCommentUseCase() 
    
class GetCommentsSQLiteFactory(CommentSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return GetCommentsUseCase() 
    
class AddManyCommentsSQLiteFactory(CommentSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return AddManyCommentsUseCase() 
    
class QueryCommentsSQLiteFactory(CommentSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return QueryCommentUseCase() 