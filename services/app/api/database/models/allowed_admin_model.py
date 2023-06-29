from dataclasses import dataclass
from typing import Optional


@dataclass
class AllowedAdmin:
    email_address: str
    id: Optional[int] = None
