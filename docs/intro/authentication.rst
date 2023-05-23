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