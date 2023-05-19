from dataclasses import dataclass, field
import datetime as dt
from typing import Optional

@dataclass
class User:
    first_name: str
    last_name: str
    email_address: str
    password: str
    date_registered: Optional[dt.datetime] = field(default_factory=dt.datetime.now)
    date_updated: Optional[dt.datetime] = field(default_factory=dt.datetime.now)
    id: Optional[int] = None