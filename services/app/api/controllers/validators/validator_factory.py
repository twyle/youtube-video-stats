from typing import Any, Protocol, Optional
from .data_validators import (EmailValidator, NameValidator, PasswordValidator, PasswordMatchValidator)
from ..validators.validator import DataValidator

class ValidatorFactory(Protocol):
    def validate(self, data: dict) -> dict:
        ...
        
class DataValidatorList:
    def __init__(self, data_validators: Optional[list[DataValidator]]) -> None:
        self.__validators = []
        
    def add_validator(self, validator: DataValidator) -> None:
        pass
    
    def remove_validator(self, validator: DataValidator) -> DataValidator:
        pass
    
    def insert_validator(self, existing_validator: DataValidator, new_validator: DataValidator) -> None:
        pass
    
    def __call__(self) -> dict:
        pass
class CreateUserValidator:
    def validate(self, data: dict) -> dict:
        password_match = PasswordMatchValidator(None)
        password_validator = PasswordValidator(password_match)
        email_validator = EmailValidator(password_validator)
        last_name_validator = NameValidator(email_validator, 'last_name')
        first_name_validator = NameValidator(last_name_validator, 'first_name')
        return first_name_validator(data)

