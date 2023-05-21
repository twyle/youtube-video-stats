from ..request_builders.request_builder import RequestBuilder
from ..controllers.controller import Controller
from ..data_validators.validator_factory import ValidatorList
from .create_response_base import ResponseBuilderBase
from flask import Request
from ...database.request_handler.request_handler import RequestHandler

class ResponseBuilder(ResponseBuilderBase):    
    def __init__(self) -> None:
        self.__data_validators = None
        self.__request_builder = None
        self.__controller = None
        self.__request_object = None
         
    def with_data_validators(self, data_validators: ValidatorList):
        self.__data_validators = data_validators
        return self
    
    def with_request_builder(self, request_builder: RequestBuilder):
        self.__request_builder = request_builder
        return self
    
    def with_controller(self, controller: Controller):
        self.__controller = controller
        return self
    
    def with_request_object(self, request_object: Request):
        self.__request_object = request_object
        return self
    
    def with_request_handler(self, request_handler: RequestHandler):
        self.__request_handler = request_handler
        return self
    
    def build(self):
        if (not self.__data_validators or not self.__request_builder or not 
            self.__request_object or not self.__controller):
            raise ValueError('All the dependencies must be provided before building the use case.')
        return self.__controller(
            self.__request_builder, self.__data_validators, self.__request_object, 
            self.__request_handler
        )
    
    