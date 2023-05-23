from .base_controller import BaseController
from ..request_builders.request_builder import RequestBuilder
from ..data_validators.validator_factory import ValidatorList
from flask import Request
from ...database.request_handler.request_handler import RequestHandler
from ...exceptions.exceptions import (
    VideoExistsException, VideoDoesNotExistException, UserExistsException, UserDoesNotExistException
)

class Controller(BaseController):                     
    def __call__(self, request_builder: RequestBuilder, data_validators: ValidatorList, 
                 request_object: Request, request_handler: RequestHandler) -> tuple[dict, int]:
        try:
            api_request_data = self.handle_request(request_builder, data_validators, 
                                request_object, request_handler)
        except (VideoExistsException, UserExistsException) as e:
            return {'Error': str(e)}, 409
        except (VideoDoesNotExistException, UserDoesNotExistException) as e:
            return {'Error': str(e)}, 404
        else:
            return api_request_data, 201
        
    def handle_request(self, request_builder: RequestBuilder, data_validators: ValidatorList, 
                 request_object: Request, request_handler: RequestHandler) -> tuple[dict, int]:
        api_request_data = request_builder(request_object, data_validators)
        data = request_handler(api_request_data)
        return data