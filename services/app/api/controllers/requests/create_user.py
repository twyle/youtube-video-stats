from .api_request import APIRequest
from ..validators.validator_factory import CreateUserValidator

class CreateUserRequest(APIRequest):
    def __init__(self, api_request) -> None:
        self.__api_request = api_request
        
    def __call__(self) -> dict[str, str]:
        registration_data = self.get_request_data()
        create_user_validator = CreateUserValidator()
        data = create_user_validator.validate(registration_data)
        return data
        
    def get_request_data(self) -> dict[str, str]:
        form = self.__api_request.form
        first_name = form.get('First Name', '')
        last_name = form.get('Last Name', '')
        email_address = form.get('Email Address', '')
        password = form.get('Password')
        confirm_password = form.get('Confirm Password', '')
        registration_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email_address': email_address,
            'password': password,
            'confirm_password': confirm_password
        }
        return registration_data
 
    def validate_request_data(self) -> dict[str, str]:
        pass