from .sqlite_request_handler import SQLiteRequestHandlerFactory
from ..repositories.sqlite_playlist_repository import SQLitePlaylistRepository
from ..repositories.base_repository import BaseRepository
from ..usecases.use_case import UseCase
from ..usecases.playlist_usecases import (
    AddPlaylistUseCase, GetPlaylistUseCase, UpdatePlaylistUseCase, DeletePlaylistUseCase, 
    GetPlaylistsUseCase, AddManyPlaylistsUseCase, QueryPlaylistUseCase
)
from ..models.playlist_model import Playlist

class PlaylistSQLiteFactory(SQLiteRequestHandlerFactory):
    def get_repository(self) -> BaseRepository[Playlist]:
        return SQLitePlaylistRepository()    
    
    
class AddPlaylistSQLiteFactory(PlaylistSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return AddPlaylistUseCase()    
    

class GetPlaylistSQLiteFactory(PlaylistSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return GetPlaylistUseCase()
    
class UpdatePlaylistSQLiteFactory(PlaylistSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return UpdatePlaylistUseCase()
    
class DeletePlaylistSQLiteFactory(PlaylistSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return DeletePlaylistUseCase() 
    
class GetPlaylistsSQLiteFactory(PlaylistSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return GetPlaylistsUseCase() 
    
class AddManyPlaylistsSQLiteFactory(PlaylistSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return AddManyPlaylistsUseCase() 
    
class QueryPlaylistsSQLiteFactory(PlaylistSQLiteFactory):    
    def get_use_case(self) -> UseCase:
        return QueryPlaylistUseCase() 