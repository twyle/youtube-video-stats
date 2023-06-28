from flasgger import swag_from
from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from ...controllers.controllers.user_controller_factory import (
    ActivateAccountControllerFactory,
    CreateUserControllerFactory,
    DeleteUserControllerFactory,
    GetUserControllerFactory,
    ListUsersControllerFactory,
    LoginUserControllerFactory,
    UpdateUserControllerFactory,
)
from ...controllers.response_builders.create_response import ResponseBuilder
from ..decorators import admin_token_required
from ..flow import flow

auth = Blueprint("auth", __name__)


@swag_from("./docs/register.yml", endpoint="auth.register_client", methods=["POST"])
@auth.route("/register", methods=["POST"])
def register_client():
    controller = CreateUserControllerFactory()
    return flow(controller)


@auth.route("/get", methods=["GET"])
# @jwt_required()
@swag_from("./docs/get.yml", endpoint="auth.get_client", methods=["GET"])
def get_client():
    controller = GetUserControllerFactory()
    return flow(controller)


@auth.route("/update", methods=["PUT"])
# @jwt_required()
@swag_from("./docs/update.yml", endpoint="auth.update_client", methods=["PUT"])
def update_client():
    controller = UpdateUserControllerFactory()
    return flow(controller)


@auth.route("/delete", methods=["DELETE"])
# @admin_token_required
@swag_from("./docs/delete.yml", endpoint="auth.delete_client", methods=["DELETE"])
def delete_client():
    controller = DeleteUserControllerFactory()
    return flow(controller)


@auth.route("/users", methods=["GET"])
# @admin_token_required
@swag_from("./docs/users.yml", endpoint="auth.list_all", methods=["GET"])
def list_all():
    controller = ListUsersControllerFactory()
    return flow(controller)


@swag_from("./docs/activate.yml", endpoint="auth.activate_account", methods=["GET"])
@auth.route("/activate", methods=["GET"])
def activate_account():
    """Activate User account."""
    controller = ActivateAccountControllerFactory()
    return flow(controller)


@swag_from("./docs/login.yml", endpoint="auth.login_client", methods=["POST"])
@auth.route("/login", methods=["POST"])
def login_client():
    """Login a registered, confirmed client."""
    controller = LoginUserControllerFactory()
    return flow(controller)


@swag_from(
    "./docs/password_reset.yml",
    endpoint="auth.request_client_password_reset",
    methods=["GET"],
)
@auth.route("/request_password_reset", methods=["GET"])
def request_client_password_rest():
    """Request a client password reset."""
    # get email address
    # confirm user exists
    # give them access token
    return "Password reset."


@swag_from("./docs/reset_password.yml", endpoint="auth.reset_password", methods=["POST"])
@auth.route("/reset_password", methods=["POST"])
def reset_client_password():
    """Reset a client password."""
    # provide token
    # provide email
    # provide password
    return "Password reset."


@auth.route("/refresh_token", methods=["POST"])
@swag_from("./docs/refresh_token.yml", endpoint="auth.refresh_token", methods=["POST"])
def refresh_token():
    """Refresh an expired token."""
    # user_id = request.args.get('user_id')
    # if not access_token:
    #     return {'Error': 'The refresh token has to be provided.'}, 401
    # access_token = create_access_token(user_id)
    # return access_token
