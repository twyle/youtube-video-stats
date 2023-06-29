import dataclasses
from typing import Any, Optional

from flask import current_app, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from jwt import ExpiredSignatureError, InvalidTokenError

from ..connections import create_sqlite_database_connection
from ..models.user_model import User
from ..repositories.allowed_admins_repository import SQLiteAllowedAdminRepository
from ..repositories.unit_of_work import BaseUnitfWork, UnitOfWork
from .use_case import UseCase


class CheckAdminEmailUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            email_address = data["email_address"]
            allowed_email = uow.repository.get_by_email(email_address)
        return True if allowed_email else False


def check_admin_email(data: dict[str, Any]) -> bool:
    """Check if admin email is allowed."""
    uow = UnitOfWork()
    repo = SQLiteAllowedAdminRepository()
    usecase = CheckAdminEmailUseCase()
    with create_sqlite_database_connection() as conn:
        repo.connection = conn
        uow.connection = conn
        uow.repository = repo
        usecase.unit_of_work = uow
        allowed_admin_email = usecase.execute(data)
    return allowed_admin_email


class CreateAdminUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            if check_admin_email(data):
                user = User(
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    email_address=data["email_address"],
                    password=User.hash_password(data["password"]),
                    role="admin",
                    account_activated=1,
                )
                uow.repository.add(user)
                registration_data = {"admin": dataclasses.asdict(user)}
            else:
                registration_data = {"error": f'Email {data["email_address"]} cannot register as an admin.'}
        return jsonify(registration_data)


class LoginAdminUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            user_email = data["email_address"]
            user = uow.repository.get_by_email(user_email)
            if not user.check_password(data["password"]):
                raise ValueError("Invalid email address or password.")
        access_token = User.generate_admin_token(user.id)
        return jsonify({"access_token": access_token})
