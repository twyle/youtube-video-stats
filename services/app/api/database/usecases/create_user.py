from ..repositories.user_unit_of_work import UserUnitOfWork
from ..models.user_model import User


class CreateUserUseCase:
    def __init__(self, unit_of_work: UserUnitOfWork) -> None:
        self.unit_of_work = unit_of_work
        
    def execute(self, user: User) -> User:
        with self.unit_of_work as uow:
            uow.users.add(user)
        return user