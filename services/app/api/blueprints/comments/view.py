from flasgger import swag_from
from flask import Blueprint, request

from ...controllers.controllers.comment_controller_factory import (
    AddCommentControllerFactory,
    AddManyCommentsControllerFactory,
    DeleteCommentControllerFactory,
    GetCommentControllerFactory,
    GetCommentsControllerFactory,
    QueryCommentsControllerFactory,
    UpdateCommentControllerFactory,
)
from ...controllers.response_builders.create_response import ResponseBuilder
from ..flow import flow

comments = Blueprint("comments", __name__)


@swag_from("./docs/add.yml", endpoint="comments.add", methods=["POST"])
@comments.route("/comment", methods=["POST"])
def add():
    controller = AddCommentControllerFactory()
    return flow(controller)


@swag_from("./docs/update.yml", endpoint="comments.update", methods=["PUT"])
@comments.route("/comment", methods=["PUT"])
def update():
    controller = UpdateCommentControllerFactory()
    return flow(controller)


@swag_from("./docs/delete.yml", endpoint="comments.delete", methods=["DELETE"])
@comments.route("/comment", methods=["DELETE"])
def delete():
    controller = DeleteCommentControllerFactory()
    return flow(controller)


@swag_from("./docs/get.yml", endpoint="comments.get", methods=["GET"])
@comments.route("/comment", methods=["GET"])
def get():
    controller = GetCommentControllerFactory()
    return flow(controller)


@comments.route("/", methods=["POST"])
# @admin_token_required
@swag_from("./docs/add_many.yml", endpoint="comments.add_many", methods=["POST"])
def add_many():
    controller = AddManyCommentsControllerFactory()
    return flow(controller)


@swag_from("./docs/comments.yml", endpoint="comments.list_all_comments", methods=["GET"])
@comments.route("/", methods=["GET"])
def list_all_comments():
    controller = GetCommentsControllerFactory()
    return flow(controller)


@swag_from("./docs/videos.yml", endpoint="comments.video_comments", methods=["GET"])
@comments.route("/video/", methods=["GET"])
def video_comments():
    controller = QueryCommentsControllerFactory()
    return flow(controller)


@swag_from("./docs/channels.yml", endpoint="channels.channel_channels", methods=["GET"])
@comments.route("/channel/", methods=["GET"])
def channel_channels():
    return "channel channels"
