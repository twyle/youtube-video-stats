from dataclasses import dataclass
from typing import Optional
import datetime as dt

@dataclass
class Video:
    video_id: str
    video_title: str
    channel_title: str 
    video_description: str
    video_thumbnail: str
    video_duration: str
    views_count: int
    likes_count: int
    date_published: dt.date
    comments_count: int
    id: Optional[int] = None
    