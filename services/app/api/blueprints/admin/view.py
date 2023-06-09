from flasgger import swag_from
from flask import Blueprint

from ...controllers.controllers.user_controller_factory import (
    CreateAdminControllerFactory,
    DeleteUserControllerFactory,
    ListUsersControllerFactory,
    LoginAdminControllerFactory,
)
from ..decorators import admin_token_required
from ..flow import flow

admin = Blueprint("admin", __name__)


@swag_from("./docs/register.yml", endpoint="admin.register", methods=["POST"])
@admin.route("/register", methods=["POST"])
def register():
    controller = CreateAdminControllerFactory()
    return flow(controller)


@swag_from("./docs/login.yml", endpoint="admin.login_client", methods=["POST"])
@admin.route("/login", methods=["POST"])
def login_client():
    """Login a registered, confirmed client."""
    controller = LoginAdminControllerFactory()
    return flow(controller)


@admin.route("/get", methods=["GET"])
@admin_token_required
@swag_from("./docs/get.yml", endpoint="admin.get", methods=["GET"])
def get():
    controller = CreateAdminControllerFactory()
    return flow(controller)


@admin.route("/update", methods=["PUT"])
@admin_token_required
@swag_from("./docs/update.yml", endpoint="admin.update", methods=["PUT"])
def update():
    controller = CreateAdminControllerFactory()
    return flow(controller)


@admin.route("/delete", methods=["DELETE"])
@admin_token_required
@swag_from("./docs/delete.yml", endpoint="admin.delete", methods=["DELETE"])
def delete():
    controller = DeleteUserControllerFactory()
    return flow(controller)


@admin.route("/list_all", methods=["GET"])
@admin_token_required
@swag_from("./docs/admins.yml", endpoint="admin.list_all", methods=["GET"])
def list_all():
    controller = ListUsersControllerFactory()
    return flow(controller)
