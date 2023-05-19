from ..validators.validator_factory import ValidatorFactory
from ..requests.api_request import APIRequest
from ..controllers.controller import Controller
from abc import ABC, abstractmethod


class ResponseBuilder(ABC):  
    @abstractmethod     
    def with_create_data_validator(self, create_data_validator: ValidatorFactory):
        raise NotImplementedError()
    
    @abstractmethod
    def with_create_request(self, create_request: APIRequest):
        raise NotImplementedError()
    
    # def with_register_user_controller(self, register_user_controller: RegisterUserController):
    #     self.__register_user_controller = register_user_controller
    #     return self
    
    @abstractmethod
    def with_request_object(self, request_object):
        raise NotImplementedError()
    
    @abstractmethod
    def build(self):
        raise NotImplementedError()