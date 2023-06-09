from typing import Any

from ..connections import create_sqlite_database_connection
from ..repositories.unit_of_work import BaseUnitfWork, UnitOfWork
from .factories import RequestHandlerFactory


class SQLiteRequestHandlerFactory(RequestHandlerFactory):
    def get_database_connection(self) -> Any:
        return create_sqlite_database_connection

    def get_unit_of_work(self) -> BaseUnitfWork:
        return UnitOfWork()
