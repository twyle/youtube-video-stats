from abc import ABC, abstractmethod
from typing import Any

class DataValidator(ABC):
    @abstractmethod
    def __call__(self, data: dict) -> dict:
        pass
    
    @abstractmethod
    def validate(data: dict) -> dict:
        pass