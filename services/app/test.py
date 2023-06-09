import random
from typing import Any

import requests
from faker import Faker

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
        'comments_count': random.randint(0, 1000),
        'date_published': fake.date(),
    }
    return data


# flake8: noqa: E501
def post_data():
    url = 'http://localhost:5000/api/v1/videos/'
    admin_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODU1MjAxOTcsImlhdCI6MTY4NDkxNTM5Nywic3ViIjoyfQ.hne-aXvET8nSwzK1EVtC3-0hPZE_Sa4njp8ZH1u7rkk'
    headers = {'Authorization': f'Bearer {admin_token}'}

    videos = {'videos': [generate_data() for _ in range(5)]}

    resp = requests.post(url, json=videos, headers=headers)
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
        'confirm_password': 'password',
    }
    resp = requests.post(url, json=user_details)
    if resp.ok:
        print(resp.json())
    else:
        print(resp.json())


def activate_account():
    url = 'http://localhost:5000/api/v1/auth/activate'
    user_id = 1
    activation_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODQ5MTA3MTQsImlhdCI6MTY4NDkwMzUxNCwic3ViIjoxfQ.cDndKPsrTVIA0fcr8ucX99q7THhaBKjbqHvLpSoYDa0'
    resp = requests.get(url, params={'user_id': user_id, 'activation_token': activation_token})
    if resp.ok:
        print(resp.json())
    else:
        print(resp.json())


def login_user():
    url = 'http://localhost:5000/api/v1/auth/login'
    login_details = {'email_address': 'lyle@gmail.com', 'password': 'password'}
    resp = requests.post(url, json=login_details)
    if resp.ok:
        print(resp.json())
    else:
        print(resp.json())


# flake8: noqa: E501
def get_videos():
    url = 'http://localhost:5000/api/v1/videos'
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NDkxNTIzNCwianRpIjoiYTcyOGQ0NzEtNDc3Yi00ZGJmLWJmZmYtNWJhMzU0ZGYwNWMwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjg0OTE1MjM0LCJleHAiOjE2ODUwMDE2MzR9.vapCGWOlCAHZPd72ZDz_MM8cV4wdZMDQdH7452TGaCA'
    headers = {'Authorization': f'Bearer {token}'}
    resp = requests.get(url, headers=headers)
    if resp.ok:
        print(resp.json())
    else:
        print(resp.json())


# flake8: noqa: E501
def test_admin():
    url = 'http://localhost:5000/api/v1/videos'
    admin_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODU1MjAxOTcsImlhdCI6MTY4NDkxNTM5Nywic3ViIjoyfQ.hne-aXvET8nSwzK1EVtC3-0hPZE_Sa4njp8ZH1u7rkk'
    headers = {'Authorization': f'Bearer {admin_token}'}
    resp = requests.get(url, headers=headers)
    if resp.ok:
        print(resp.json())
    else:
        print(resp.json())


if __name__ == '__main__':
    post_data()
