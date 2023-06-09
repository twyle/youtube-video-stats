import datetime as dt
from dataclasses import dataclass
from typing import Optional

from .resource_saver_mixins import ResourseSaverMixin


@dataclass
class Comment(ResourseSaverMixin):
    video_id: str
    comment_id: str
    comment_text: str
    parent_id: str
    like_count: int
    published_at: dt.datetime
    updated_at: dt.datetime
    id: Optional[int] = None
