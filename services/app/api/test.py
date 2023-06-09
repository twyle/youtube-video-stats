from database.usecases.queries.limiter import FieldLimiter, LimitLimiter, OffsetLimiter, SortLimiter
from database.usecases.queries.query_limiters import QueryLimiters

limiters = [SortLimiter(), LimitLimiter(), OffsetLimiter(), FieldLimiter()]

query = 'SELECT * FROM videos'

data = {
    'fields': ['video_id', 'video_title', 'channel_title'],
    'limit': 20,
    'offset': 20,
    'query': {'comments_count': {'gt': 500}},
    'sort': {'fileds': ['comments_count', 'likes_count'], 'order': 'asc'},
}

ql = QueryLimiters(limiters)

if __name__ == '__main__':
    r = ql(query, data)
    print(r[0])
