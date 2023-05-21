from typing import Protocol
from .data_validators.validator_factory import DataValidatorList
from .request_builders.request_builder import RequestBuilder
from ..database.request_handler.request_handler import RequestHandler

class ControllerFactory(Protocol):
    def get_request_data_validator(self) -> DataValidatorList:
        ...
        
    def get_request_bulder(self) -> RequestBuilder:
        ...
        
    def get_request_handler(self) -> RequestHandler:
        ...