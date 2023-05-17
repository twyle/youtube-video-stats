from abc import ABC, abstractmethod
from ..requests.api_request import APIRequest


class Controller(ABC):
    def __init__(self, request_data: dict[str, str]) -> None:
        self.__request_data = request_data
        
    @abstractmethod
    def handle_request(self) -> tuple[dict, int]:
        pass