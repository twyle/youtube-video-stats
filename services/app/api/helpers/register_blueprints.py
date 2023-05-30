from ..blueprints.videos.view import videos
from ..blueprints.auth.view import auth
from ..blueprints.channels.view import channels
from ..blueprints.admin.view import admin
from ..blueprints.playlists.view import playlists
from ..blueprints.playlist_items.view import playlist_items
from ..blueprints.comment_authors.view import comment_authors
from ..blueprints.comments.view import comments
from flask import Flask


def register_blueprints(app: Flask) -> None:
    """Register the application blueprints."""
    app.register_blueprint(videos, url_prefix='/api/v1/videos')
    app.register_blueprint(auth, url_prefix='/api/v1/auth')
    app.register_blueprint(channels, url_prefix='/api/v1/channels')
    app.register_blueprint(admin, url_prefix='/api/v1/admin')
    app.register_blueprint(playlists, url_prefix='/api/v1/playlists')
    app.register_blueprint(playlist_items, url_prefix='/api/v1/playlist_items')
    app.register_blueprint(comment_authors, url_prefix='/api/v1/comment_authors')
    app.register_blueprint(comments, url_prefix='/api/v1/comments')