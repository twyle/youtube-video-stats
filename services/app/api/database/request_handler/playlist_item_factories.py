from .sqlite_request_handler import SQLiteRequestHandlerFactory
from ..repositories.sqlite_playlist_item_repository import SQLitePlaylistItemRepository
from ..repositories.base_repository import BaseRepository
from ..usecases.use_case import UseCase
from ..usecases.playlist_item_usecases import (
    AddPlaylistItemUseCase, GetPlaylistItemUseCase, UpdatePlaylistItemUseCase, DeletePlaylistItemUseCase, 
    GetPlaylistItemsUseCase, AddManyPlaylistItemsUseCase, QueryPlaylistItemUseCase
)
from ..models.playlist_item_model import PlaylistItemModel

class PlaylistItemSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[PlaylistItemModel]:
        return SQLitePlaylistItemRepository()    
    
    
class AddPlaylistItemSQLiteFactory(PlaylistItemSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return AddPlaylistItemUseCase()    
    

class GetPlaylistItemSQLiteFactory(PlaylistItemSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return GetPlaylistItemUseCase()
    
class UpdatePlaylistItemSQLiteFactory(PlaylistItemSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return UpdatePlaylistItemUseCase()
    
class DeletePlaylistItemSQLiteFactory(PlaylistItemSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return DeletePlaylistItemUseCase() 
    
class GetPlaylistItemsSQLiteFactory(PlaylistItemSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return GetPlaylistItemsUseCase() 
    
class AddManyPlaylistItemsSQLiteFactory(PlaylistItemSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return AddManyPlaylistItemsUseCase() 
    
class QueryPlaylistItemsSQLiteFactory(PlaylistItemSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return QueryPlaylistItemUseCase() 