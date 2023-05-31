from dataclasses import dataclass
from typing import Optional


@dataclass
class CommentAuthor:
    author_display_name: str
    author_profile_image_url: str
    author_channel_url: str
    author_channel_id: str
    author_id: Optional[int] = None