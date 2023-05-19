from typing import Any, Protocol, Optional
from .data_validators import (EmailValidator, NameValidator, PasswordValidator, PasswordMatchValidator)
from ..validators.validator import DataValidator

class ValidatorFactory(Protocol):
    def validate(self, data: dict) -> dict:
        ...
        
class DataValidatorList:
    def __init__(self, data_validators: Optional[list[DataValidator]]) -> None:
        self.__first_validator = None
        for validator in data_validators:
            self.add_validator(validator)
        
    def add_validator(self, validator: DataValidator) -> None:
        if not self.__first_validator:
            self.__first_validator = validator
        else:
            current = self.__first_validator
            while current.next_validator:
                next_validator = current.next_validator
                current = next_validator
            current.next_validator = validator
    
    def remove_validator(self, validator: DataValidator) -> DataValidator:
        pass
    
    def insert_validator(self, existing_validator: DataValidator, new_validator: DataValidator) -> None:
        pass
    
    def __call__(self, data: dict) -> dict:
        if self.__first_validator:
            self.__first_validator(data) 
class CreateUserValidator:
    def validate(self, data: dict) -> dict:
        password_match = PasswordMatchValidator(None)
        password_validator = PasswordValidator(password_match)
        email_validator = EmailValidator(password_validator)
        last_name_validator = NameValidator(email_validator, 'last_name')
        first_name_validator = NameValidator(last_name_validator, 'first_name')
        return first_name_validator(data)

