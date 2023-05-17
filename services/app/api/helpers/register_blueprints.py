from ..blueprints.videos.view import videos
from ..blueprints.auth.view import auth
from flask import Flask


def register_blueprints(app: Flask) -> None:
    """Register the application blueprints."""
    app.register_blueprint(videos, url_prefix='/videos')
    app.register_blueprint(auth, url_prefix='/auth')