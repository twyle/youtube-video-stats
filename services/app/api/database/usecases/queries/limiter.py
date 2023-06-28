from abc import ABC, abstractmethod
from typing import Any, Optional


class Limiter(ABC):
    def __init__(self, next_limiter: Optional[Any] = None) -> None:
        self.__next_limiter = next_limiter

    @property
    def next_limiter(self) -> None:
        return self.__next_limiter

    @next_limiter.setter
    def next_limiter(self, limiter: Any) -> None:
        self.__next_limiter = limiter

    @abstractmethod
    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        pass


class LimitLimiter(Limiter):
    def __init__(self, next_limiter: Any | None = None) -> None:
        super().__init__(next_limiter)

    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        limit = query_parameters.get("limit", 10)
        updated_query = query + f" LIMIT {limit}"
        if self.next_limiter:
            return self.next_limiter(updated_query, query_parameters)
        return updated_query, query_parameters


class OffsetLimiter(Limiter):
    def __init__(self, next_limiter: Any | None = None) -> None:
        super().__init__(next_limiter)

    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        offset = query_parameters.get("offset", 0)
        updated_query = query + f" OFFSET {offset}"
        if self.next_limiter:
            return self.next_limiter(updated_query, query_parameters)
        return updated_query, query_parameters


class FieldLimiter(Limiter):
    def __init__(self, next_limiter: Any | None = None) -> None:
        super().__init__(next_limiter)

    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        fields = "*"
        if query_parameters.get("fields"):
            fields = ", ".join(query_parameters.get("fields"))
        updated_query = query.replace("*", fields)
        if self.next_limiter:
            return self.next_limiter(updated_query, query_parameters)
        return updated_query, query_parameters


class SortLimiter(Limiter):
    def __init__(self, next_limiter: Any | None = None) -> None:
        super().__init__(next_limiter)

    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        field = "id"
        order = "ASC"
        if query_parameters.get("sort"):
            field = query_parameters["sort"]["field"]
            order = query_parameters["sort"]["order"]
        updated_query = query + f" ORDER BY {field} {order}"
        if self.next_limiter:
            return self.next_limiter(updated_query, query_parameters)
        return updated_query, query_parameters
