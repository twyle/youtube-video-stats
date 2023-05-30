from dataclasses import dataclass
import datetime as dt
from typing import Optional
from .resource_saver_mixins import ResourseSaverMixin


@dataclass
class PlaylistItemModel(ResourseSaverMixin):
    playlist_item_id: str
    date_added: dt.datetime
    channel_adder_id: str
    video_owner_channel_id: str
    playlist_id: str
    position: int
    video_id: str
    privacy_status: str
    id: Optional[int] = -1