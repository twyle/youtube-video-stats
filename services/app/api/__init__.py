from flask import Flask, jsonify
from .helpers.register_blueprints import register_blueprints
from .helpers.register_extensions import register_extensions
from .helpers.helpers import set_configuration
from .helpers.error_handlers import register_error_handlers


def create_app() -> Flask:
    """Create the flask app instance."""
    app = Flask(__name__)
    
    set_configuration(app)
    register_error_handlers(app)
    register_extensions(app)
    register_blueprints(app)
    
    @app.route('/', methods=['GET'])
    def health_check():
        return jsonify({'success': 'Hello from the stats API.'}), 200
    
    app.shell_context_processor({"app": app})

    return app