from abc import ABC, abstractmethod
from ..request_builders.request_builder import RequestBuilder
from ..data_validators.validator_factory import ValidatorList
from flask import Request


class Controller(ABC):                
    @abstractmethod
    def __call__(self, request_builder: RequestBuilder, data_validators: ValidatorList, 
                 request_object: Request) -> tuple[dict, int]:
        pass
        
    @abstractmethod
    def handle_request(self, request_builder: RequestBuilder, data_validators: ValidatorList, 
                 request_object: Request) -> tuple[dict, int]:
        pass