from ..controllers.controllers.base_controller_factory import BaseControllerFactory
from ..controllers.response_builders.create_response import ResponseBuilder
from flask import request


def flow(controller: BaseControllerFactory) -> tuple[dict, int]:
    response_builder = ResponseBuilder()
    api_response = (
        response_builder.with_data_validators(controller.get_request_data_validator())
        .with_request_builder(controller.get_request_builder())
        .with_request_object(request)
        .with_request_handler(controller.get_request_handler())
        .with_controller(controller.get_controller())
        .build()
    )
    return api_response
    