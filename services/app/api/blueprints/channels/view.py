from flask import Blueprint
from flasgger import swag_from
from ...controllers.controllers.channel_controller_factory import (
    AddChannelControllerFactory, GetChannelControllerFactory, UpdateChannelControllerFactory, 
    DeleteChannelControllerFactory, GetChannelsControllerFactory, AddManyChannelsControllerFactory,
    QueryChannelsControllerFactory
)
from ..flow import flow
from ..decorators import admin_token_required
from flask_jwt_extended import jwt_required


channels = Blueprint('channels', __name__)


@swag_from('./docs/add.yml', endpoint='channels.add', methods=['POST'])
@channels.route('/channel', methods=['POST'])
def add():
    controller = AddChannelControllerFactory()
    return flow(controller) 

@swag_from('./docs/update.yml', endpoint='channels.update', methods=['PUT'])
@channels.route('/channel', methods=['PUT'])
def update():
    controller = UpdateChannelControllerFactory()
    return flow(controller)


@swag_from('./docs/delete.yml', endpoint='channels.delete', methods=['DELETE'])
@channels.route('/channel', methods=['DELETE'])
def delete():
    controller = DeleteChannelControllerFactory()
    return flow(controller)


@swag_from('./docs/get.yml', endpoint='channels.get', methods=['GET'])
@channels.route('/channel', methods=['GET'])
def get():
    controller = GetChannelControllerFactory()
    return flow(controller)


@channels.route('/', methods=['POST'])
# @admin_token_required
@swag_from('./docs/add_many.yml', endpoint='channels.add_many', methods=['POST'])
def add_many():
    controller = AddManyChannelsControllerFactory()
    return flow(controller)


@channels.route('/', methods=['GET'])
@jwt_required()
@swag_from('./docs/channels.yml', endpoint='channels.list_all_channels', methods=['GET'])
def list_all_channels(): 
    controller = GetChannelsControllerFactory()
    return flow(controller)


@swag_from('./docs/add.yml', endpoint='channels.channel_Channels', methods=['GET'])
@channels.route('/channel/videos', methods=['GET'])
def channel_videos():
    return 'Channel Videos'


@swag_from('./docs/videos.yml', endpoint='channels.channel_playlists', methods=['GET'])
@channels.route('/channel/playlists', methods=['GET'])
def channel_playlists():
    controller = QueryChannelsControllerFactory()
    return flow(controller)


@swag_from('./docs/add.yml', endpoint='channels.channel_comments', methods=['GET'])
@channels.route('/channel/comments', methods=['GET'])
def channel_comments():
    return 'Channel Comments'