from .sqlite_request_handler import SQLiteRequestHandlerFactory
from ..repositories.sqlite_channel_repository import SQLiteChannelRepository
from ..repositories.base_repository import BaseRepository
from ..usecases.use_case import UseCase
from ..usecases.channel_usecases import (
    AddChannelUseCase, GetChannelUseCase, UpdateChannelUseCase, DeleteChannelUseCase, 
    GetChannelsUseCase, AddManyChannelsUseCase, QueryChannelUseCase
)
from ..models.channel_model import Channel

class ChannelSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[Channel]:
        return SQLiteChannelRepository()    
    
    
class AddChannelSQLiteFactory(ChannelSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return AddChannelUseCase()    
    

class GetChannelSQLiteFactory(ChannelSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return GetChannelUseCase()
    
class UpdateChannelSQLiteFactory(ChannelSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return UpdateChannelUseCase()
    
class DeleteChannelSQLiteFactory(ChannelSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return DeleteChannelUseCase() 
    
class GetChannelsSQLiteFactory(ChannelSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return GetChannelsUseCase() 
    
class AddManyChannelsSQLiteFactory(ChannelSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return AddManyChannelsUseCase() 
    
class QueryChannelsSQLiteFactory(ChannelSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return QueryChannelUseCase() 