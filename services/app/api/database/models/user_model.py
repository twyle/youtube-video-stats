from dataclasses import dataclass
import datetime as dt

@dataclass
class User:
    first_name: str
    last_name: str
    email_address: str
    password: str
    date_registered: dt.datetime
    date_updated: dt.datetime