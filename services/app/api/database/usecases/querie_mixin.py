from .queries.filters import (
    GreaterThanFilter, LessThanFilter, InFilter, NotInFilter, GreaterThanEqualToFilter,
    LessThanEqualToFilter, LessThanGreaterThanFilter, BetweenFilter
)
from .queries.query_builder import QueryBuilder
from .queries.query_generator import QueryGenerator
from typing import Any
from .queries.limiter import (
    LimitLimiter, OffsetLimiter, FieldLimiter, SortLimiter
)
from .queries.query_limiters import QueryLimiters

qr = {
    "query": {
        "comments_count": {
            "gt": 500
        },
        "id": {
            "not in": [10, 13, 14, 16]
        },
        "views_count": {
            "gt": 500
        }
    },
    "limit": 100,
    "offset": 10,
    "fields": ["video_title", "video_id", "channel_id"]
}

class QueryMixin:       
    @staticmethod    
    def generate_query(data: dict[str, dict[str, Any]]):
        query = """SELECT * FROM videos"""
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
            NotInFilter()
        ]
        
    @staticmethod
    def generate_limiters():
        return [
            SortLimiter(),
            LimitLimiter(),
            OffsetLimiter(),
            FieldLimiter()
        ]