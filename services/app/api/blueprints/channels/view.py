from flask import Blueprint, request
from flasgger import swag_from
from ...controllers.response_builders.create_response import ResponseBuilder
from ...controllers.controllers.video_controller_factory import AddVideoControllerFactory
from ...controllers.controllers.user_controller_factory import ListUsersControllerFactory


channels = Blueprint('channels', __name__)


@swag_from('./docs/add.yml', endpoint='channels.add', methods=['POST'])
@channels.route('/channel', methods=['POST'])
def add():
    return 'Channel Added'

@swag_from('./docs/add.yml', endpoint='channels.update', methods=['PUT'])
@channels.route('/channel', methods=['PUT'])
def update():
    return 'Channel Updated'

@swag_from('./docs/add.yml', endpoint='channels.delete', methods=['DELETE'])
@channels.route('/channel', methods=['DELETE'])
def delete():
    return 'Channel Deleted'

@swag_from('./docs/add.yml', endpoint='channels.get', methods=['GET'])
@channels.route('/channel', methods=['GET'])
def get():
    return 'Channel'

@swag_from('./docs/channels.yml', endpoint='channels.list_all_channels', methods=['GET'])
@channels.route('/', methods=['GET'])
def list_all_channels(): 
    controller = ListUsersControllerFactory()
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


@swag_from('./docs/add.yml', endpoint='channels.channel_videos', methods=['GET'])
@channels.route('/channel/videos', methods=['GET'])
def channel_videos():
    return 'Channel Videos'