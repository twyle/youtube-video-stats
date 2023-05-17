from .controller import Controller
from ..requests.api_request import APIRequest

class RegisterUserController(Controller):  
    def __init__(self, api_request: APIRequest) -> None:
        self.__api_request = api_request
              
    def __call__(self) -> tuple[dict, int]:
        try:
            api_request_data = self.handle_request()
        except ValueError:
            return {'error': 'No such user'}, 404
        else:
            return api_request_data, 201
        
    def handle_request(self) -> tuple[dict, int]:
        api_request_data = self.__api_request()
        return api_request_data