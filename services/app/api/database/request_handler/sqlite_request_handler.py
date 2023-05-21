from typing import Any
from ..repositories.unit_of_work import BaseUnitfWork
from ..connections import create_sqlite_database_connection
from .factories import RequestHandlerFactory
from ..repositories.unit_of_work import UnitOfWork

class SQLiteRequestHandlerFactory(RequestHandlerFactory):
    def get_database_connection(self) -> Any:
        return create_sqlite_database_connection
        
    def get_unit_of_work(self) -> BaseUnitfWork:
        return UnitOfWork()
