from abc import ABC, abstractmethod
from typing import Any


class RequestHandlerBase(ABC):
    @abstractmethod
    def __call__(self, data: dict[str, Any]) -> dict[str, Any]:
        pass
