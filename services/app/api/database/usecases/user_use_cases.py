from ..repositories.unit_of_work import BaseUnitfWork
from ..models.user_model import User
from typing import Optional, Any
import dataclasses
from .use_case import UseCase
from flask import jsonify, current_app
from jwt import ExpiredSignatureError, InvalidTokenError
from flask_jwt_extended import create_access_token, create_refresh_token

class CreateUserUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            user = User(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email_address=data['email_address'],
                password=User.hash_password(data['password'])
            )
            uow.repository.add(user)
        activation_token = User.encode_auth_token(user.id)
        data = {
            'user': dataclasses.asdict(user),
            'activation_token': activation_token
        }
        return data
    

class GetUserUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            user_id = data['user_id']
            user = uow.repository.get_by_id(user_id)
        return dataclasses.asdict(user)
    
class DeleteUserUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            user_id = data['user_id']
            user = uow.repository.get_by_id(user_id) 
            uow.repository.delete(user_id)
        return dataclasses.asdict(user)
    

class UpdateUserUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            user_id = data['user_id']
            user = uow.repository.get_by_id(user_id)
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            if data.get('last_name'):
                user.last_name = data.get('last_name')
            if data.get('email_address'):
                user.email_address = data.get('email_address')
            uow.repository.update(user)
        return dataclasses.asdict(user)
    
    
class GetAllUsersUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            users = uow.repository.list_all()
        return jsonify(users)
    
class ActivateUserUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        exct = None
        with self.unit_of_work as uow:
            user_id = data['user_id']
            user = uow.repository.get_by_id(user_id)
            try:
                user_identity = User.decode_auth_token(data['activation_token'])
            except (ExpiredSignatureError, InvalidTokenError) as e:
                uow.repository.delete(user_id)
                exct = e
            else:
                if not int(user_id) == int(user_identity):
                    raise InvalidTokenError()
                user.account_activated = 1
                uow.repository.update(user)
        if exct:
            raise exct
        return {'Success': 'Account Activated',
                'data': dataclasses.asdict(user)}
        
class LoginUserUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            user_email = data['email_address']
            user = uow.repository.get_by_email(user_email)
            if not user.account_activated:
                raise ValueError('The user account has not been activated.')
            if not user.check_password(data['password']):
                raise ValueError('Invalid email address or password.')
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
        

class CreateAdminUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)
        
    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            user = User(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email_address=data['email_address'],
                password=User.hash_password(data['password']),
                role='admin',
                account_activated=1
            )
            uow.repository.add(user)
        activation_token = User.generate_admin_token(user.id)
        data = {
            'admin': dataclasses.asdict(user),
            'admin_token': activation_token
        }
        return data