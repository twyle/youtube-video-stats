from flask import Blueprint, request
from flasgger import swag_from
from ...controllers.response_builders.create_response import ResponseBuilder
from ...controllers.controllers.comment_controller_factory import (
    AddCommentControllerFactory, GetCommentControllerFactory, UpdateCommentControllerFactory, 
    DeleteCommentControllerFactory, GetCommentsControllerFactory, AddManyCommentsControllerFactory,
    QueryCommentsControllerFactory
)


comments = Blueprint('comments', __name__)


@swag_from('./docs/add.yml', endpoint='comments.add', methods=['POST'])
@comments.route('/comment', methods=['POST'])
def add():
    controller = AddCommentControllerFactory()
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

@swag_from('./docs/update.yml', endpoint='comments.update', methods=['PUT'])
@comments.route('/comment', methods=['PUT'])
def update():
    controller = UpdateCommentControllerFactory()
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

@swag_from('./docs/delete.yml', endpoint='comments.delete', methods=['DELETE'])
@comments.route('/comment', methods=['DELETE'])
def delete():
    controller = DeleteCommentControllerFactory()
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

@swag_from('./docs/get.yml', endpoint='comments.get', methods=['GET'])
@comments.route('/comment', methods=['GET'])
def get():
    controller = GetCommentControllerFactory()
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


@comments.route('/', methods=['POST'])
# @admin_token_required
@swag_from('./docs/add_many.yml', endpoint='comments.add_many', methods=['POST'])
def add_many():
    controller = AddManyCommentsControllerFactory()
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


@swag_from('./docs/comments.yml', endpoint='comments.list_all_comments', methods=['GET'])
@comments.route('/', methods=['GET'])
def list_all_comments(): 
    controller = GetCommentsControllerFactory()
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


@swag_from('./docs/videos.yml', endpoint='comments.video_comments', methods=['GET'])
@comments.route('/video/', methods=['GET'])
def video_comments():
    controller = QueryCommentsControllerFactory()
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


@swag_from('./docs/channels.yml', endpoint='channels.channel_channels', methods=['GET'])
@comments.route('/channel/', methods=['GET'])
def channel_channels():
    return 'channel channels'