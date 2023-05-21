from .controller import Controller
from ..request_builders.request_builder import RequestBuilder
from ..data_validators.validator_factory import ValidatorList
from flask import Request
from ...database.request_handler.request_handler import RequestHandler

class AddVideoController(Controller):                     
    def __call__(self, request_builder: RequestBuilder, data_validators: ValidatorList, 
                 request_object: Request, request_handler: RequestHandler) -> tuple[dict, int]:
        try:
            api_request_data = self.handle_request(request_builder, data_validators, 
                                request_object, request_handler)
        except ValueError:
            return {'error': 'No such user'}, 404
        else:
            return api_request_data, 201
        
    def handle_request(self, request_builder: RequestBuilder, data_validators: ValidatorList, 
                 request_object: Request, request_handler: RequestHandler) -> tuple[dict, int]:
        api_request_data = request_builder(request_object, data_validators)
        data = request_handler(api_request_data)
        return data