from flask import Blueprint
from flasgger import swag_from


videos = Blueprint('videos', __name__)


@swag_from('./docs/channels.yml', endpoint='videos.list_all_channels', methods=['GET'])
@videos.route('/channels', methods=['GET'])
def list_all_channels():
    return 'All channels.'


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