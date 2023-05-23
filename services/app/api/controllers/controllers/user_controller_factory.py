from .base_controller_factory import BaseControllerFactory
from ..data_validators.validator_factory import DataValidatorList
from ..data_validators.data_validators import (
    NameValidator, EmailValidator, PasswordValidator, PasswordMatchValidator
)
from ...database.request_handler.request_handler_base import RequestHandlerBase
from ...database.request_handler.request_handler import RequestHandler
from ...database.request_handler.user_factories import (
    AddUserSQLiteFactory, ListUsersSQLiteFactory, DeleteUserSQLiteFactory
)

class CreateUserControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = [
            NameValidator(attr='first_name'),
            NameValidator(attr='last_name'),
            EmailValidator(),
            PasswordValidator(),
            PasswordMatchValidator()
        ]
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = AddUserSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
class DeleteUserControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = DeleteUserSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
class ListUsersControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = ListUsersSQLiteFactory()
        return RequestHandler(request_handler_factory)