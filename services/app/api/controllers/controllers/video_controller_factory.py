from ...database.request_handler.request_handler import RequestHandler
from ...database.request_handler.request_handler_base import RequestHandlerBase
from ...database.request_handler.video_factories import (
    AddManyVideosSQLiteFactory,
    AddVideoSQLiteFactory,
    DeleteVideoSQLiteFactory,
    GetVideoSQLiteFactory,
    GetVideosSQLiteFactory,
    QueryVideosSQLiteFactory,
    UpdateVideoSQLiteFactory,
)
from ..data_validators.validator_factory import DataValidatorList
from .base_controller_factory import BaseControllerFactory


class AddVideoControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = AddVideoSQLiteFactory()
        return RequestHandler(request_handler_factory)


class GetVideoControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = GetVideoSQLiteFactory()
        return RequestHandler(request_handler_factory)


class UpdateVideoControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = UpdateVideoSQLiteFactory()
        return RequestHandler(request_handler_factory)


class DeleteVideoControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = DeleteVideoSQLiteFactory()
        return RequestHandler(request_handler_factory)


class GetVideosControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = GetVideosSQLiteFactory()
        return RequestHandler(request_handler_factory)


class AddManyVideosControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = AddManyVideosSQLiteFactory()
        return RequestHandler(request_handler_factory)


class QueryVideosControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = QueryVideosSQLiteFactory()
        return RequestHandler(request_handler_factory)
