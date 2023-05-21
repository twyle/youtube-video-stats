from .request_builder import RequestBuilder
from ..data_validators.validator_factory import ValidatorList
from flask import Request
from typing import Any

class ListChannelsRequestBuilder(RequestBuilder):        
    def __call__(self, request_object: Request, request_data_validator: ValidatorList) -> dict[str, str]:
        registration_data = self.get_request_data(request_object)
        data = self.validate_request_data(request_data_validator, registration_data)
        return data
        
    def get_request_data(self, request_object: Request) -> dict[str, str]:
        return {}
 
    def validate_request_data(self, request_data_validator: ValidatorList, registration_data: dict[str, Any]) -> dict[str, str]:
        return request_data_validator(registration_data)