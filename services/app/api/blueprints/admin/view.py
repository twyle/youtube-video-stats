from flask import Blueprint, request
from flasgger import swag_from
from ...controllers.response_builders.create_response import ResponseBuilder
from ...controllers.controllers.user_controller_factory import CreateAdminControllerFactory

admin = Blueprint('admin', __name__)

@swag_from('./docs/register.yml', endpoint='admin.register', methods=['POST'])
@admin.route('/register', methods=['POST'])
def register():
    controller = CreateAdminControllerFactory()
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