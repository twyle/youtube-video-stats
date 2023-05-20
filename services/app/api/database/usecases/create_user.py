from ..repositories.user_unit_of_work import UserUnitOfWork
from ..models.user_model import User
from abc import ABC, abstractmethod
from typing import Optional

class UseCase(ABC):
    @abstractmethod
    def execute(self, item: User | int) -> User | int:
        pass

class CreateUserUseCase:
    def __init__(self, unit_of_work: Optional[UserUnitOfWork] = None) -> None:
        self.__unit_of_work = unit_of_work
        
    @property
    def unit_of_work(self) -> UserUnitOfWork:
        return self.__unit_of_work
    
    @unit_of_work.setter
    def unit_of_work(self, unit_of_work: UserUnitOfWork) -> None:
        self.__unit_of_work = unit_of_work
        
    def execute(self, data: dict) -> User:
        with self.unit_of_work as uow:
            user = User(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email_address=data['email_address'],
                password=data['password']
            )
            uow.users.add(user)
        return user
    
class GetUserUseCase:
    def __init__(self, unit_of_work: UserUnitOfWork) -> None:
        self.unit_of_work = unit_of_work
        
    def execute(self, user_id: int) -> User:
        with self.unit_of_work as uow:
            user = uow.users.get_by_id(user_id)
        return user
    

class UpdateUserUseCase:
    def __init__(self, unit_of_work: UserUnitOfWork) -> None:
        self.unit_of_work = unit_of_work
        
    def execute(self, user: User) -> User:
        with self.unit_of_work as uow:
            user = uow.users.update(user)
        return user
    
#create_user, delete_user, find_user, update_user
#UseCaseBuilder(connection, repository, usecase(item))