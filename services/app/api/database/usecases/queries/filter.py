from abc import ABC, abstractmethod
from typing import Any, Optional


class Filter(ABC):
    def __init__(self, next_filter: Optional[Any] = None) -> None:
        self.__operator_map = {
            "gt": ">",
            "gte": ">=",
            "lt": "<",
            "eq": "=",
            "lte": "<=",
            "in": "IN",
            "not in": "NOT IN",
            "between": "",
            "not between": "",
        }
        self.__next_filter = next_filter

    @property
    def operator_map(self) -> dict[str, str]:
        return self.__operator_map

    @operator_map.setter
    def operator_map(self, operator_map: dict[str, str]) -> None:
        self.__operator_map = operator_map

    @property
    def next_filter(self) -> Any:
        return self.__next_filter

    @next_filter.setter
    def next_filter(self, next_filter: Any) -> None:
        self.__next_filter = next_filter

    @abstractmethod
    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        pass
