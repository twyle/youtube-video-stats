from .validator import DataValidator

class NameValidator(DataValidator):
    def __init__(self, next_validator: DataValidator, attr: str) -> None:
        self.__next_validator = next_validator
        self.__attr = attr
        
    def __call__(self, data: dict) -> dict:
        self.validate(data)
        if self.__next_validator:
            self.__next_validator(data)
        return data
    
    def validate(self, data: dict) -> dict:
        print(f'Validating {self.__attr} name')
        
        
class EmailValidator(DataValidator):
    def __init__(self, next_validator: DataValidator) -> None:
        self.__next_validator = next_validator
        
    def __call__(self, data: dict) -> dict:
        self.validate(data)
        if self.__next_validator:
            self.__next_validator(data)
        return data
    
    def validate(self, data: dict) -> dict:
        print('Validating email')
        
        
class PasswordValidator(DataValidator):
    def __init__(self, next_validator: DataValidator) -> None:
        self.__next_validator = next_validator
        
    def __call__(self, data: dict) -> dict:
        self.validate(data)
        if self.__next_validator:
            self.__next_validator(data)
        return data
    
    def validate(self, data: dict) -> dict:
        print('Validating password')
        
        
class PasswordMatchValidator(DataValidator):
    def __init__(self, next_validator: DataValidator) -> None:
        self.__next_validator = next_validator
        
    def __call__(self, data: dict) -> dict:
        self.validate(data)
        if self.__next_validator:
            self.__next_validator(data)
        return data
    
    def validate(self, data: dict) -> dict:
        print('Validating that passwords match')
        raise ValueError('The passwords do not match.')