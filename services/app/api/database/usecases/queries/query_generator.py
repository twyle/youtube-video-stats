from abc import ABC, abstractmethod
from typing import Any
from .query_builder import QueryBuilderBase


class BaseQueryGenerator(ABC):
    def __init__(self, query_builder: QueryBuilderBase) -> None:
        self.__query_builder = query_builder
        
    @property
    def query_builder(self) -> QueryBuilderBase:
        return self.__query_builder
    
    @abstractmethod
    def __call__(self, query_parameters: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
        pass
    
    
class QueryGenerator(BaseQueryGenerator):        
    def __call__(self, query_parameters: dict[str, dict[str, Any]]) -> str:
        return self.__generate_query(query_parameters)
    
    def __generate_query(self, query_parameters: dict[str, dict[str, Any]]) -> str:
        generated_query = self.query_builder(query_parameters['query'])
        return generated_query[0]
    
    def __validate_query_parameters(self, query_parameters: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
        pass