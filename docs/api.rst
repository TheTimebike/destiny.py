API Reference
===============

Client
-------

.. autoclass:: destiny.Client
   :members:

Authorisation
---------------
.. class:: Authorisation

   To authorise your application, create a class constructor and decorate it with ``@client.auth`` and provide data in the form of class variables. ::

      @client.auth
      class Authorisation:
          def __init__(self):
              self.apiToken = "Token"

   Variables that you can give in the authorisation class:
   Most of these variables are optional, with the exception of the apiToken. However, Bungie has requested that users provide application information for the user agent as a gesture of good will.

   :param str apiToken: The API token for the application to run under.

   :param str appName: The name of the application. [Optional]

   :param str appVersion: The current version of the application. [Optional]

   :param str appID: The ID of the application. [Optional]

   :param str appWebsite: The website for the application. [Optional]

   :param str appEmail: The email for the application. [Optional]

Event Reference
---------------

To register an event, decorate an asynchronous function with ``@client.event``.

.. warning::
   
   All events must be coroutines to function properly. This means that they must be either:
   decorated with ``@asyncio.coroutine`` or be defined with ``async def`` (Python 3.5+)

.. function:: on_run()
   
   This event is called on the initial run of the program. The main bulk of the code should be put into
   this event.

.. function:: on_data_recieve(data)

   This event is called whenever the client receives data from an API request.

   :param str data: The data that was recieved.

.. function:: on_get_request(request)

   This event is called whenever the client makes a get request to the API.

   :param str request: The URL for the get request that the client made.

.. function:: on_post_request(request)

   This event is called whenever the client makes a post request to the API.

   :param str request: The URL for the post request that the client made.

Object Reference
----------------
.. autoclass:: destiny.Membership
   :members:

.. autoclass:: destiny.Components
   :members:

.. autoclass:: destiny.Platform
   :members: