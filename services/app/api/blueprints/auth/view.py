from flask import Blueprint, request
from flasgger import swag_from
from ...controllers.request_builders.create_user_request_builder import CreateUserRequestBuilder
from ...controllers.data_validators.validator_factory import DataValidatorList
from ...controllers.response_builders.create_response import ResponseBuilder
from ...controllers.data_validators.data_validators import (
    NameValidator, EmailValidator, PasswordValidator, PasswordMatchValidator
)
from ...controllers.controllers.register_user_controller import RegisterUserController
from ...database.builder.user_builder import CreateUserRequestHandler
from ...database.connections import create_sqlite_database_connection
from ...database.repositories.sqlite_repository import SQLiteUserRepository
from ...database.repositories.user_unit_of_work import UserUnitOfWork
from ...database.usecases.create_user import CreateUserUseCase

auth = Blueprint('auth', __name__)

@swag_from('./docs/register.yml', endpoint='auth.register_client', methods=['POST'])
@auth.route('/register', methods=['POST'])
def register_client():
    validators = [
        NameValidator(attr='first_name'),
        NameValidator(attr='last_name'),
        EmailValidator(),
        PasswordValidator(),
        PasswordMatchValidator()
    ]
    request_data_validators = DataValidatorList(validators)
    create_user_request_builder = CreateUserRequestBuilder()
    register_user_controller = RegisterUserController()
    create_user_builder = ResponseBuilder()
    sqlite_repository = SQLiteUserRepository()
    unit_of_work = UserUnitOfWork()
    create_user_use_case = CreateUserUseCase()
    create_user_request_handler = CreateUserRequestHandler(create_sqlite_database_connection, 
                sqlite_repository, unit_of_work, create_user_use_case)
    api_response = (
        create_user_builder.with_data_validators(request_data_validators)
        .with_request_builder(create_user_request_builder)
        .with_request_object(request)
        .with_request_handler(create_user_request_handler)
        .with_controller(register_user_controller)
        .build()
    )
    return api_response


@swag_from('./docs/confirm_email.yml', endpoint='auth.confirm_client_email', methods=['GET'])
@auth.route('/confirm_email', methods=['GET'])
def confirm_client_email():
    """Confirm email address."""
    return 'Email confirmed.'


@swag_from('./docs/login.yml', endpoint='auth.login_client', methods=['POST'])
@auth.route('/login', methods=['POST'])
def login_client():
    """Login a registered, confirmed client."""
    return 'Logged in.'


@swag_from('./docs/password_reset.yml', endpoint='auth.request_client_password_rest', methods=['GET'])
@auth.route('/request_password_reset', methods=['GET'])
def request_client_password_rest():
    """Request a client password reset."""
    return 'Password reset.'


@swag_from('./docs/reset_password.yml', endpoint='auth.reset_password', methods=['POST'])
@auth.route('/reset_password', methods=['POST'])
def reset_client_password():
    """Reset a client password."""
    return 'Password reset.'


@swag_from('./docs/refresh_token.yml', endpoint='auth.refresh_token', methods=['POST'])
@auth.route('/refresh_token', methods=['POST'])
def refresh_token():
    """Refresh an expired token."""
    return 'Token refreshed.'
