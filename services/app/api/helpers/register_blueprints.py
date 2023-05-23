from ..blueprints.videos.view import videos
from ..blueprints.auth.view import auth
from ..blueprints.channels.view import channels
from flask import Flask


def register_blueprints(app: Flask) -> None:
    """Register the application blueprints."""
    app.register_blueprint(videos, url_prefix='/api/v1/videos')
    app.register_blueprint(auth, url_prefix='/api/v1/auth')
    app.register_blueprint(channels, url_prefix='/api/v1/channels')