from flask import Blueprint, request
from flasgger import swag_from
from ...controllers.requests.create_user import CreateUserRequest
from ...controllers.validators.validator_factory import CreateUserValidator
from ...controllers.response.create_user_response import CreateUserResponseBuilder

auth = Blueprint('auth', __name__)

@swag_from('./docs/register.yml', endpoint='auth.register_client', methods=['POST'])
@auth.route('/register', methods=['POST'])
def register_client():
    request_data_validator = CreateUserValidator()
    create_user_request = CreateUserRequest()
    create_user_builder = CreateUserResponseBuilder()
    api_response = (
        create_user_builder.with_create_user_data_validator(request_data_validator)
        .with_create_user_request(create_user_request)
        .with_request_object(request)
        .build()
    )
    return api_response()


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
