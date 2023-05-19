from api.controllers.validators.validator_factory import DataValidatorList
from api.controllers.validators.data_validators import NameValidator


validators = [NameValidator() for _ in range(10)]
val_list = DataValidatorList(validators)
data = {
    'name': 'lyle'
}

if __name__ == '__main__':
    val_list(data)