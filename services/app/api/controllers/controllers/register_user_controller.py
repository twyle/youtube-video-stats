from .controller import Controller
from ..requests.api_request import APIRequest
from ..validators.validator_factory import ValidatorFactory

class RegisterUserController(Controller):  
    def __init__(self, api_request: APIRequest, request_data_val: ValidatorFactory, request_object) -> None:
        self.__api_request = api_request
        self.__request_data_val = request_data_val
        self.__request_object = request_object
                    
    def __call__(self) -> tuple[dict, int]:
        try:
            api_request_data = self.handle_request()
        except ValueError:
            return {'error': 'No such user'}, 404
        else:
            return api_request_data, 201
        
    def handle_request(self) -> tuple[dict, int]:
        api_request_data = self.__api_request(self.__request_object, self.__request_data_val)
        return api_request_data