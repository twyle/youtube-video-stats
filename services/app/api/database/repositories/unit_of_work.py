from abc import ABC, abstractmethod
from typing import Any, Optional

from ..models.user_model import User
from .base_repository import BaseRepository


class BaseUnitfWork(ABC):
    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exec_type, exec_val, exec_tb):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass


class UnitOfWork(BaseUnitfWork):
    def __init__(
        self,
        connection: Optional[Any] = None,
        repository: Optional[BaseRepository[User]] = None,
    ) -> None:
        self.__connection = connection
        self.__repositrory = repository

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, connection):
        self.__connection = connection

    @property
    def repository(self):
        return self.__repositrory

    @repository.setter
    def repository(self, repository: BaseRepository[User]):
        self.__repositrory = repository

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
