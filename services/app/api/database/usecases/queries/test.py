from filters import (
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
from query_builder import QueryBuilder
from query_generator import QueryGenerator

q_p = {
    'comments_count': {'eq': 100},
    'likes_count': {'lte': 100},
    'views_count': {'gte': 100},
    'date': {'lt': '2023-05-23', 'gt': '2023-05-15'},
    'id': {'not in': [1, 2, 3, 4]},
}

q = """SELECT * FROM videos"""

eq = EqualFilter()
gt = GreaterThanFilter(next_filter=eq)
lt = LessThanFilter(next_filter=gt)
gte = GreaterThanEqualToFilter(next_filter=lt)
lte = LessThanEqualToFilter(next_filter=gte)
btw = BetweenFilter(next_filter=lte)
lt_gt = LessThanGreaterThanFilter(next_filter=btw)
in_f = InFilter(next_filter=lt_gt)
not_in = NotInFilter(next_filter=in_f)

q_filters = [EqualFilter(), GreaterThanEqualToFilter(), NotInFilter()]
qb = QueryBuilder(q, q_filters)

qg = QueryGenerator(qb)

qr = {
    'query': {'comments_count': {'gt': 500}},
    'limit': 100,
    'offset': 10,
    'fields': ['video_title', 'video_id', 'channel_id'],
}

if __name__ == '__main__':
    r = qg(qr)
    print(r)
