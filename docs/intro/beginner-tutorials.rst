.. _beginner_tutorials:

============
Simple Usage
============

In this step by step tutorial, we will go through the steps needed to:

1. Getting a list of channels and their details.
2. Getting a list of playlists.
3. Getting a playlist's items.
4. Getting a playlist's videos.
5. Getting a videos comments.

Before we get started, make sure to take a look at :ref:`intro-overview` to learn how to get
started with the API.

Getting a list of channels
--------------------------

Make a ```GET``` request to ``api/v1/channels/``.

Using Python:

.. code-block:: python3

    import requests

    def get_channels():
        url = 'https://youtube-stats.oryks-sytem.com/api/v1/channels'
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NDkwNzQ2OCwianRpIjoiOTk5ZTBkMzItNjcxMC00YWYwLTkyYzktMTQ0MDljNjU4ZmNkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjg0OTA3NDY4LCJleHAiOjE2ODQ5MDgzNjh9.j0ClUjFyRnl8w8BrQ-dL8z_CCkr87D-LTaIn6jbXCDw"
        headers = {"Authorization": f"Bearer {token}"}
        resp = requests.get(url, headers=headers)
        if resp.ok:
            print(resp.json())
        else:
            print(resp.json())

    if __name__ == '__main__':
        get_channels()

Make sure to replace the token with your own authorization token. Put this in a text file, name it to
something like ``get_channels.py`` and run it using the :command:`python` command::

    python get_channels.py

Once it's done executing you will get back a list of YouTube channels. Here is sample output:

.. code-block::

    [
    {
        "channel_description": "At Engage, fascinating thinkers and doers combine to spark discussion and connection with the audience on a diverse mix of topics. https://linktr.ee/EngageKe \nEvery week, we have a new video of someone like you and I sharing their stories, experiences, dreams, aspirations, fears and ambitions. Inform. Inspire and Influence. We believe that the Inspiration we seek rests in people like us who seem ordinary and have gone through experiences that we can learn from or aspire to. We believe in the power of human connection and engagement. Subscribe and share!\n\nEngage also provides an opportunity for talented artistes to showcase their skill and entertain the audience. \nFollow us on our social media pages  https://www.facebook.com/EngageKe/ and @Engageke on Instagram and Twitter.  You can reach us on info@engage.or.ke and +254702547254.",
        "channel_id": "UCD-Mf4F5ZQ1Jw-nb2gqD1mw",
        "channel_thumbnail": "https://yt3.ggpht.com/BhYf5rOvYBFoRZ9Qrax9nm-8CNkuyOtPuPv0X6jpaITZJZK6zNNPoTt06gcjkJT4-AtjHHdQ=s240-c-k-c0x00ffffff-no-rj",
        "channel_title": "Engage Talk",
        "custom_url": "@engagetalk",
        "id": 6,
        "published_at": "2015-09-21T11:45:57Z",
        "subscribers_count": 153000,
        "videos_count": 765,
        "views_count": 20060261
    },
    {
        "channel_description": "This is an Issue based Comedy show on NTV  Kenya Hosted by DR. King'ori",
        "channel_id": "UCJvhxJf8-Bne99uzuQpFIpg",
        "channel_thumbnail": "https://yt3.ggpht.com/vljXBSKmKbPhu6nOkcJoxczYZgm6rIzBB5nSY7xyRIeGZMc75C_XKSxFIQH6Uz3FguXAvouon2s=s240-c-k-c0x00ffffff-no-rj",
        "channel_title": "The Wicked Edition with Dr. King'ori",
        "custom_url": "@thewickededitiondrkingori",
        "id": 7,
        "published_at": "2016-06-03T22:11:03Z",
        "subscribers_count": 395000,
        "videos_count": 747,
        "views_count": 59405338
    },
    {
        "channel_description": "\nHosted by celebrated Kenyan content creators Wanjiru Njiru and Ben Cyco, The Joy Ride is a platform that aims to inspire, educate and entertain by sharing on life and its journey.\n\nHop on the ultimate Joy Ride!\n",
        "channel_id": "UCCjULCQvh2cQQLzYe4DC2Nw",
        "channel_thumbnail": "https://yt3.ggpht.com/QuvmCT8MHN8SgnRC1uFxNMowtIgo5sdn3KO9z3cYiXAsTPre73xsFVt5THieiEshyDfyxPoI=s240-c-k-c0x00ffffff-no-rj",
        "channel_title": "The Joy Ride",
        "custom_url": "@thejoyridepod",
        "id": 8,
        "published_at": "2021-12-06T08:07:37.9638Z",
        "subscribers_count": 54700,
        "videos_count": 115,
        "views_count": 5227127
    }
    ]

Getting a list of Playlists
----------------------------

Let us now get a bunch of playlists.

Make a ```GET``` request to ``api/v1/playlists/``.

Using Python:

Using Python:

.. code-block:: python3

    import requests

    def get_playlists():
        url = 'https://youtube-stats.oryks-sytem.com/api/v1/playlists'
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NDkwNzQ2OCwianRpIjoiOTk5ZTBkMzItNjcxMC00YWYwLTkyYzktMTQ0MDljNjU4ZmNkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjg0OTA3NDY4LCJleHAiOjE2ODQ5MDgzNjh9.j0ClUjFyRnl8w8BrQ-dL8z_CCkr87D-LTaIn6jbXCDw"
        headers = {"Authorization": f"Bearer {token}"}
        resp = requests.get(url, headers=headers)
        if resp.ok:
            print(resp.json())
        else:
            print(resp.json())

    if __name__ == '__main__':
        get_playlists()

Put this in a text file, name it to something like ``get_playlists.py`` and run it using the
:command:`python` command::

    python get_playlists.py

Once this is done running you will get back a list of playlists:

.. code-block::

    [
    {
        "channel_id": "UC5WVOSvL9bc6kwCMXXeFLLw",
        "id": 3,
        "playlist_description": "",
        "playlist_id": "PLouh1K1d9jkZQE0ITJH820mS6s8J5PyxH",
        "playlist_thumbnail": "https://i.ytimg.com/vi/EcRg4X1ftrQ/sddefault.jpg",
        "playlist_title": "VLOGS",
        "privacy_status": "public",
        "published_at": "2022-10-12T18:15:53Z",
        "videos_count": 355
    },
    {
        "channel_id": "UC5WVOSvL9bc6kwCMXXeFLLw",
        "id": 4,
        "playlist_description": "",
        "playlist_id": "PLouh1K1d9jkbKgYLnO8csSJONqCBxM7Bj",
        "playlist_thumbnail": "https://i.ytimg.com/vi/qVHhcn_r3bs/sddefault.jpg",
        "playlist_title": "TUMA PIN",
        "privacy_status": "public",
        "published_at": "2022-02-02T20:39:46Z",
        "videos_count": 5
    },
    {
        "channel_id": "UC5WVOSvL9bc6kwCMXXeFLLw",
        "id": 5,
        "playlist_description": "",
        "playlist_id": "PLouh1K1d9jkYZo8h1zPH3P1ScAWA8gxbu",
        "playlist_thumbnail": "https://i.ytimg.com/vi/27FnpZNmJ8M/mqdefault.jpg",
        "playlist_title": "LTMYS",
        "privacy_status": "public",
        "published_at": "2021-08-19T08:49:34Z",
        "videos_count": 20
    },
    {
        "channel_id": "UC5WVOSvL9bc6kwCMXXeFLLw",
        "id": 6,
        "playlist_description": "",
        "playlist_id": "PLouh1K1d9jkbgO4hIHvabpyxUTqruqFq-",
        "playlist_thumbnail": "https://i.ytimg.com/img/no_thumbnail.jpg",
        "playlist_title": "MAKE-UP REVIEWS",
        "privacy_status": "public",
        "published_at": "2018-08-11T13:28:00Z",
        "videos_count": 0
    }
    ]
