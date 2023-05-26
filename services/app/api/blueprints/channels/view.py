from flask import Blueprint, request
from flasgger import swag_from
from ...controllers.response_builders.create_response import ResponseBuilder
from ...controllers.controllers.channel_controller_factory import (
    AddChannelControllerFactory, GetChannelControllerFactory, UpdateChannelControllerFactory, 
    DeleteChannelControllerFactory, GetChannelsControllerFactory, AddManyChannelsControllerFactory,
    QueryChannelsControllerFactory
)


channels = Blueprint('channels', __name__)


@swag_from('./docs/add.yml', endpoint='channels.add', methods=['POST'])
@channels.route('/channel', methods=['POST'])
def add():
    controller = AddChannelControllerFactory()
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

@swag_from('./docs/update.yml', endpoint='channels.update', methods=['PUT'])
@channels.route('/channel', methods=['PUT'])
def update():
    controller = UpdateChannelControllerFactory()
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

@swag_from('./docs/delete.yml', endpoint='channels.delete', methods=['DELETE'])
@channels.route('/channel', methods=['DELETE'])
def delete():
    controller = DeleteChannelControllerFactory()
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

@swag_from('./docs/get.yml', endpoint='channels.get', methods=['GET'])
@channels.route('/channel', methods=['GET'])
def get():
    controller = GetChannelControllerFactory()
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


@channels.route('/', methods=['POST'])
# @admin_token_required
@swag_from('./docs/add_many.yml', endpoint='channels.add_many', methods=['POST'])
def add_many():
    controller = AddManyChannelsControllerFactory()
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


@swag_from('./docs/channels.yml', endpoint='channels.list_all_channels', methods=['GET'])
@channels.route('/', methods=['GET'])
def list_all_channels(): 
    controller = GetChannelsControllerFactory()
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


@swag_from('./docs/add.yml', endpoint='channels.channel_Channels', methods=['GET'])
@channels.route('/channel/videos', methods=['GET'])
def channel_videos():
    return 'Channel Videos'


@swag_from('./docs/add.yml', endpoint='channels.channel_playlists', methods=['GET'])
@channels.route('/channel/playlists', methods=['GET'])
def channel_playlists():
    return 'Channel Playlists'


@swag_from('./docs/add.yml', endpoint='channels.channel_comments', methods=['GET'])
@channels.route('/channel/comments', methods=['GET'])
def channel_comments():
    return 'Channel Comments'