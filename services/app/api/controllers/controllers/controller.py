from .base_controller import BaseController
from ..request_builders.request_builder import RequestBuilder
from ..data_validators.validator_factory import ValidatorList
from flask import Request
from ...database.request_handler.request_handler import RequestHandler
from ...exceptions.exceptions import (
    ResourceExistsException, ResourceNotExistException
)
from jwt import ExpiredSignatureError, InvalidTokenError
from http import HTTPStatus

class Controller(BaseController):                     
    def __call__(self, request_builder: RequestBuilder, data_validators: ValidatorList, 
                 request_object: Request, request_handler: RequestHandler) -> tuple[dict, int]:
        try:
            api_request_data = self.handle_request(request_builder, data_validators, 
                                request_object, request_handler)
        except ResourceExistsException as e:
            return {'Error': str(e)}, HTTPStatus.CONFLICT
        except ResourceNotExistException as e:
            return {'Error': str(e)}, HTTPStatus.NOT_FOUND
        except ValueError as e:
            return {'Error': str(e)}, 404
        # except KeyError as e:
        #     return {'Error': f'The key {str(e)} is not allowed for this route.'}, HTTPStatus.NOT_FOUND
        else:
            return api_request_data, 201
        
    def handle_request(self, request_builder: RequestBuilder, data_validators: ValidatorList, 
                 request_object: Request, request_handler: RequestHandler) -> tuple[dict, int]:
        api_request_data = request_builder(request_object, data_validators)
        data = request_handler(api_request_data)
        return data