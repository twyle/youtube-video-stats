from typing import Any
from .base_repository import BaseRepository
from ..models.user_model import User

class UserUnitOfWork:
    def __init__(self, connection: Any, user_repository: BaseRepository[User]) -> None:
        self.connection = connection
        self.users = user_repository
        
    def __enter__(self):
        return self
    
    def __exit__(self, exec_type, exec_val, exec_tb):
        if exec_type:
            self.rollback()
        else:
            self.commit()
            
    def commit(self):
        self.connection.commit()
        
    def rollback(self):
        self.connection.rollback()