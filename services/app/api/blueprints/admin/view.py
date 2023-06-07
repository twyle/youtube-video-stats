from flask import Blueprint
from flasgger import swag_from
from ...controllers.controllers.user_controller_factory import (
    CreateAdminControllerFactory, DeleteUserControllerFactory, ListUsersControllerFactory
)
from ..flow import flow


admin = Blueprint('admin', __name__)

@swag_from('./docs/register.yml', endpoint='admin.register', methods=['POST'])
@admin.route('/register', methods=['POST'])
def register():
    controller = CreateAdminControllerFactory()
    return flow(controller)


@swag_from('./docs/get.yml', endpoint='admin.get', methods=['GET'])
@admin.route('/get', methods=['GET'])
def get():
    controller = CreateAdminControllerFactory()
    return flow(controller)


@swag_from('./docs/update.yml', endpoint='admin.update', methods=['PUT'])
@admin.route('/update', methods=['PUT'])
def update():
    controller = CreateAdminControllerFactory()
    return flow(controller)


@swag_from('./docs/delete.yml', endpoint='admin.delete', methods=['DELETE'])
@admin.route('/delete', methods=['DELETE'])
def delete():
    controller = DeleteUserControllerFactory()
    return flow(controller)


@swag_from('./docs/admins.yml', endpoint='admin.list_all', methods=['GET'])
@admin.route('/list_all', methods=['GET'])
def list_all():
    controller = ListUsersControllerFactory()
    return flow(controller)