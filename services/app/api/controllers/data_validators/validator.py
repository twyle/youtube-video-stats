from abc import ABC, abstractmethod
from typing import Any


class DataValidator(ABC):
    @abstractmethod
    def __call__(self, data: dict[str, Any]) -> dict[str, Any]:
        pass

    @abstractmethod
    def validate(data: dict[str, Any]) -> dict[str, Any]:
        pass
