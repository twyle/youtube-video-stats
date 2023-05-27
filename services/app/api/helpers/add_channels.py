from ..database.models.channel_model import Channel
from ..database.models.video_model import Video
from typing import Optional
import os
import json
from youtube import YouTube
import requests


client_secrets_file = '/home/lyle/Downloads/python_learning_site.json'
youtube = YouTube(client_secrets_file)

def get_video_by_id(video_id: str) -> Video:
    """"Get a video by it's id."""
    video = youtube.find_video_by_id(video_id)
    return video

def get_channel_id_title(video: Video) -> dict[str, str]:
    """Get channel id and title from video."""
    data = {}
    if video:
        data[video.channel_title] = video.channel_id 
    return data

def save_to_channels(video_id: str, file_name: Optional[str] = "kenyan_channels.json") -> None:
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
        if not channel_data in kenyan_channels:
            kenyan_channels.append(channel_data)
        f.write(json.dumps(kenyan_channels, indent=2))
        
def find_channel(channel_id: str) -> Channel:
    """Find a channel with the given id."""
    channel = youtube.find_channel_by_id(channel_id)
    return channel

def post_data(data: dict[str, int|str], url: str) -> dict[str, str]:
    admin_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODU1MjAxOTcsImlhdCI6MTY4NDkxNTM5Nywic3ViIjoyfQ.hne-aXvET8nSwzK1EVtC3-0hPZE_Sa4njp8ZH1u7rkk"
    headers = {"Authorization": f"Bearer {admin_token}"}
    
    resp = requests.post(url, json=data, headers=headers)
    return resp

def add_channel(channel: Channel) -> dict[str, str|int|float]:
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
    data = {
        'channels': channels
    }
    url = 'http://localhost:5000/api/v1/channels/'
    resp = post_data(url=url, data=data)
    print(resp.json())