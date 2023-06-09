from typing import Any

from .queries.filters import (
    BetweenFilter,
    EqualFilter,
    GreaterThanEqualToFilter,
    GreaterThanFilter,
    InFilter,
    LessThanEqualToFilter,
    LessThanFilter,
    LessThanGreaterThanFilter,
    NotInFilter,
)
from .queries.limiter import FieldLimiter, LimitLimiter, OffsetLimiter, SortLimiter
from .queries.query_builder import QueryBuilder
from .queries.query_generator import QueryGenerator
from .queries.query_limiters import QueryLimiters


class QueryMixin:
    @staticmethod
    def generate_query(data: dict[str, dict[str, Any]]):
        query = """SELECT * FROM playlists"""
        filters = QueryMixin.generate_filters()
        query_builder = QueryBuilder(filters)
        limiters = QueryMixin.generate_limiters()
        query_limiter = QueryLimiters(limiters)
        query_generator = QueryGenerator(query, query_builder, query_limiter)
        generated_query = query_generator(data)
        print(generated_query)
        return generated_query

    @staticmethod
    def generate_filters():
        return [
            GreaterThanFilter(),
            LessThanFilter(),
            GreaterThanEqualToFilter(),
            LessThanEqualToFilter(),
            LessThanGreaterThanFilter(),
            BetweenFilter(),
            InFilter(),
            NotInFilter(),
            EqualFilter(),
        ]

    @staticmethod
    def generate_limiters():
        return [SortLimiter(), LimitLimiter(), OffsetLimiter(), FieldLimiter()]
