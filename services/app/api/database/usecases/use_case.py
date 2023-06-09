from abc import ABC, abstractmethod
from typing import Any, Optional

from ..repositories.unit_of_work import BaseUnitfWork


class UseCase(ABC):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        self.__unit_of_work = unit_of_work

    @property
    def unit_of_work(self) -> BaseUnitfWork:
        return self.__unit_of_work

    @unit_of_work.setter
    def unit_of_work(self, unit_of_work: BaseUnitfWork) -> None:
        self.__unit_of_work = unit_of_work

    @abstractmethod
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        pass
