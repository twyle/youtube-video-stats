.. Kenyan Influencer's YouTube Stats documentation master file, created by
   sphinx-quickstart on Mon May 22 11:03:02 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=============================================================
Welcome to Kenyan Influencer's YouTube Stats's documentation!
=============================================================

This is an Application Programming Interface (API) for getting information
on Videos Posted by Kenyan Social Media Influencers on YouTube. The data
provided includes channel details such as title, number of subscribers,
playlist including the videos in the playlists, video details such as comments, likes,
views, when the video was published as well as the video duration..

Getting Started
===============

.. toctree::
   :caption: Getting Started
   :hidden:

   intro/overview
   intro/authentication
   intro/beginner-tutorials
   intro/advanced-tutorials

:doc:`intro/overview`
    Understand what the YouTube Stats API is and how it can help you.

:doc:`intro/authentication`
    Learn how to get authenticated in oreder to use the API.

:doc:`intro/beginner-tutorials`
    Send your First request to the Stats API.

:doc:`intro/advanced-tutorials`
    Dig deep into data retrieval by sending complex requests.

API Routes
===============

.. toctree::
   :caption: API Routes
   :hidden:

   api/v1/auth/auth
   api/v1/channels/channels
   api/v1/videos/videos

:doc:`api/v1/auth/auth`
    Learn how the authentication route works.

:doc:`/api/v1/channels/channels`
    Learn how to get channel data using the channel route.

:doc:`/api/v1/videos/videos`
    Learn how to get video data using the videos route..

.. toctree::
   :caption: Auth Routes
   :hidden:

   api/v1/auth/register
   api/v1/auth/activate
   api/v1/auth/login
   api/v1/auth/refresh

:doc:`api/v1/auth/register`
    Learn how the registration route works.

:doc:`api/v1/auth/activate`
    Learn how the account activation route works.

:doc:`api/v1/auth/login`
    Learn how the login route works.

:doc:`api/v1/auth/refresh`
    Learn how the token refresh route works.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
