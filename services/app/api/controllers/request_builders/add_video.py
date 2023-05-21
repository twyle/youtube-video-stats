from .request_builder import RequestBuilder
from ..data_validators.validator_factory import ValidatorList
from flask import Request
from typing import Any

class AddVideoRequestBuilder(RequestBuilder):        
    def __call__(self, request_object: Request, request_data_validator: ValidatorList) -> dict[str, str]:
        video_data = self.get_request_data(request_object)
        video_data = self.validate_request_data(request_data_validator, video_data)
        return video_data
        
    def get_request_data(self, request_object: Request) -> dict[str, str]:
        video_data = request_object.json
        return video_data
 
    def validate_request_data(self, request_data_validator: ValidatorList, 
                              video_data: dict[str, Any]) -> dict[str, str]:
        return request_data_validator(video_data)