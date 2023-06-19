import datetime as dt
from dataclasses import dataclass
from typing import Optional

from .resource_saver_mixins import ResourseSaverMixin


@dataclass
class Video(ResourseSaverMixin):
    video_id: str
    video_title: str
    channel_id: str
    video_description: str
    video_thumbnail: str
    video_duration: str
    views_count: int
    likes_count: int
    comments_count: int
    published_at: dt.datetime
    id: Optional[int] = None
