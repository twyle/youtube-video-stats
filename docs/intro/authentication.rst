.. _intro-install:

=====================
Getting Authenticated
=====================

The first step to getting started with the YouTube Stats APi is getting 
authenticated. All the routes provided by the API required an authentication 
token.

This token is issued after registering, activating your account and then logging 
into your account. The Authentication process involves three main steps:

1. Creating an account
2. Activating your account
3. Logging into your account

To get you up to speed, we will walk you through the whole process.

Creating a user account
=======================

To create a new account you need:
1. A first name, which is a string of more than two characters and less than twenty 
characters
2. A last name, which similar restrictions to a first name.
3. A unique email address that you have access to.
4. A unique and difficult to guess password, preferably consisting of both 
uppercase and lowercase characters, numbers, symbols and atleast eight characters long.

To register, send a ``post request`` request to the route ``/api/v1/auth/register`` with 
the details mentioned above. 

Here's the python code that registers a new user:

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

This will print the account activation token as well as the user details as shown 
below:

.. code-block:: 
    
    {
        'activation_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODQ5MTA3MTQsImlhdCI6MTY4NDkwMzUxNCwic3ViIjoxfQ.cDndKPsrTVIA0fcr8ucX99q7THhaBKjbqHvLpSoYDa0', 
        'user': 
            {
                'account_activated': 0, 
                'date_registered': 'Wed, 24 May 2023 00:00:00 GMT', 
                'date_updated': 'Wed, 24 May 2023 00:00:00 GMT', 
                'email_address': 'lyle@gmail.com', 
                'first_name': 'lyle', 
                'id': 1, 
                'last_name': 'okoth', 
                'password': '$2b$12$/AnSOsQo2J08Ye1wFOybaeC0Cos3Inr5bdC2CpWXPkCWQdfBYI11C'
        }
    }

Activating a Created Account
============================
The next step is to activate the created account. Send a ``get request`` request to the 
route ``/api/v1/auth/activate`` with your user ``id`` and ``activation token``, both of which were 
given to you when you created your account.

Once an account is activated, you can log in with your email and password to get an 
authorization token. 

To activate your account with python:

.. code-block:: python

    import requests

    def activate_account():
        url = 'http://localhost:5000/api/v1/auth/activate'
        user_id = 1
        activation_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleoYDa0'
        resp = requests.get(url, params={'user_id': user_id, 'activation_token': activation_token})
        if resp.ok:
            print(resp.json())
        else:
            print(resp.json())

    if __name__ == '__main__':
        activate_account()

Put this in a text file, name it to something like ``activate_account.py``
and run it using the :command:`python` command::

    python activate_account.py

This will print out the user details as well as the account activation 
success message:

.. code-block:: python

    {
        'Success': 'Account Activated', 
        'data': 
            {
                'account_activated': 1, 
                'date_registered': '2023-05-24', 
                'date_updated': '2023-05-24', 
                'email_address': 'lyle@gmail.com', 
                'first_name': 'lyle', 
                'id': 1, 
                'last_name': 'okoth', 
                'password': '$2b$12$/AnSOsQo2J08Ye1wFOybaeC0Cos3Inr5bdC2CpWXPkCWQdfBYI11C'
            }
    }

Getting an authorization token
==============================
To make requests to the stats API, you need an authorization token.
This is obtained when you log into an activated account.

To log into your activated account, send a ``post request`` request to the 
``/api/v1/auth/login`` route with your ``email`` and ``password``. You will 
det back an ``access_token`` and a ``refresh_token``.

Here is an example using Python:

.. code-block:: python

    import requests

    def login_user():
        url = 'http://localhost:5000/api/v1/auth/login'
        login_details = {
            'email_address': 'lyle@gmail.com',
            'password': 'password'
        }
        resp = requests.post(url, json=login_details)
        if resp.ok:
            print(resp.json())
        else:
            print(resp.json())

    if __name__ == '__main__':
        login_user()

Put this in a text file, name it to something like ``login_user.py``
and run it using the :command:`python` command::

    python login_user.py

This will print out the ``access_token`` as well as the ``refresh_token``:

.. code-block:: python

    {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6Zm",
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6Zm"
    }

You can now use the access token to make requests to the stats API.