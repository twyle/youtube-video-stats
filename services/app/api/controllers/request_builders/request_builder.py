from ..data_validators.validator_factory import ValidatorList
from flask import Request
from typing import Any
from .request_builder_base import RequestBuilderBase

class RequestBuilder(RequestBuilderBase):        
    def __call__(self, request_object: Request, request_data_validator: ValidatorList) -> dict[str, str]:
        request_data = self.get_request_data(request_object)
        request_data = self.validate_request_data(request_data_validator, request_data)
        return request_data
        
    def get_request_data(self, request_object: Request) -> dict[str, str]:
        request_data = {}
        if request_object.method in ['GET', 'DELETE']:
            request_data = dict(request_object.args)
        elif request_object.method in ['POST', 'PUT']:
            request_data = request_object.json  
            if request_object.args:
                request_data.update(dict(request_object.args))
        return request_data
 
    def validate_request_data(self, request_data_validator: ValidatorList, 
                              request_data: dict[str, Any]) -> dict[str, str]:
        return request_data_validator(request_data)