from flask import Blueprint, request
from flasgger import swag_from
from ...controllers.response_builders.create_response import ResponseBuilder
from ...controllers.controllers.playlist_controller_factory import (
    AddPlaylistControllerFactory, GetPlaylistControllerFactory, UpdatePlaylistControllerFactory, 
    DeletePlaylistControllerFactory, GetPlaylistsControllerFactory, AddManyPlaylistsControllerFactory,
    QueryPlaylistsControllerFactory
)


playlists = Blueprint('playlists', __name__)


@swag_from('./docs/add.yml', endpoint='playlists.add', methods=['POST'])
@playlists.route('/playlist', methods=['POST'])
def add():
    controller = AddPlaylistControllerFactory()
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

@swag_from('./docs/update.yml', endpoint='playlists.update', methods=['PUT'])
@playlists.route('/playlist', methods=['PUT'])
def update():
    controller = UpdatePlaylistControllerFactory()
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

@swag_from('./docs/delete.yml', endpoint='playlists.delete', methods=['DELETE'])
@playlists.route('/playlist', methods=['DELETE'])
def delete():
    controller = DeletePlaylistControllerFactory()
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

@swag_from('./docs/get.yml', endpoint='playlists.get', methods=['GET'])
@playlists.route('/playlist', methods=['GET'])
def get():
    controller = GetPlaylistControllerFactory()
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


@playlists.route('/', methods=['POST'])
# @admin_token_required
@swag_from('./docs/add_many.yml', endpoint='playlists.add_many', methods=['POST'])
def add_many():
    controller = AddManyPlaylistsControllerFactory()
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


@swag_from('./docs/playlists.yml', endpoint='playlists.list_all_playlists', methods=['GET'])
@playlists.route('/', methods=['GET'])
def list_all_playlists(): 
    controller = GetPlaylistsControllerFactory()
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


@swag_from('./docs/playlist_videos.yml', endpoint='playlists.videos', methods=['GET'])
@playlists.route('/playlist/videos', methods=['GET'])
def videos():
    return 'Playlist Videos'