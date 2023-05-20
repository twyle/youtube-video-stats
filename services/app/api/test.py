from database.builder.user_builder import  get_user, update_user
from database.connections import create_sqlite_database_connection
from database.builder.user_builder import CreateUserRequestHandler
from database.models.user_model import User


request_handler = CreateUserRequestHandler(create_sqlite_database_connection)
new_user = User(
    first_name='lyle',
    last_name='okoth',
    email_address='lyle@gmail.com',
    password='password'
)


if __name__ == '__main__':
    request_handler(new_user)
    # update_user()
    # get_user()