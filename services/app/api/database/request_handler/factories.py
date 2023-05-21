from typing import Protocol, Any, TypeVar
from ..repositories.base_repository import BaseRepository
from ..repositories.unit_of_work import BaseUnitfWork
from ..usecases.use_case import UseCase

T = TypeVar('T')

class RequestHandlerFactoryProtocol(Protocol):
    def get_database_connection(self) -> Any:
        ...
        
    def get_repository(self) -> BaseRepository[T]:
        ...
        
    def get_unit_of_work(self) -> BaseUnitfWork:
        ...
        
    def get_use_case(self) -> UseCase:
        ...