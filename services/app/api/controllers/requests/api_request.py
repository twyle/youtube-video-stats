from abc import ABC, abstractmethod
from typing import Any
from flask import request

class APIRequest(ABC):
    @abstractmethod
    def __call__(self) -> dict[str, str]:
        pass
        
    @abstractmethod
    def get_request_data(self) -> dict[str, str]:
        pass
    
    @abstractmethod
    def validate_request_data(self) -> dict[str, str]:
        pass