from typing import Any, Optional
from .base_repository import BaseRepository
from ..models.user_model import User

class UserUnitOfWork:
    def __init__(self, connection: Optional[Any] = None, 
                 user_repository: Optional[BaseRepository[User]] = None) -> None:
        self.__connection = connection
        self.__users = user_repository
        
    @property
    def connection(self):
        return self.__connection
    
    @connection.setter
    def connection(self, connection):
        self.__connection = connection
        
    @property
    def users(self):
        return self.__users
    
    @users.setter
    def users(self, users):
        self.__users = users
        
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