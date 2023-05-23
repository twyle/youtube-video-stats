from abc import ABC, abstractmethod
from typing import Optional, Any
from .filter import Filter

class QueryBuilderBase(ABC):
    def __init__(self, query: str, query_filters: Optional[list[Filter]] = []) -> None:
        self.__query = query
        self.__query_filters = query_filters
        
    @property
    def query(self) -> str:
        return self.__query
    
    @query.setter
    def query(self, query: str) -> None:
        self.__query = query
        
    @abstractmethod    
    def add_filter(self, query_filter: Filter) -> None:
        pass
    
    @abstractmethod
    def __call__(self, query_parameters: dict[str, dict[str, Any]]) -> str:
        pass
    
class QueryBuilder(QueryBuilderBase):
    def __init__(self, query: str, query_filters: Optional[list[Filter]] = []) -> None:
        super().__init__(query, query_filters)
        self.__first_filter = None
        if query_filters:
            for query_filter in query_filters:
                self.add_filter(query_filter)
           
    def add_filter(self, query_filter: Filter) -> None:
        if not self.__first_filter:
            self.__first_filter = query_filter
        else:
            current_filter = self.__first_filter
            while current_filter.next_filter:
                next_filter = current_filter.next_filter
                current_filter = next_filter
            current_filter.next_filter = query_filter
    
    def __call__(self, query_parameters: dict[str, dict[str, Any]]) -> str:
        if self.__first_filter:
            return self.__first_filter(self.query, query_parameters)
        return self.query, query_parameters