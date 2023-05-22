from flask import Blueprint, request
from flasgger import swag_from
from ...controllers.response_builders.create_response import ResponseBuilder
from ...controllers.controllers.video_controller_factory import (
    AddVideoControllerFactory, GetVideoControllerFactory, UpdateVideoControllerFactory, 
    DeleteVideoControllerFactory, GetVideosControllerFactory
)


videos = Blueprint('videos', __name__)


@swag_from('./docs/add.yml', endpoint='videos.add', methods=['POST'])
@videos.route('/video', methods=['POST'])
def add():
    controller = AddVideoControllerFactory()
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

@swag_from('./docs/get.yml', endpoint='videos.get', methods=['GET'])
@videos.route('/video', methods=['GET'])
def get():
    controller = GetVideoControllerFactory()
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

@swag_from('./docs/update.yml', endpoint='videos.update', methods=['PUT'])
@videos.route('/video', methods=['PUT'])
def update():
    controller = UpdateVideoControllerFactory()
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

@swag_from('./docs/delete.yml', endpoint='videos.delete', methods=['DELETE'])
@videos.route('/video', methods=['DELETE'])
def delete():
    controller = DeleteVideoControllerFactory()
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


@swag_from('./docs/videos.yml', endpoint='videos.list_all', methods=['GET'])
@videos.route('/', methods=['GET'])
def list_all():
    controller = GetVideosControllerFactory()
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


@swag_from('./docs/comments.yml', endpoint='videos.get_video_comments', methods=['GET'])
@videos.route('/video/comments', methods=['GET'])
def get_video_comments():
    """Get the comments for a particular video."""
    return 'Video Comments.'