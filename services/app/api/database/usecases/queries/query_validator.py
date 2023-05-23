from abc import ABC, abstractmethod
from typing import Any


class QueryValidator(ABC):
    @abstractmethod
    def __call__(self, query_parameters: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
        pass