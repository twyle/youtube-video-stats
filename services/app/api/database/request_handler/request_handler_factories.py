from typing import Any
from ..repositories.base_repository import BaseRepository
from ..repositories.unit_of_work import BaseUnitfWork
from ..usecases.use_case import UseCase
from ..connections import create_sqlite_database_connection
from ..models.user_model import User
from ..repositories.sqlite_repository import SQLiteUserRepository
from ..repositories.unit_of_work import UnitOfWork
from ..usecases.user_use_cases import CreateUserUseCase

class CreateUserSQLiteFactory:
    def get_database_connection(self) -> Any:
        return create_sqlite_database_connection
        
    def get_repository(self) -> BaseRepository[User]:
        return SQLiteUserRepository()
        
    def get_unit_of_work(self) -> BaseUnitfWork:
        return UnitOfWork()
    
    def get_use_case(self) -> UseCase:
        return CreateUserUseCase()