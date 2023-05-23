from faker import Faker
import random
from typing import Any
import requests

fake = Faker()
def generate_data():
    data = {
        'video_id': fake.sbn9(),
        'video_title': fake.text(),
        'channel_title': fake.text(),
        'video_description': fake.text(),
        'video_thumbnail': fake.url(),
        'video_duration': '',
        'views_count': random.randint(0, 1000),
        'likes_count': random.randint(0, 1000),
        'comments_count': random.randint(0,1000),
        'date_published': fake.date()
    }
    return data

def post_data():
    url = 'http://localhost:5000/videos/'

    videos = {
        'videos': [
            generate_data() for _ in range(150)
        ]
    }
    
    resp = requests.post(url, json=videos)
    if resp.ok:
        print(resp.json())
    else:
        print(resp.json())
        
q = {
    "query": {
        "likes_count": {
            "gte": 500,
            "lte": 1000
        }
    },
    "limit": 10,
    "offset": 10,
    "sort": {
        "field": "id",
        "order": 'ASC'
    }
}
    
data = {
    "likes_count": {
        "gt": 12,
        "lt": 20
    },
    "comments_count": {
        "eq": 100
    },
    "views_count": {
        "lte": 100,
        "gte": 5
    }
}        
def generate_query(data: dict[str, dict[str, Any]]):
    operator_map = {
        'gt': '>',
        'gte': '>=',
        'lt': '<',
        "eq": "=",
        "lte": "<="
    }
    q = ""
    query = data["query"]
    for field, query_parameters in query.items():
        operators_values = list(query_parameters.items())
        for operator, value in operators_values:
            if not q:
                q = f'SELECT * FROM videos WHERE {field} {operator_map[operator]} {value}'
            else: 
                q = q + f" AND {field} {operator_map[operator]} {value}"
    if 'sort' in data.keys():
        q = q + f" ORDER BY {data['sort']['field']} {data['sort']['order']}"
    if 'limit' in data.keys():
        q = q + f" LIMIT {data['limit']}"
    if 'offset' in data.keys():
        q = q + f" OFFSET {data['offset']}"
    print(q)
    

if __name__ == '__main__':
    generate_query(q)