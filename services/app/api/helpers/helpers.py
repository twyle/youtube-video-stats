import os
from flask import Flask
from ..config.config import Config

def set_configuration(app: Flask) -> None:
    """Set the application configuration.

    The application configuration will depend on the
    environment i.e Test, Development, Staging or Production.

    Parameters
    ----------
    app: flask.Flask
        A flask app instance

    Returns
    -------
    bool:
        Whether the config was set up successfully.
    """
    config_name = os.environ.get("FLASK_ENV")
    app.config.from_object(Config[config_name])