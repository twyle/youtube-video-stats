from typing import Any, TypeVar
from ..repositories.base_repository import BaseRepository
from ..repositories.unit_of_work import BaseUnitfWork
from ..usecases.use_case import UseCase
from abc import ABC, abstractmethod

T = TypeVar('T')

class RequestHandlerFactory(ABC):
    @abstractmethod
    def get_database_connection(self) -> Any:
        pass
    
    @abstractmethod    
    def get_repository(self) -> BaseRepository[T]:
        pass
    
    @abstractmethod    
    def get_unit_of_work(self) -> BaseUnitfWork:
        pass
    
    @abstractmethod    
    def get_use_case(self) -> UseCase:
        pass