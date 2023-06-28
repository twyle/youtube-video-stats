from functools import wraps
from typing import Any

from flask import current_app, jsonify, make_response, request
from jwt import ExpiredSignatureError, InvalidTokenError, decode

from ..database.models.user_model import User
from ..database.request_handler.user_factories import GetUserSQLiteFactory


def get_user(data: dict[str, Any]) -> User:
    sqlite_factory = GetUserSQLiteFactory()
    connection = sqlite_factory.get_database_connection()
    unit_of_work = sqlite_factory.get_unit_of_work()
    use_case = sqlite_factory.get_use_case()
    repository = sqlite_factory.get_repository()
    with connection() as conn:
        repository.connection = conn
        unit_of_work.connection = conn
        unit_of_work.repository = repository
        use_case.unit_of_work = unit_of_work
        user = use_case.execute(data)
    return user


# Authentication decorator
def admin_token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        # ensure the jwt-token is passed with the headers
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split()[1]
        if not token:  # throw error if no token provided
            return make_response(jsonify({"message": "A valid admin token is missing!"}), 401)
        try:
            # decode the token to obtain user public_id
            data = decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            user_data = {"user_id": data["sub"]}
            admin = get_user(user_data)
            if not admin["role"] == "admin":
                return make_response(jsonify({"message": "A valid admin token is missing!"}), 401)
        except (ExpiredSignatureError, InvalidTokenError) as e:
            return make_response(jsonify({"message": str(e)}), 401)
        # Return the user information attached to the token
        return f(*args, **kwargs)

    return decorator
