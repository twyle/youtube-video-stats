from flasgger import swag_from
from flask import Blueprint, request

from ...controllers.controllers.playlist_controller_factory import (
    AddManyPlaylistsControllerFactory,
    AddPlaylistControllerFactory,
    DeletePlaylistControllerFactory,
    GetPlaylistControllerFactory,
    GetPlaylistsControllerFactory,
    QueryPlaylistsControllerFactory,
    UpdatePlaylistControllerFactory,
)
from ...controllers.response_builders.create_response import ResponseBuilder
from ..flow import flow

playlists = Blueprint("playlists", __name__)


@swag_from("./docs/add.yml", endpoint="playlists.add", methods=["POST"])
@playlists.route("/playlist", methods=["POST"])
def add():
    controller = AddPlaylistControllerFactory()
    return flow(controller)


@swag_from("./docs/update.yml", endpoint="playlists.update", methods=["PUT"])
@playlists.route("/playlist", methods=["PUT"])
def update():
    controller = UpdatePlaylistControllerFactory()
    return flow(controller)


@swag_from("./docs/delete.yml", endpoint="playlists.delete", methods=["DELETE"])
@playlists.route("/playlist", methods=["DELETE"])
def delete():
    controller = DeletePlaylistControllerFactory()
    return flow(controller)


@swag_from("./docs/get.yml", endpoint="playlists.get", methods=["GET"])
@playlists.route("/playlist", methods=["GET"])
def get():
    controller = GetPlaylistControllerFactory()
    return flow(controller)


@playlists.route("/", methods=["POST"])
# @admin_token_required
@swag_from("./docs/add_many.yml", endpoint="playlists.add_many", methods=["POST"])
def add_many():
    controller = AddManyPlaylistsControllerFactory()
    return flow(controller)


@swag_from("./docs/playlists.yml", endpoint="playlists.list_all_playlists", methods=["GET"])
@playlists.route("/", methods=["GET"])
def list_all_playlists():
    controller = GetPlaylistsControllerFactory()
    return flow(controller)


@swag_from("./docs/channel.yml", endpoint="playlists.channel_playlists", methods=["GET"])
@playlists.route("/channel/", methods=["GET"])
def channel_playlists():
    controller = QueryPlaylistsControllerFactory()
    return flow(controller)


@swag_from("./docs/playlist_videos.yml", endpoint="playlists.videos", methods=["GET"])
@playlists.route("/playlist/videos", methods=["GET"])
def videos():
    return "Playlist Videos"
