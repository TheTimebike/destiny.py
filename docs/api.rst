API Reference
===============

Client
-------

.. autoclass:: destiny.Client
   :members:

.. autoclass:: destiny.GatewaySession
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

   :param str appID: The ID of the application. [Optional] [Required for Authentication]

   :param str appSecret: The secret of the application. [Optional] [Required for Authentication]

   :param str appWebsite: The website for the application. [Optional]

   :param str appEmail: The email for the application. [Optional]

   Destiny.py also includes an access token manager to make it easier to send requests that need authentication.
   authentication tokens are stored by the ID of the *bungie net* account that they are enlisted under.
   The management system includes automatic refreshing of expired access tokens. To get started, pass an
   *oAuth* token to ``client.authentication.get_access_from_oauth()``. get_access_from_oauth is a coroutine and must
   be awaited.

   The tokens themselves are stored in the ``tokens`` attribute of client.authentication inside a dictionary.

   .. autoclass:: destiny.Authentication()
      :members:
       

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

.. autoclass:: destiny.Membership()
   :members:

.. autoclass:: destiny.Components()
   :members:

.. autoclass:: destiny.Platform(membershipType)
   :members:

.. autoclass:: destiny.Progress()
   :members:

.. autoclass:: destiny.BungieProfile()
   :members:

.. autoclass:: destiny.ProfileBundle()
   :members:

.. autoclass:: destiny.Group()
   :members:

.. autoclass:: destiny.GroupType(groupType)
   :members:

.. autoclass:: destiny.GroupFeatures()
   :members:

.. autoclass:: destiny.GroupMember()
   :members:

.. autoclass:: destiny.Manifest()
   :members:

.. autoclass:: destiny.ManifestReader()
   :members:

Exception Reference
--------------------

.. autoclass:: destiny.NotFoundException()
   :members:

.. autoclass:: destiny.NoGatewayException()
   :members:

.. autoclass:: destiny.TokenException()
   :members:

.. autoclass:: destiny.LanguageNotFoundException()
   :members: