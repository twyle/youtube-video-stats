from typing import Any

from .factories import RequestHandlerFactory
from .request_handler_base import RequestHandlerBase


class RequestHandler(RequestHandlerBase):
    def __init__(self, factory: RequestHandlerFactory) -> None:
        self.__connection = factory.get_database_connection()
        self.__repository = factory.get_repository()
        self.__unit_of_work = factory.get_unit_of_work()
        self.__use_case = factory.get_use_case()

    def __call__(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.__connection() as conn:
            self.__repository.connection = conn
            self.__unit_of_work.connection = conn
            self.__unit_of_work.repository = self.__repository
            self.__use_case.unit_of_work = self.__unit_of_work
            user = self.__use_case.execute(data)
        return user
