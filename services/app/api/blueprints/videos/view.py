from flask import Blueprint, request
from flasgger import swag_from
from ...controllers.list_channels_controller_factory import ListChannelsControllerFactory
from ...controllers.response_builders.create_response import ResponseBuilder


videos = Blueprint('videos', __name__)


@swag_from('./docs/channels.yml', endpoint='videos.list_all_channels', methods=['GET'])
@videos.route('/channels', methods=['GET'])
def list_all_channels(): 
    list_channels_controller = ListChannelsControllerFactory()
    response_builder = ResponseBuilder()
    api_response = (
        response_builder.with_data_validators(list_channels_controller.get_request_data_validator())
        .with_request_builder(list_channels_controller.get_request_builder())
        .with_request_object(request)
        .with_request_handler(list_channels_controller.get_request_handler())
        .with_controller(list_channels_controller.get_controller())
        .build()
    )
    return api_response


@swag_from('./docs/videos.yml', endpoint='videos.get_channel_videos', methods=['GET'])
@videos.route('/channels/<string:channel_id>', methods=['GET'])
def get_channel_videos():
    """List videos for a particular channel."""
    return 'Channel Videos.'


@swag_from('./docs/comments.yml', endpoint='videos.get_video_comments', methods=['GET'])
@videos.route('/videos/<string:video_id>/comments', methods=['GET'])
def get_video_comments():
    """Get the comments for a particular video."""
    return 'Video Comments.'