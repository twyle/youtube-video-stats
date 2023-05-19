from api.controllers.validators.validator_factory import DataValidatorList, NameValidator


validators = [NameValidator() for _ in range(5)]
val_list = DataValidatorList(validators)
data = {
    'name': 'lyle'
}

if __name__ == '__main__':
    val_list(data)