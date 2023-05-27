# -*- coding: utf-8 -*-
"""This module declares the error handlers."""
from flask import jsonify, Flask
from http import HTTPStatus


def handle_resource_not_found(e):
    """Handle all resource not found errors."""
    return jsonify({"error": str(e)}), HTTPStatus.NOT_FOUND


def handle_method_not_allowed(e):
    """Handle all method not allowed errors."""
    return jsonify({"error": str(e)}), HTTPStatus.METHOD_NOT_ALLOWED


def handle_internal_server_error(e):
    """Handle all internal server errors."""
    return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR


def register_error_handlers(app: Flask) -> None:
    """Register the error handlers."""
    app.register_error_handler(HTTPStatus.NOT_FOUND, handle_resource_not_found)
    app.register_error_handler(HTTPStatus.METHOD_NOT_ALLOWED, handle_method_not_allowed)
    app.register_error_handler(
        HTTPStatus.INTERNAL_SERVER_ERROR, handle_internal_server_error
    )
