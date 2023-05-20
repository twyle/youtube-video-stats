from typing import Any
from ..repositories.sqlite_repository import SQLiteUserRepository
from ..repositories.user_unit_of_work import UserUnitOfWork
from ..usecases.create_user import CreateUserUseCase, GetUserUseCase, UpdateUserUseCase
from ..models.user_model import User
from ..connections import create_sqlite_database_connection
from abc import ABC, abstractmethod
from ..repositories.base_repository import BaseRepository
from ..usecases.create_user import UseCase

class RequestHandler(ABC):
    @abstractmethod       
    def __call__(self, connection, data: dict[str, Any]) -> Any:
        pass
    
class CreateUserRequestHandler(RequestHandler):
    def __init__(self, connection, repository: BaseRepository[User],
                 unit_of_work: UserUnitOfWork, use_case: UseCase) -> None:
        self.__connection = connection
        self.__repository = repository
        self.__unit_of_work = unit_of_work
        self.__use_case = use_case
        
    def __call__(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.__connection() as conn:
            self.__repository.connection = conn
            self.__unit_of_work.connection = conn
            self.__unit_of_work.users = self.__repository
            self.__use_case.unit_of_work = self.__unit_of_work
            user = self.__use_case.execute(data)
        return user
        
def create_user():        
    with create_sqlite_database_connection() as conn:
        repository = SQLiteUserRepository(conn)
        unit_of_work = UserUnitOfWork(conn, repository)
        new_user = User(
            first_name='lyle',
            last_name='okoth',
            email_address='lyle@gmail.com',
            password='password'
        )
        user =  CreateUserUseCase(unit_of_work).execute(new_user)
    return user
    
def get_user():        
    with create_sqlite_database_connection() as conn:
        repository = SQLiteUserRepository(conn)
        unit_of_work = UserUnitOfWork(conn, repository)
        user =  GetUserUseCase(unit_of_work).execute(1)
    print(user)
    
def update_user():        
    with create_sqlite_database_connection() as conn:
        repository = SQLiteUserRepository(conn)
        unit_of_work = UserUnitOfWork(conn, repository)
        new_user = User(
            first_name='lyle2',
            last_name='okoth',
            email_address='lyle@gmail.com',
            password='password',
            id=1
        )
        user =  UpdateUserUseCase(unit_of_work).execute(new_user)
    print(user)