from abc import ABC, abstractmethod
from flask import request

class APIRequest(ABC):
    def __init__(self, api_request) -> None:
        self.__api_request = request
        
    @abstractmethod
    def get_request_data(self) -> dict[str, str]:
        pass
    
    @abstractmethod
    def validate_request_data(self) -> dict[str, str]:
        pass