from typing import Protocol
from .data_validators.validator_factory import DataValidatorList
from .request_builders.request_builder import RequestBuilder
from ..database.request_handler.request_handler import RequestHandler
from .data_validators.data_validators import (
    NameValidator, EmailValidator, PasswordValidator, PasswordMatchValidator
)
from .request_builders.create_user_request_builder import CreateUserRequestBuilder
from ..database.request_handler.request_handler import RequestHandler
from ..database.request_handler.request_handler_factories import CreateUserSQLiteFactory
from .controllers.controller import Controller
from .controllers.register_user_controller import RegisterUserController

class CreateUserControllerFactory:
    def get_request_data_validator(self) -> DataValidatorList:
        validators = [
            NameValidator(attr='first_name'),
            NameValidator(attr='last_name'),
            EmailValidator(),
            PasswordValidator(),
            PasswordMatchValidator()
        ]
        return DataValidatorList(validators)
        
    def get_request_builder(self) -> RequestBuilder:
        return CreateUserRequestBuilder()
        
    def get_request_handler(self) -> RequestHandler:
        request_handler_factory = CreateUserSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
    def get_controller(self) -> Controller:
        return RegisterUserController()