from .base_controller_factory import BaseControllerFactory
from ..data_validators.validator_factory import DataValidatorList
from ...database.request_handler.request_handler_base import RequestHandlerBase
from ...database.request_handler.channel_factories import (
    AddChannelSQLiteFactory, GetChannelSQLiteFactory, UpdateChannelSQLiteFactory, 
    DeleteChannelSQLiteFactory, GetChannelsSQLiteFactory, AddManyChannelsSQLiteFactory,
    QueryChannelsSQLiteFactory
)
from ...database.request_handler.request_handler import RequestHandler

class AddChannelControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = AddChannelSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
    
class GetChannelControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = GetChannelSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
class UpdateChannelControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = UpdateChannelSQLiteFactory()
        return RequestHandler(request_handler_factory)
    

class DeleteChannelControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = DeleteChannelSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
class GetChannelsControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = GetChannelsSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
class AddManyChannelsControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = AddManyChannelsSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
class QueryChannelsControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = QueryChannelsSQLiteFactory()
        return RequestHandler(request_handler_factory)