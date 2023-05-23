from .sqlite_request_handler import SQLiteRequestHandlerFactory
from ..repositories.sqlite_repository import SQLiteUserRepository
from ..repositories.base_repository import BaseRepository
from ..usecases.use_case import UseCase
from ..usecases.user_use_cases import (
    CreateUserUseCase, GetAllUsersUseCase, DeleteUserUseCase
)
from ..models.user_model import User

class AddUserSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[User]:
        return SQLiteUserRepository()
    
    def get_use_case(self) -> UseCase:
        return CreateUserUseCase()
    
class DeleteUserSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[User]:
        return SQLiteUserRepository()
    
    def get_use_case(self) -> UseCase:
        return DeleteUserUseCase()
    
class ListUsersSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[User]:
        return SQLiteUserRepository()
    
    def get_use_case(self) -> UseCase:
        return GetAllUsersUseCase()