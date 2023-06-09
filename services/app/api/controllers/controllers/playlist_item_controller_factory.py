from ...database.request_handler.playlist_item_factories import (
    AddManyPlaylistItemsSQLiteFactory,
    AddPlaylistItemSQLiteFactory,
    DeletePlaylistItemSQLiteFactory,
    GetPlaylistItemSQLiteFactory,
    GetPlaylistItemsSQLiteFactory,
    QueryPlaylistItemsSQLiteFactory,
    UpdatePlaylistItemSQLiteFactory,
)
from ...database.request_handler.request_handler import RequestHandler
from ...database.request_handler.request_handler_base import RequestHandlerBase
from ..data_validators.validator_factory import DataValidatorList
from .base_controller_factory import BaseControllerFactory


class AddPlaylistItemControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = AddPlaylistItemSQLiteFactory()
        return RequestHandler(request_handler_factory)


class GetPlaylistItemControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = GetPlaylistItemSQLiteFactory()
        return RequestHandler(request_handler_factory)


class UpdatePlaylistItemControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = UpdatePlaylistItemSQLiteFactory()
        return RequestHandler(request_handler_factory)


class DeletePlaylistItemControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = DeletePlaylistItemSQLiteFactory()
        return RequestHandler(request_handler_factory)


class GetPlaylistItemsControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = GetPlaylistItemsSQLiteFactory()
        return RequestHandler(request_handler_factory)


class AddManyPlaylistItemsControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = AddManyPlaylistItemsSQLiteFactory()
        return RequestHandler(request_handler_factory)


class QueryPlaylistItemsControllerFactory(BaseControllerFactory):
    def get_request_data_validator(self) -> DataValidatorList:
        validators = []
        return DataValidatorList(validators)

    def get_request_handler(self) -> RequestHandlerBase:
        request_handler_factory = QueryPlaylistItemsSQLiteFactory()
        return RequestHandler(request_handler_factory)
