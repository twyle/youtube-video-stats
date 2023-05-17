from flask import Flask
from .helpers.register_blueprints import register_blueprints
from .helpers.register_extensions import register_extensions


def create_app() -> Flask:
    """Create the flask app instance."""
    app = Flask(__name__)
    
    register_extensions(app)
    register_blueprints(app)
    
    app.shell_context_processor({"app": app})

    return app