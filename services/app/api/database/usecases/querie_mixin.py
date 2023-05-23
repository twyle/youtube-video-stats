from .queries.filters import (
    GreaterThanFilter, LessThanFilter
)
from .queries.query_builder import QueryBuilder
from .queries.query_generator import QueryGenerator

filters = [
    GreaterThanFilter(), LessThanFilter()
]

query = """SELECT * FROM videos"""

qr = {
    "query": {
        "comments_count": {
            "gt": 500
        }
    },
    "limit": 100,
    "offset": 10,
    "fields": ["video_title", "video_id", "channel_id"]
}

qb = QueryBuilder(query, filters)
qg = QueryGenerator(qb)

class QueryMixin:
    @staticmethod
    def print_yay():
        print('Yay')
        
    @staticmethod    
    def generate_query():
        r = qg(qr)
        print(r)
        return r