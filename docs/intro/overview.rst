.. _intro-overview:

===============
API at a glance
===============

The YouTube Stats API is an API that provides the user with data on Videos, Playlists and Channels
operated by social media influencers from Kenya.

With this API, you can esaily obtain details about a video uploaded to YouTube such as when 
it was uploaded, how many views does it have, the number of likes and comments as well as the 
comments posted. The data also includes the video duration and description. The same applies 
to playlists and channels.

Walk-through of an example of loading 10 videos from Test channel
====================================================================

To show you the capabilities of this API, we will walk you through the process
of obtaining data on the latest 10 videos uploaded to the Test Channel.

The process involves 3 steps

1. Registration for an account. This is neccessary in order to get an API key.
2. Account activation.
3. Logging ibto the created account to obtain the API key.
4. Sending a request to the channels endpoint in order to load the latest 10 videos.

Account Registration
====================

To get started with the YouTube Stats API, you need an account. Send a ``post request``
to the end-point ``/api/v1/auth/register`` with the following details:

1. First Name e.g `lyle`
2. Last Name e.g `okoth`
3. Email Address e.g `lyle@gmail.com`
4. Password e.g `password`
5. Password confirmation e.g `password`

Here is an example using python:

.. code-block:: python

    import requests

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
            print(resp.json)

    if __name__ == '__main__':
        register_user()

Put this in a text file, name it to something like ``register_user.py``
and run it using the :command:`python` command::

    python register_user.py


This will print a list of videos that deal with programming with Python. The
output looks like this:

.. code-block:: python
    {
        'date_registered': 'Tue, 23 May 2023 16:25:51 GMT', 
        'date_updated': 'Tue, 23 May 2023 16:25:51 GMT', 
        'email_address': 'lyle@gmail.com', 
        'first_name': 'lyle', 
        'id': 2, 
        'last_name': 'okoth', 
        'password': 'password',
        'activation_token': 'activation token'
    }

Account Activation
==================

To activate your account, make a ``post request`` to the account activation route
``/api/v1/auth/register`` with your email address and the token returned when you 
created your account.

Here is an example using python:

.. code-block:: python

    import requests

    def activate_account():
        url = 'http://localhost:5000/api/v1/auth/activate'
        activation_details = {
            'email_address': 'lyle@gmail.com',
            'token': 'token'
        }
        resp = requests.post(url, json=activation_details)
        if resp.ok:
            print(resp.json)

    if __name__ == '__main__':
        activate_account()

Put this in a text file, name it to something like ``activate_account.py``
and run it using the :command:`python` command::

    python activate_account.py    

The output will include your registration details as shown:

.. code-block:: python
    { 
        'email_address': 'lyle@gmail.com', 
        'first_name': 'lyle', 
        'id': 2, 
        'last_name': 'okoth'
    }

Log into Activated Account
==========================

To use the API, you will need an API key, that will be used to authenticate 
your identity. To get an API key, log into your aactivated account. This 
involves sending a ``post request`` request to the ``/api/v1/auth/register`` 
route with your email and password.

Here is an example in Python:

.. code-block:: python

    import requests

    def log_into_account():
        url = 'http://localhost:5000/api/v1/auth/login'
        login_details = {
            'email_address': 'lyle@gmail.com',
            'password': 'password'
        }
        resp = requests.post(url, json=login_details)
        if resp.ok:
            print(resp.json)

    if __name__ == '__main__':
        log_into_account()

Put this in a text file, name it to something like ``log_into_account.py``
and run it using the :command:`python` command::

    python log_into_account.py    

Once this is done executing, you will get back an authorization token 
and a refresh toke. The authorization token will be used every time you 
make a request to the API, whereas the refresh token will be used to 
generate a new authentication token. 

Here is a sample output:

.. code-block:: python
    { 
        'authorization_token': 'authorization token', 
        'refresh_token': 'refresh token'
    }