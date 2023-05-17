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
        email_validator = EmailValidator(password_match)
        name_validator = NameValidator(email_validator)
        data = name_validator(data)