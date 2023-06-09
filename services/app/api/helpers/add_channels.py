import json
import os
from typing import Iterator, Optional

import requests
from youtube import YouTube
from youtube.models.comment_model import Comment, CommentAuthor
from youtube.models.comment_thread_model import CommentThread, VideoComment, VideoCommentThread

from ..database.models.channel_model import Channel
from ..database.models.playlist_item_model import PlaylistItemModel
from ..database.models.playlist_model import Playlist
from ..database.models.video_model import Video

client_secrets_file = '/home/lyle/Downloads/python_learning_site.json'
youtube = YouTube(client_secrets_file)


def get_video_by_id(video_id: str) -> Video:
    """ "Get a video by it's id."""
    video = youtube.find_video_by_id(video_id)
    return video


def get_channel_id_title(video: Video) -> dict[str, str]:
    """Get channel id and title from video."""
    data = {}
    if video:
        data[video.channel_title] = video.channel_id
    return data


def save_to_channels(video_id: str, file_name: Optional[str] = 'kenyan_channels.json') -> None:
    """Save channel id and title to file."""
    kenyan_channels = []
    video = get_video_by_id(video_id)
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            try:
                kenyan_channels = json.loads(f.read())
            except json.decoder.JSONDecodeError:
                pass
    with open(file_name, 'w', encoding='utf-8') as f:
        channel_data: dict[str, str] = get_channel_id_title(video)
        if channel_data not in kenyan_channels:
            kenyan_channels.append(channel_data)
        f.write(json.dumps(kenyan_channels, indent=2))


def find_channel(channel_id: str) -> Channel:
    """Find a channel with the given id."""
    channel = youtube.find_channel_by_id(channel_id)
    return channel


# flake8: noqa: E501
def post_data(data: dict[str, int | str], url: str) -> dict[str, str]:
    admin_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODU1MjAxOTcsImlhdCI6MTY4NDkxNTM5Nywic3ViIjoyfQ.hne-aXvET8nSwzK1EVtC3-0hPZE_Sa4njp8ZH1u7rkk'
    headers = {'Authorization': f'Bearer {admin_token}'}

    resp = requests.post(url, json=data, headers=headers)
    return resp


def add_channel(channel: Channel) -> dict[str, str | int | float]:
    """Add a single channel to the database."""
    url = 'http://localhost:5000/api/v1/channels/channel'
    data = {}
    if channel:
        data = channel.to_dict()
    resp = post_data(url=url, data=data)
    return resp


def load_channels(file: str) -> list[str]:
    """Load channel ids."""
    channel_ids: list[str] = []
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            channel_list: list[dict[str, str]] = json.loads(f.read())
            for data in channel_list:
                channel_ids.append(list(data.values())[0])
    return channel_ids


def create_channels(file: str) -> None:
    """Create the channels."""
    channel_ids = load_channels(file)
    channels = []
    for channel_id in channel_ids:
        channel = find_channel(channel_id)
        channels.append(channel.to_dict())
    data = {'channels': channels}
    url = 'http://localhost:5000/api/v1/channels/'
    resp = post_data(url=url, data=data)
    print(resp.json())


def get_channel_playlists(channel_id: str) -> list[Playlist]:
    """Get a channels playlists."""
    playlists = youtube.find_channel_playlists(channel_id)
    return playlists


def add_many_channels(channel_ids: list[str]) -> None:
    """Add many channels."""
    channels = youtube.find_channel_by_id(channel_ids)
    if not isinstance(channels, list):
        channels = [channels]
    data = {'channels': [channel.to_dict() for channel in channels]}
    # print(data)
    url = 'http://localhost:5000/api/v1/channels/'
    resp = post_data(url=url, data=data)
    print(resp.json())


def add_many_videos(video_ids: list[str]) -> None:
    """Add many videos."""
    videos: list[Video] = youtube.find_video_by_id(video_ids)
    data = {'videos': [video.to_dict() for video in videos]}
    # print(data)
    url = 'http://localhost:5000/api/v1/videos/'
    resp = post_data(url=url, data=data)
    print(resp.json())


def add_playlist(playlist: Playlist) -> None:
    """Add a single playlist."""
    # print(playlist.to_dict())
    url = 'http://localhost:5000/api/v1/playlists/playlist'
    resp = post_data(url=url, data=playlist.to_dict())
    print(resp.json())


def add_many_playlist_items(playlist_items: PlaylistItemModel) -> None:
    """Add many playlist items."""
    data: dict[str, list[dict[str, str | int]]] = {'playlist_items': [pl.to_dict() for pl in playlist_items]}
    # print(data)
    url = 'http://localhost:5000/api/v1/playlist_items/'
    resp = post_data(url=url, data=data)
    print(resp.json())


def get_video_comments(video_id: str) -> list[dict[str, int | str]]:
    """Get a videos comments."""
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
        # video_comment = {
        #     'video_id': video_comment_thread.video_id,
        #     'author_display_name': author.author_display_name,
        #     'author_profile_image_url': author.author_profile_image_url,
        #     'author_channel_url': author.author_channel_url,
        #     'author_channel_id': author.author_channel_id,
        #     'comment_id': comment.comment_id,
        #     'comment_text': comment.text_display,
        #     'like_count': comment.like_count,
        #     'published_at': comment.published_at,
        #     'updated_at': comment.updated_at,
        #     'parent_id': comment.parent_id
        # }
    print(authors)
    print(comments)


def add_palylist_items(playlist: Playlist) -> None:
    """Add playlist items."""
    playlist_id: str = playlist.playlist_id
    playlist_items: list[PlaylistItemModel] = list(next(youtube.find_playlist_items(playlist_id, max_results=25)))
    channel_ids = []
    video_ids = []
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
    """Add the channels playlists."""
    playlists = get_channel_playlists(channel_id)
    for playlist in playlists:
        add_palylist_items(playlist)
