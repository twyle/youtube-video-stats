from ...database.request_handler.request_handler import RequestHandler
from ...database.request_handler.request_handler_base import RequestHandlerBase
from ...database.request_handler.user_factories import (
    ActivateAccountSQLiteFactory,
    AddAdminSQLiteFactory,
    AddUserSQLiteFactory,
    DeleteUserSQLiteFactory,
    GetUserSQLiteFactory,
    ListUsersSQLiteFactory,
    LoginUserSQLiteFactory,
    UpdateUserSQLiteFactory,
)
from ..data_validators.data_validators import (
    EmailValidator,
    NameValidator,
    PasswordMatchValidator,
    PasswordValidator,
)
from ..data_validators.validator_factory import DataValidatorList
from .base_controller_factory import BaseControllerFactory


class CreateUserControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = [
            NameValidator(attr="first_name"),
            NameValidator(attr="last_name"),
            EmailValidator(),
            PasswordValidator(),
            PasswordMatchValidator(),
        ]
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = AddUserSQLiteFactory()
        return RequestHandler(request_handler_factory)


class GetUserControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = GetUserSQLiteFactory()
        return RequestHandler(request_handler_factory)


class UpdateUserControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = UpdateUserSQLiteFactory()
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


class ActivateAccountControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = ActivateAccountSQLiteFactory()
        return RequestHandler(request_handler_factory)


class LoginUserControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = LoginUserSQLiteFactory()
        return RequestHandler(request_handler_factory)


class CreateAdminControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = [
            NameValidator(attr="first_name"),
            NameValidator(attr="last_name"),
            EmailValidator(),
            PasswordValidator(),
            PasswordMatchValidator(),
        ]
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = AddAdminSQLiteFactory()
        return RequestHandler(request_handler_factory)
