from abc import ABC, abstractmethod
from typing import Any

from flask import Request

from ..data_validators.validator_factory import ValidatorList


class RequestBuilderBase(ABC):
    @abstractmethod
    def __call__(self, request_object: Request, request_data_validator: ValidatorList) -> dict[str, str]:
        pass

    @abstractmethod
    def get_request_data(self) -> dict[str, str]:
        pass

    @abstractmethod
    def validate_request_data(self) -> dict[str, str]:
        pass
