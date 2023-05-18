from ..validators.validator_factory import CreateUserValidator
from ..requests.create_user import CreateUserRequest
from ..controllers.register_user_controller import RegisterUserController

class CreateUserResponseBuilder:
    def __init__(self) -> None:
        self.__create_user_data_validator = None
        self.__create_user_request = None
        self.__register_user_controller = None
        
    def with_create_user_data_validator(self, create_user_data_validator: CreateUserValidator):
        self.__create_user_data_validator = create_user_data_validator
        return self
    
    def with_create_user_request(self, create_user_request: CreateUserRequest):
        self.__create_user_request = create_user_request
        return self
    
    # def with_register_user_controller(self, register_user_controller: RegisterUserController):
    #     self.__register_user_controller = register_user_controller
    #     return self
    
    def with_request_object(self, request_object):
        self.__request_object = request_object
        return self
    
    def build(self):
        if not self.__create_user_data_validator or not self.__create_user_request or not self.__request_object:
            raise ValueError('All the dependencies must be provided before building the use case.')
        create_user_controller = RegisterUserController(self.__create_user_request, 
                    self.__create_user_data_validator, self.__request_object)
        return create_user_controller
    
    