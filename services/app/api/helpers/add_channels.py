"""This module enables the addition of data to database.

The function in this module allows for the addition of resource data to the database using
the ``youtube`` library. This starts with obtaining the given resource from the Google 
API and then passing in the resource to the appropriate route.

Examples:
    To get a YouTube Video's data::
        $ get_video_by_id(video_id='9mdadNspP_M')
        
    To save the YouTube Video to database, you make a ``POST`` request to the video endpoint 
    i.e '/api/v1/video`` passing in the video data::
    
        $ post_data(data={}, url='http://flask.localhost/api/v1/video)
        
    To save a YouTube Channels's data to database::
    
        $ add_channel_playlists('UC5WVOSvL9bc6kwCMXXeFLLw')
        
Args:
    client_secrets_file (str): This string represents the path to the clients' secret file 
        downloaded from Google API. It contains the authentication details for accessing the 
        YouTube API.
    admin_token (str): The administrator token. This token enables you to create resources.
    youtube (youtube.YouTube): The YouTube instance that provides the methods for interacting 
        with the YouTube API.
        
@Author: Lyle Okoth
@Date: 28/06/2023
@Portfolio: https://lyleokoth.oryks-sytem.com
"""

import json
import os
from datetime import datetime
from typing import Iterator, Optional, TypeAlias, Union

import requests
from dotenv import load_dotenv
from requests import Response
from youtube import YouTube
from youtube.models.channel_model import Channel
from youtube.models.comment_model import Comment, CommentAuthor
from youtube.models.comment_thread_model import VideoCommentThread
from youtube.models.playlist_item_model import PlaylistItem
from youtube.models.playlist_model import Playlist
from youtube.models.video_model import Video as YouTubeVideo

load_dotenv()

client_secrets_file = os.environ["SECRET_FILE"]
admin_token = os.environ["ADMIN_TOKEN"]
youtube = YouTube(client_secrets_file)
youtube.authenticate()


def get_video_by_id(video_id: str) -> YouTubeVideo:
    """Get a video by it's id.

    Parameters
    ----------
    video_id: str
        The id of the video whos details you want. This is the part of the url
        after the v in any YouTube Video url i.e 'https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11463s'
        the video id is 'oBt53YbR9Kk'.

    Returns
    -------
    video: YouTubeVideo
        A YouTube Video instance containing the YouTube Video details.
    """
    video = youtube.find_video_by_id(video_id)
    return video


def get_channel_id_title(video: YouTubeVideo) -> dict[str, str]:
    """Get channel id and title from a YouTube Video instnace.

    Given a YouTube Video instance, this method gets the channel title and id.

    Parameters
    ----------
    video: YouTubeVideo
        The YouTube Video instance.

    Returns
    -------
    data: dict[str, str]
        A dictionary with string keys and values. Contains two values, the channel title
        and the channel id.
    """
    data = {}
    if video:
        data[video.channel_title] = video.channel_id
    return data


def save_to_channels(video_id: str, file_name: Optional[str] = "kenyan_channels.json") -> None:
    """Save channel id and title to file.

    Fetches a videos details from Youtube, then gets the channel id and title and saves
    these details to file incase they don't exist.

    Parameters
    ----------
    video_id: str
        The id of the video whose channel details you want i.e '9mdadNspP_M'
    file_name: optional, str
        The path to save the channel details. The default is 'kenyan_channels.json'.
    """
    kenyan_channels = []
    # Get the video details
    video = get_video_by_id(video_id)
    if os.path.exists(file_name):
        # Load the existing channel data
        with open(file_name, "r", encoding="utf-8") as f:
            # Handle the JSONDecodeError that is raised if the file is empty.
            try:
                kenyan_channels = json.loads(f.read())
            except json.decoder.JSONDecodeError:
                pass
    # Add the new channel details and save the file.
    with open(file_name, "w", encoding="utf-8") as f:
        channel_data: dict[str, str] = get_channel_id_title(video)
        if channel_data not in kenyan_channels:
            kenyan_channels.append(channel_data)
        f.write(json.dumps(kenyan_channels, indent=2))


def find_channel(channel_id: str) -> Channel:
    """Find a channel with the given id.

    Parameters
    ----------
    channel_id: str
        The id of the channel whose details you want. You get this id from a YouTube Video object.

    Returns
    -------
    channel: Channel
        A Channel instance with the YouTube Channel details.
    """
    channel = youtube.find_channel_by_id(channel_id)
    return channel


ResourceType: TypeAlias = Union[int, str, datetime, float]


# flake8: noqa: E501
def post_data(data: dict[str, ResourceType], url: str) -> Response:
    """Post data to the API.

    This function sends data to the API. It gets the admin token from the environment
    and uses the requests library to send a POST request to the appropriate endpoint.

    Parameters
    ----------
    data: dict[str, ResourceType]:
        A dictionary containing the resource details. The Resource can be a Video, Channel, Playlist,
        Comment or Comment Author.
    url: str
        The API endpoint that the resource is to be added to.

    Returns
    -------
    requests.Response:
        A Response object containing the API response data.

    Raises
    ------
    KeyError:
        If the ADMIN_TOKEN environment variable is not set.
    """
    headers = {"Authorization": f"Bearer {admin_token}"}

    resp: Response = requests.post(url, json=data, headers=headers)
    return resp


def add_channel(channel: Channel) -> Response:
    """Add a single channel to the database.

    When called with a valid Channel instance, it adds the channel to database by sending a POST request
    to the channel's endpoint.

    Parameters
    ----------
    channel: Channel
        A channel instance.

    Returns
    -------
    requests.Response:
        A Response object containing the API response data.
    """
    url: str = "http://localhost:5000/api/v1/channels/channel"
    data = {}
    if channel:
        data = channel.to_dict()
    resp: Response = post_data(url=url, data=data)
    return resp


def load_channels(file: str) -> list[str]:
    """Load channel ids.

    Loads the channel ids from a json file.

    Parameters
    ----------
    file: str
        The path to the json file containing the channel ids.

    Returns
    -------
    channel_ids: list[str]
        A list of channel ids.
    """
    channel_ids: list[str] = []
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            channel_list: list[dict[str, str]] = json.loads(f.read())
            for data in channel_list:
                channel_ids.append(list(data.values())[0])
    return channel_ids


# TODO(lyle okoth) : Use Async operations to add channels
def create_channels(file: str) -> None:
    """Create the channels.

    Adds a list of channels to the database. It takes in a file path, loads
    the channel ids and for each channel, fetches the channel details and adds the details to the
    database.

    Parameters
    ----------
    file: str
        Path to the json file containing a list of channel ids.
    """
    channel_ids: list[str] = load_channels(file)
    channels: list[dict[str, ResourceType]] = []
    for channel_id in channel_ids:
        channel: Channel = find_channel(channel_id)
        channels.append(channel.to_dict())
    data: dict[str, dict[str, ResourceType]] = {"channels": channels}
    url = "http://localhost:5000/api/v1/channels/"
    resp: Response = post_data(url=url, data=data)
    print(resp.json())


def get_channel_playlists(channel_id: str) -> list[Playlist]:
    """Get a channels playlists.

    This function fetches all the playlists for a given channel.

    Parameters
    ----------
    channel_id: str
        The id of the channel whose playlists you want.

    Returns
    -------
    playlists: list[Playlist]
        A list of Playlist instances belonging to a given channel.
    """
    playlists: list[Playlist] = youtube.find_channel_playlists(channel_id)
    return playlists


def add_many_channels(channel_ids: list[str]) -> None:
    """Add many channels to the API in a single request.

    Parameters
    ----------
    channel_ids: list[str]
        A list of channel ids
    """
    channels = youtube.find_channel_by_id(channel_ids)
    # Check if the API could only find a single channel, then turn it into a list
    if not isinstance(channels, list):
        channels = [channels]
    data: dict[str, list[dict[str, ResourceType]]] = {"channels": [channel.to_dict() for channel in channels]}
    url = "http://localhost:5000/api/v1/channels/"
    resp: Response = post_data(url=url, data=data)
    print(resp.json())


def add_many_videos(video_ids: list[str]) -> None:
    """Add many channels to the API in a single request.

    Parameters
    ----------
    videos_ids: list[str]
        A list of video ids.
    """
    videos: list[YouTubeVideo] = youtube.find_video_by_id(video_ids)
    data: dict[str, list[dict[str, ResourceType]]] = {"videos": [video.to_dict() for video in videos]}
    url = "http://localhost:5000/api/v1/videos/"
    resp: Response = post_data(url=url, data=data)
    print(resp.json())


def add_playlist(playlist: Playlist) -> None:
    """Add a single playlist to database.

    Parameters
    ----------
    playlist: Playlist
        A Playlist instance.
    """
    url = "http://localhost:5000/api/v1/playlists/playlist"
    resp: Response = post_data(url=url, data=playlist.to_dict())
    print(resp.json())


def add_many_playlist_items(playlist_items: list[PlaylistItem]) -> None:
    """Add many playlist items to the database in a single request.

    playlist_items: list[PlaylistItem]:
        A list of PlaylistItem instances.
    """
    data: dict[str, list[dict[str, ResourceType]]] = {"playlist_items": [pl.to_dict() for pl in playlist_items]}
    url = "http://localhost:5000/api/v1/playlist_items/"
    resp: Response = post_data(url=url, data=data)
    print(resp.json())


def get_video_comments(video_id: str) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Get a videos comments and their authors.

    This function fetches the comments posted to a video as well as the details of the
    people who posted the comments.

    Parameters
    ----------
    video_id: str
        The id of the video.

    Returns
    -------
    tuple[list[dict[str, str]], list[dict[str, str]]]:
        This is a tuple of two lists, one containing the authors and the other containing the
        comments.
    """
    search_iterator: Iterator = youtube.find_video_comments(video_id, max_results=5)
    video_comment_threads: list[VideoCommentThread] = list(next(search_iterator))
    authors: list[dict[str, str]] = []
    comments: list[dict[str, str]] = []
    for video_comment_thread in video_comment_threads:
        comment: Comment = video_comment_thread.top_level_comment.comment
        author: CommentAuthor = video_comment_thread.top_level_comment.comment.comment_author
        authors.append(author.to_dict())
        video_comment: dict[str, str] = comment.to_dict()
        comments.append(video_comment)
    return authors, comments


def add_palylist_items(playlist: Playlist) -> None:
    """Add playlist items to database.

    This function adds all the playlist items for a given playlist to the database.
    It first adds all the channel details, followed by the videos, then the playlists
    and finally the playlist items. This is due to the relationships that exist between the various
    entities.

    Parameters
    ----------
    playlist: Playlist
        The Playlist instance to add to the database.
    """
    playlist_id: str = playlist.playlist_id
    playlist_items: list[PlaylistItem] = list(next(youtube.find_playlist_items(playlist_id, max_results=25)))
    channel_ids: list[str] = []
    video_ids: list[str] = []
    for playlist_item in playlist_items:
        if playlist_item.video_owner_channel_id not in channel_ids:
            channel_ids.append(playlist_item.video_owner_channel_id)
        if playlist_item.channel_adder_id not in channel_ids:
            channel_ids.append(playlist_item.channel_adder_id)
        if playlist_item.video_id not in video_ids:
            video_ids.append(playlist_item.video_id)

    add_many_channels(channel_ids)
    add_many_videos(video_ids)
    add_playlist(playlist)
    add_many_playlist_items(playlist_items)


def add_channel_playlists(channel_id: str) -> None:
    """Add the a channel's playlists to database.

    This function will add all the resources associated with a given
    channels playlists to the database. This includes the videos, comments and
    playlist items associated with the given playlist.

    Parameters
    ----------
    channel_id: str
        The channel id whose details you want to add to the API.
    """
    playlists: list[Playlist] = get_channel_playlists(channel_id)
    for playlist in playlists:
        add_palylist_items(playlist)
