from flasgger import swag_from
from flask import Blueprint
from flask_jwt_extended import jwt_required

from ...controllers.controllers.channel_controller_factory import (
    AddChannelControllerFactory,
    AddManyChannelsControllerFactory,
    DeleteChannelControllerFactory,
    GetChannelControllerFactory,
    GetChannelsControllerFactory,
    QueryChannelsControllerFactory,
    UpdateChannelControllerFactory,
)
from ..decorators import admin_token_required
from ..flow import flow

channels = Blueprint("channels", __name__)


@channels.route("/channel", methods=["POST"])
@admin_token_required
@swag_from("./docs/add.yml", endpoint="channels.add", methods=["POST"])
def add():
    controller = AddChannelControllerFactory()
    return flow(controller)


@channels.route("/channel", methods=["PUT"])
@admin_token_required
@swag_from("./docs/update.yml", endpoint="channels.update", methods=["PUT"])
def update():
    controller = UpdateChannelControllerFactory()
    return flow(controller)


@channels.route("/channel", methods=["DELETE"])
@admin_token_required
@swag_from("./docs/delete.yml", endpoint="channels.delete", methods=["DELETE"])
def delete():
    controller = DeleteChannelControllerFactory()
    return flow(controller)


@channels.route("/channel", methods=["GET"])
@admin_token_required
@swag_from("./docs/get.yml", endpoint="channels.get", methods=["GET"])
def get():
    controller = GetChannelControllerFactory()
    return flow(controller)


@channels.route("/", methods=["POST"])
@admin_token_required
@swag_from("./docs/add_many.yml", endpoint="channels.add_many", methods=["POST"])
def add_many():
    controller = AddManyChannelsControllerFactory()
    return flow(controller)


@channels.route("/", methods=["GET"])
@jwt_required()
@swag_from("./docs/channels.yml", endpoint="channels.list_all_channels", methods=["GET"])
def list_all_channels():
    controller = GetChannelsControllerFactory()
    return flow(controller)


@channels.route("/channel/videos", methods=["GET"])
@jwt_required()
@swag_from("./docs/add.yml", endpoint="channels.channel_Channels", methods=["GET"])
def channel_videos():
    return "Channel Videos"


@channels.route("/channel/playlists", methods=["GET"])
@jwt_required()
@swag_from("./docs/videos.yml", endpoint="channels.channel_playlists", methods=["GET"])
def channel_playlists():
    controller = QueryChannelsControllerFactory()
    return flow(controller)


@channels.route("/channel/comments", methods=["GET"])
@jwt_required()
@swag_from("./docs/add.yml", endpoint="channels.channel_comments", methods=["GET"])
def channel_comments():
    return "Channel Comments"
