from typing import TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar('T')

class BaseRepository(ABC, Generic[T]):
    "A base class for repositories."
    
    @abstractmethod
    def add(self, item: T) -> T:
        """Add a new item to a repository."""
        raise NotImplementedError()
    
    @abstractmethod
    def update(self, item: T) -> T:
        """Update an existing item in the repository."""
        raise NotImplementedError()
    
    @abstractmethod
    def delete(self, item_id: int) -> T:
        """Delete an existing item from the repository."""
        raise NotImplementedError()
    
    @abstractmethod
    def get_by_id(self, item_id: int) -> T:
        """Retrieve an item by its id from the repository."""
        raise NotImplementedError()