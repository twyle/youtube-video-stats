from contextlib import contextmanager
import sqlite3
from ..repositories.sqlite_repository import SQLiteUserRepository
from ..repositories.user_unit_of_work import UserUnitOfWork
from ..usecases.create_user import CreateUserUseCase
from ..models.user_model import User

@contextmanager
def create_database_connection():
    db_connection = sqlite3.connect('data.db')
    try:
        yield db_connection
    finally:
        db_connection.close()
        
def main():        
    with create_database_connection() as conn:
        user_repository = SQLiteUserRepository(conn)
        unit_of_work = UserUnitOfWork(conn, user_repository)
        create_use_case = CreateUserUseCase(unit_of_work)
        new_user = User(
            first_name='lyle',
            last_name='okoth',
            email_address='lyle@gmail.com',
            password='password'
        )
        user = create_use_case.execute(new_user)
    print(user)