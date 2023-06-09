import datetime as dt
from dataclasses import dataclass
from typing import Optional

from .resource_saver_mixins import ResourseSaverMixin


@dataclass
class Playlist(ResourseSaverMixin):
    playlist_id: str
    published_at: dt.datetime
    channel_id: str
    playlist_title: str
    playlist_description: str
    playlist_thumbnail: str
    privacy_status: Optional[str] = "public"
    videos_count: Optional[int] = 0
    id: Optional[int] = -1
