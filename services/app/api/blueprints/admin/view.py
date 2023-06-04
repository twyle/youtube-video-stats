from flask import Blueprint, request
from flasgger import swag_from
from ...controllers.response_builders.create_response import ResponseBuilder
from ...controllers.controllers.user_controller_factory import CreateAdminControllerFactory
from ..flow import flow


admin = Blueprint('admin', __name__)

@swag_from('./docs/register.yml', endpoint='admin.register', methods=['POST'])
@admin.route('/register', methods=['POST'])
def register():
    controller = CreateAdminControllerFactory()
    return flow(controller)