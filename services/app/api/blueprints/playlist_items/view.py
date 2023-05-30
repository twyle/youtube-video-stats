from flask import Blueprint, request
from flasgger import swag_from
from ...controllers.response_builders.create_response import ResponseBuilder
from ...controllers.controllers.playlist_item_controller_factory import (
    AddPlaylistItemControllerFactory, GetPlaylistItemControllerFactory, UpdatePlaylistItemControllerFactory, 
    DeletePlaylistItemControllerFactory, GetPlaylistItemsControllerFactory, AddManyPlaylistItemsControllerFactory,
    QueryPlaylistItemsControllerFactory
)


playlist_items = Blueprint('playlist_items', __name__)


@swag_from('./docs/add.yml', endpoint='playlist_items.add', methods=['POST'])
@playlist_items.route('/playlist_item', methods=['POST'])
def add():
    controller = AddPlaylistItemControllerFactory()
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

@swag_from('./docs/update.yml', endpoint='playlist_items.update', methods=['PUT'])
@playlist_items.route('/playlist_item', methods=['PUT'])
def update():
    controller = UpdatePlaylistItemControllerFactory()
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

@swag_from('./docs/delete.yml', endpoint='playlist_items.delete', methods=['DELETE'])
@playlist_items.route('/playlist_item', methods=['DELETE'])
def delete():
    controller = DeletePlaylistItemControllerFactory()
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

@swag_from('./docs/get.yml', endpoint='playlist_items.get', methods=['GET'])
@playlist_items.route('/playlist_item', methods=['GET'])
def get():
    controller = GetPlaylistItemControllerFactory()
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


@playlist_items.route('/', methods=['POST'])
# @admin_token_required
@swag_from('./docs/add_many.yml', endpoint='playlist_items.add_many', methods=['POST'])
def add_many():
    controller = AddManyPlaylistItemsControllerFactory()
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


@swag_from('./docs/playlist_items.yml', endpoint='playlist_items.list_all_playlist_items', methods=['GET'])
@playlist_items.route('/', methods=['GET'])
def list_all_playlist_items(): 
    controller = GetPlaylistItemsControllerFactory()
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


@swag_from('./docs/playlist_videos.yml', endpoint='playlist_items.video', methods=['GET'])
@playlist_items.route('/playlist_item/video', methods=['GET'])
def video():
    return 'Playlist Item Video'