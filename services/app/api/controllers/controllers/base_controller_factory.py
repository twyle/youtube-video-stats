from abc import ABC, abstractmethod
from ..data_validators.validator_factory import DataValidatorList
from ..request_builders.request_builder_base import RequestBuilderBase
from ..request_builders.request_builder import RequestBuilder
from ...database.request_handler.request_handler_base import RequestHandlerBase
from .base_controller import BaseController
from .controller import Controller

class BaseControllerFactory(ABC):
    @abstractmethod
    def get_request_data_validator(self) -> DataValidatorList:
        pass
        
    def get_request_builder(self) -> RequestBuilderBase:
        return RequestBuilder()
    
    def get_controller(self) -> BaseController:
        return Controller()
    
    @abstractmethod    
    def get_request_handler(self) -> RequestHandlerBase:
        pass