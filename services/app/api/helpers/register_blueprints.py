from ..blueprints.auth.view import auth
from flask import Flask


def register_blueprints(app: Flask) -> None:
    """Register the application blueprints."""
    app.register_blueprint(auth, url_prefix='/auth')