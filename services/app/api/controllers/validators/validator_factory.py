from typing import Protocol
from .data_validators import (
    NameValidator, EmailValidator, PasswordValidator, PasswordMatchValidator
)

class ValidatorFactory(Protocol):
    def validate(self, data: dict) -> dict:
        ...
        

class CreateUserValidator:
    def validate(self, data: dict) -> dict:
        password_match = PasswordMatchValidator(None)
        password_validator = PasswordValidator(password_match)
        email_validator = EmailValidator(password_validator)
        last_name_validator = NameValidator(email_validator, 'last_name')
        first_name_validator = NameValidator(last_name_validator, 'first_name')
        return first_name_validator(data)