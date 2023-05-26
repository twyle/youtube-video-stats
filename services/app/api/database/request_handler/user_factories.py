from .sqlite_request_handler import SQLiteRequestHandlerFactory
from ..repositories.sqlite_repository import SQLiteUserRepository
from ..repositories.base_repository import BaseRepository
from ..usecases.use_case import UseCase
from ..usecases.user_use_cases import (
    CreateUserUseCase, GetAllUsersUseCase, DeleteUserUseCase, ActivateUserUseCase,
    LoginUserUseCase, CreateAdminUseCase, GetUserUseCase, UpdateUserUseCase
)
from ..models.user_model import User

class AddUserSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[User]:
        return SQLiteUserRepository()
    
    def get_use_case(self) -> UseCase:
        return CreateUserUseCase()
    
class GetUserSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[User]:
        return SQLiteUserRepository()
    
    def get_use_case(self) -> UseCase:
        return GetUserUseCase()
    
class UpdateUserSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[User]:
        return SQLiteUserRepository()
    
    def get_use_case(self) -> UseCase:
        return UpdateUserUseCase()
    
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
    
class ActivateAccountSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[User]:
        return SQLiteUserRepository()
    
    def get_use_case(self) -> UseCase:
        return ActivateUserUseCase()
    
class LoginUserSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[User]:
        return SQLiteUserRepository()
    
    def get_use_case(self) -> UseCase:
        return LoginUserUseCase()
    
class AddAdminSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[User]:
        return SQLiteUserRepository()
    
    def get_use_case(self) -> UseCase:
        return CreateAdminUseCase()