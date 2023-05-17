from abc import ABC, abstractmethod
from typing import Any
from ..requests.api_request import APIRequest


class Controller(ABC):                
    @abstractmethod
    def __call__(self) -> tuple[dict, int]:
        pass
        
    @abstractmethod
    def handle_request(self) -> tuple[dict, int]:
        pass