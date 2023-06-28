from flasgger import swag_from
from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from ...controllers.controllers.video_controller_factory import (
    AddManyVideosControllerFactory,
    AddVideoControllerFactory,
    DeleteVideoControllerFactory,
    GetVideoControllerFactory,
    GetVideosControllerFactory,
    QueryVideosControllerFactory,
    UpdateVideoControllerFactory,
)
from ...controllers.response_builders.create_response import ResponseBuilder
from ..decorators import admin_token_required
from ..flow import flow

videos = Blueprint("videos", __name__)


@videos.route("/video", methods=["POST"])
@admin_token_required
@swag_from("./docs/add.yml", endpoint="videos.add", methods=["POST"])
def add():
    controller = AddVideoControllerFactory()
    return flow(controller)


@videos.route("/", methods=["POST"])
@admin_token_required
@swag_from("./docs/add_many.yml", endpoint="videos.add_many", methods=["POST"])
def add_many():
    controller = AddManyVideosControllerFactory()
    return flow(controller)


@videos.route("/video", methods=["GET"])
@jwt_required()
@swag_from("./docs/get.yml", endpoint="videos.get", methods=["GET"])
def get():
    controller = GetVideoControllerFactory()
    return flow(controller)


@videos.route("/video", methods=["PUT"])
@admin_token_required
@swag_from("./docs/update.yml", endpoint="videos.update", methods=["PUT"])
def update():
    controller = UpdateVideoControllerFactory()
    return flow(controller)


@videos.route("/video", methods=["DELETE"])
@admin_token_required
@swag_from("./docs/delete.yml", endpoint="videos.delete", methods=["DELETE"])
def delete():
    controller = DeleteVideoControllerFactory()
    return flow(controller)


@videos.route("/", methods=["GET"])
@jwt_required()
@swag_from("./docs/videos.yml", endpoint="videos.list_all", methods=["GET"])
def list_all():
    controller = GetVideosControllerFactory()
    return flow(controller)


@videos.route("/advanced", methods=["POST"])
@jwt_required()
@swag_from("./docs/advanced_search.yml", endpoint="videos.advanced_search", methods=["POST"])
def advanced_search():
    controller = QueryVideosControllerFactory()
    return flow(controller)


@videos.route("/video/comments", methods=["GET"])
@jwt_required()
@swag_from("./docs/comments.yml", endpoint="videos.get_video_comments", methods=["GET"])
def get_video_comments():
    """Get the comments for a particular video."""
    return "Video Comments."
