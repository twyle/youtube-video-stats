from ..data_validators.validator_factory import ValidatorList
from ..request_builders.request_builder import RequestBuilder
from abc import ABC, abstractmethod
from flask import Request
from ..controllers.base_controller import BaseController


class ResponseBuilderBase(ABC):  
    @abstractmethod     
    def with_data_validators(self, data_validators: ValidatorList):
        raise NotImplementedError()
    
    @abstractmethod
    def with_request_builder(self, request_builder: RequestBuilder):
        raise NotImplementedError()
    
    @abstractmethod
    def with_controller(self, controller: BaseController):
        raise NotImplementedError()
    
    @abstractmethod
    def with_request_object(self, request_object: Request):
        raise NotImplementedError()
    
    @abstractmethod
    def build(self):
        raise NotImplementedError()