from ..models.user_model import User
from ..repositories.base_repository import BaseRepository
from ..repositories.sqlite_repository import SQLiteUserRepository
from ..usecases.admin_use_cases import CreateAdminUseCase, LoginAdminUseCase
from ..usecases.use_case import UseCase
from ..usecases.user_use_cases import (
    ActivateUserUseCase,
    CreateUserUseCase,
    DeleteUserUseCase,
    GetAllUsersUseCase,
    GetUserUseCase,
    LoginUserUseCase,
    UpdateUserUseCase,
)
from .sqlite_request_handler import SQLiteRequestHandlerFactory


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


class LoginAdminSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[User]:
        return SQLiteUserRepository()

    def get_use_case(self) -> UseCase:
        return LoginAdminUseCase()
