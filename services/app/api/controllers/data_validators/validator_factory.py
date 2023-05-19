from typing import Any, Optional
from ..data_validators.validator import DataValidator
from abc import ABC, abstractmethod
    
class ValidatorList(ABC):
    @abstractmethod
    def add_validator(self, validator: DataValidator) -> None:
        pass
    
    @abstractmethod
    def remove_validator(self, validator: DataValidator) -> DataValidator:
        pass
    
    @abstractmethod
    def insert_validator(self, existing_validator: DataValidator, new_validator: DataValidator) -> None:
        pass
    
    @abstractmethod
    def __call__(self, data: dict[str, Any]) -> dict[str, Any]:
        pass
        
class DataValidatorList(ValidatorList):
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
            return self.__first_validator(data) 
        return data

