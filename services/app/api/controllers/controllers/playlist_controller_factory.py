from .base_controller_factory import BaseControllerFactory
from ..data_validators.validator_factory import DataValidatorList
from ...database.request_handler.request_handler_base import RequestHandlerBase
from ...database.request_handler.playlist_factories import (
    AddPlaylistSQLiteFactory, GetPlaylistSQLiteFactory, UpdatePlaylistSQLiteFactory, 
    DeletePlaylistSQLiteFactory, GetPlaylistsSQLiteFactory, AddManyPlaylistsSQLiteFactory,
    QueryPlaylistsSQLiteFactory
)
from ...database.request_handler.request_handler import RequestHandler

class AddPlaylistControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = AddPlaylistSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
    
class GetPlaylistControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = GetPlaylistSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
class UpdatePlaylistControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = UpdatePlaylistSQLiteFactory()
        return RequestHandler(request_handler_factory)
    

class DeletePlaylistControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = DeletePlaylistSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
class GetPlaylistsControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = GetPlaylistsSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
class AddManyPlaylistsControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = AddManyPlaylistsSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
class QueryPlaylistsControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = QueryPlaylistsSQLiteFactory()
        return RequestHandler(request_handler_factory)