from .base_controller_factory import BaseControllerFactory
from ..data_validators.validator_factory import DataValidatorList
from ...database.request_handler.request_handler_base import RequestHandlerBase
from ...database.request_handler.video_factories import AddVideoSQLiteFactory
from ...database.request_handler.request_handler import RequestHandler

class AddVideoControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)
    
    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = AddVideoSQLiteFactory()
        return RequestHandler(request_handler_factory)