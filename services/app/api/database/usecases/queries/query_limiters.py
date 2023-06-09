from abc import ABC, abstractmethod
from typing import Any, Optional

from .limiter import Limiter


class QueryLimitersBase(ABC):
    def __init__(self, limiters: Optional[list[Limiter]]) -> None:
        self.__first_limiter = None
        if limiters:
            for limiter in limiters:
                self.add_limiter(limiter)

    @property
    def first_limiter(self) -> Limiter:
        return self.__first_limiter

    @first_limiter.setter
    def first_limiter(self, limiter: Limiter) -> None:
        self.__first_limiter = limiter

    def add_limiter(self, limiter: Limiter) -> None:
        if not self.first_limiter:
            self.first_limiter = limiter
        else:
            current_limiter = self.first_limiter
            while current_limiter.next_limiter:
                next_limiter = current_limiter.next_limiter
                current_limiter = next_limiter
            current_limiter.next_limiter = limiter

    @abstractmethod
    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        pass


class QueryLimiters(QueryLimitersBase):
    def __init__(self, limiters: list[Limiter] | None) -> None:
        super().__init__(limiters)

    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        if self.first_limiter:
            return self.first_limiter(query, query_parameters)
        return query, query_parameters
