from ..extensions.extensions import swagger, bcrypt, jwt
from flasgger import LazyJSONEncoder
from flask import Flask


def register_extensions(app: Flask) -> None:
    """Register the application extensions."""
    app.json_encoder = LazyJSONEncoder
    swagger.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)