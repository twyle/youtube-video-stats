from .base_controller_factory import BaseControllerFactory
from ..data_validators.validator_factory import DataValidatorList
from ...database.request_handler.request_handler_base import RequestHandlerBase
from ...database.request_handler.comment_factories import (
    AddCommentSQLiteFactory, GetCommentSQLiteFactory, UpdateCommentSQLiteFactory, 
    DeleteCommentSQLiteFactory, GetCommentsSQLiteFactory, AddManyCommentsSQLiteFactory,
    QueryCommentsSQLiteFactory
)
from ...database.request_handler.request_handler import RequestHandler

class AddCommentControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = AddCommentSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
    
class GetCommentControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = GetCommentSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
class UpdateCommentControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = UpdateCommentSQLiteFactory()
        return RequestHandler(request_handler_factory)
    

class DeleteCommentControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = DeleteCommentSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
class GetCommentsControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = GetCommentsSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
class AddManyCommentsControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = AddManyCommentsSQLiteFactory()
        return RequestHandler(request_handler_factory)
    
class QueryCommentsControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = QueryCommentsSQLiteFactory()
        return RequestHandler(request_handler_factory)