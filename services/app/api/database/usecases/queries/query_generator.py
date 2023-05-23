from abc import ABC, abstractmethod
from typing import Any
from .query_builder import QueryBuilderBase
from .query_limiters import QueryLimitersBase


class BaseQueryGenerator(ABC):
    def __init__(self, query: str, query_builder: QueryBuilderBase, query_limiter: QueryLimitersBase) -> None:
        self.__query_builder = query_builder
        self.__query = query
        self.__query_limiter = query_limiter
        
    @property
    def query_builder(self) -> QueryBuilderBase:
        return self.__query_builder
    
    @property
    def query(self) -> str:
        return self.__query
    
    @property
    def query_limiter(self) -> QueryLimitersBase:
        return self.__query_limiter
    
    @abstractmethod
    def __call__(self, query_parameters: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
        pass
    
    
class QueryGenerator(BaseQueryGenerator):        
    def __call__(self, query_parameters: dict[str, dict[str, Any]]) -> str:
        return self.__limit_query(query_parameters)
    
    def __generate_query(self, query_parameters: dict[str, dict[str, Any]]) -> str:
        generated_query = self.query_builder(self.query, query_parameters['query'])
        return generated_query[0]
    
    def __limit_query(self, query_parameters: dict[str, dict[str, Any]]) -> str:
        query = self.__generate_query(query_parameters)
        updated_query = self.query_limiter(query, query_parameters)
        return updated_query[0]
    
    def __validate_query_parameters(self, query_parameters: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
        pass