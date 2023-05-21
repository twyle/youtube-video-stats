from .data_validators.validator_factory import DataValidatorList
from .request_builders.request_builder import RequestBuilder
from ..database.request_handler.request_handler import RequestHandler
from .request_builders.list_channels_request_builder import ListChannelsRequestBuilder
from ..database.request_handler.request_handler import RequestHandler
from ..database.request_handler.request_handler_factories import CreateUserSQLiteFactory, ListChannelsSQLiteFactory
from .controllers.controller import Controller
from .controllers.list_channels_controller import ListChannelsController

class ListChannelsControllerFactory:
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
        
    def get_request_builder(self) -> RequestBuilder:
        return ListChannelsRequestBuilder()
        
    def get_request_handler(self) -> RequestHandler:
        request_handler_factory = ListChannelsSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
    def get_controller(self) -> Controller:
        return ListChannelsController()