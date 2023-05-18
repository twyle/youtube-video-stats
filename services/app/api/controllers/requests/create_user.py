from .api_request import APIRequest
from ..validators.validator_factory import ValidatorFactory

class CreateUserRequest(APIRequest):        
    def __call__(self, api_request, request_data_validator: ValidatorFactory) -> dict[str, str]:
        registration_data = self.get_request_data(api_request)
        data = request_data_validator.validate(registration_data)
        return data
        
    def get_request_data(self, api_request) -> dict[str, str]:
        form = api_request.form
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