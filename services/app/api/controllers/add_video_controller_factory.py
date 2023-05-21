from .data_validators.validator_factory import DataValidatorList
from .request_builders.request_builder import RequestBuilder
from ..database.request_handler.request_handler import RequestHandler
from ..database.request_handler.request_handler import RequestHandler
from .controllers.controller import Controller
from .request_builders.add_video import AddVideoRequestBuilder
from ..database.request_handler.request_handler_factories import AddVideoSQLiteFactory
from .controllers.add_video_controller import AddVideoController

class AddVideoControllerFactory:
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
        
    def get_request_builder(self) -> RequestBuilder:
        return AddVideoRequestBuilder()
        
    def get_request_handler(self) -> RequestHandler:
        request_handler_factory = AddVideoSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
    def get_controller(self) -> Controller:
        return AddVideoController()