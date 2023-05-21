from typing import Any
from abc import ABC, abstractmethod
    
class RequestHandlerBase(ABC):    
    @abstractmethod    
    def __call__(self, data: dict[str, Any]) -> dict[str, Any]:
        pass
        