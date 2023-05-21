from flask import Blueprint, request
from flasgger import swag_from
from ...controllers.response_builders.create_response import ResponseBuilder
from ...controllers.controllers.user_controller_factory import CreateUserControllerFactory

auth = Blueprint('auth', __name__)

@swag_from('./docs/register.yml', endpoint='auth.register_client', methods=['POST'])
@auth.route('/register', methods=['POST'])
def register_client():
    controller = CreateUserControllerFactory()
    create_user_builder = ResponseBuilder()
    api_response = (
        create_user_builder.with_data_validators(controller.get_request_data_validator())
        .with_request_builder(controller.get_request_builder())
        .with_request_object(request)
        .with_request_handler(controller.get_request_handler())
        .with_controller(controller.get_controller())
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
