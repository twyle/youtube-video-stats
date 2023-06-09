import datetime as dt
from dataclasses import dataclass, field
from typing import Optional

import jwt
from flask import current_app
from jwt import ExpiredSignatureError, InvalidTokenError

from ...extensions.extensions import bcrypt


@dataclass
class User:
    first_name: str
    last_name: str
    email_address: str
    password: str
    date_registered: Optional[dt.date] = field(default_factory=dt.date.today)
    date_updated: Optional[dt.date] = field(default_factory=dt.date.today)
    id: Optional[int] = None
    account_activated: Optional[int] = 0
    role: Optional[str] = 'user'

    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def encode_auth_token(user_id: int):
        try:
            payload = {
                'exp': dt.datetime.utcnow() + dt.timedelta(days=0, hours=2),
                'iat': dt.datetime.utcnow(),
                'sub': user_id,
            }
            return jwt.encode(payload, current_app.config.get('SECRET_KEY'), algorithm='HS256')
        except Exception as e:
            return e

    @staticmethod
    def generate_admin_token(admin_id: int):
        try:
            payload = {
                'exp': dt.datetime.utcnow() + dt.timedelta(days=7, hours=0),
                'iat': dt.datetime.utcnow(),
                'sub': admin_id,
            }
            return jwt.encode(payload, current_app.config.get('SECRET_KEY'), algorithm='HS256')
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token: str):
        try:
            payload = jwt.decode(auth_token, current_app.config.get('SECRET_KEY'), algorithms='HS256')
            return payload['sub']
        except (ExpiredSignatureError, InvalidTokenError) as e:
            raise e
