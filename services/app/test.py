from api.controllers.validators.validator_factory import DataValidatorList
from api.controllers.validators.data_validators import (
    NameValidator, EmailValidator, PasswordValidator, PasswordMatchValidator
    )


validators = [
    NameValidator(attr='first_name'),
    NameValidator(attr='last_name'),
    EmailValidator(),
    PasswordValidator(),
    PasswordMatchValidator()
]
val_list = DataValidatorList(validators)
data = {
    'name': 'lyle'
}

if __name__ == '__main__':
    val_list(data)