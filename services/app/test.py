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
 
def register_user():
    url = 'http://localhost:5000/api/v1/auth/register'
    user_details = {
        'first_name': 'lyle',
        'last_name': 'okoth',
        'email_address': 'lyle@gmail.com',
        'password': 'password',
        'confirm_password': 'password'
    }
    resp = requests.post(url, json=user_details)
    if resp.ok:
        print(resp.json())
    else:
        print(resp.json())

if __name__ == '__main__':
    register_user()        
