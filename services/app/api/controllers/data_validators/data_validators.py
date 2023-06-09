from typing import Optional

from .validator import DataValidator


class NameValidator(DataValidator):
    def __init__(self, next_validator: Optional[DataValidator] = None, attr: Optional[str] = '') -> None:
        self.__next_validator = next_validator
        self.__attr = attr

    def __call__(self, data: dict) -> dict:
        self.validate(data)
        if self.__next_validator:
            self.__next_validator(data)
        return data

    @property
    def next_validator(self) -> DataValidator:
        return self.__next_validator

    @next_validator.setter
    def next_validator(self, next_validator: DataValidator):
        self.__next_validator = next_validator

    def validate(self, data: dict) -> dict:
        print(f'Validating {self.__attr} name')


class EmailValidator(DataValidator):
    def __init__(self, next_validator: Optional[DataValidator] = None, attr: Optional[str] = '') -> None:
        self.__next_validator = next_validator
        self.__attr = attr

    def __call__(self, data: dict) -> dict:
        self.validate(data)
        if self.__next_validator:
            self.__next_validator(data)
        return data

    @property
    def next_validator(self) -> DataValidator:
        return self.__next_validator

    @next_validator.setter
    def next_validator(self, next_validator: DataValidator):
        self.__next_validator = next_validator

    def validate(self, data: dict) -> dict:
        print('Validating email')


class PasswordValidator(DataValidator):
    def __init__(self, next_validator: Optional[DataValidator] = None, attr: Optional[str] = '') -> None:
        self.__next_validator = next_validator
        self.__attr = attr

    def __call__(self, data: dict) -> dict:
        self.validate(data)
        if self.__next_validator:
            self.__next_validator(data)
        return data

    @property
    def next_validator(self) -> DataValidator:
        return self.__next_validator

    @next_validator.setter
    def next_validator(self, next_validator: DataValidator):
        self.__next_validator = next_validator

    def validate(self, data: dict) -> dict:
        print('Validating password')


class PasswordMatchValidator(DataValidator):
    def __init__(self, next_validator: Optional[DataValidator] = None, attr: Optional[str] = '') -> None:
        self.__next_validator = next_validator
        self.__attr = attr

    def __call__(self, data: dict) -> dict:
        self.validate(data)
        if self.__next_validator:
            self.__next_validator(data)
        return data

    @property
    def next_validator(self) -> DataValidator:
        return self.__next_validator

    @next_validator.setter
    def next_validator(self, next_validator: DataValidator):
        self.__next_validator = next_validator

    def validate(self, data: dict) -> dict:
        print('Validating that passwords match')
        # raise ValueError('The passwords do not match.')
