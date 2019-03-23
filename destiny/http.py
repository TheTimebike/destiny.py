import aiohttp
import asyncio
import json

import http.cookies
http.cookies._is_legal_key = lambda _: True
from .errors import HTTPException

class GatewaySession:
    """Represents an aiohttp session that is used to make requests to the API.

    :param aiohttp.ClientSession session: The ClientSession used to make the requests.

    :param EventHandler eventHandler: The event handler that triggers events in the client.

    :param str apiToken: The token that the application is run under.

    :param str userAgent: The user agent for the application. 

    userAgent
        A str that represents the applications' useragent. If one is not provided,
        it will default to None.
    headers
        A dict that contains the headers for the request, the main oe being X-API-KEY.
    session
        The ClientSession used to make requests.

    """
    def __init__(self, session, eventHandler=None, apiToken=None, userAgent=None):
        if apiToken == None or eventHandler == None:
            raise # error
            
        self.userAgent = userAgent
        self.session = session
        self.headers = {"X-API-Key": apiToken}
        self._event_handler = eventHandler
        
    async def getRequest(self, request):
        """*This function is a coroutine.*

        A function that requests specific data from the API and returns it in JSON format.

        :param str request: The URL for the request to be made to.

        :return The data given by the get request
        :rtype dict

        """
        await self._event_handler._trigger_event("_trigger_on_get_request", request)
        async with self.session.get(request, headers=self.headers) as _data:
        #print("making request")
            self._requestData = await _data.json()
        await self._event_handler._trigger_event("_trigger_on_data_recieve", self._requestData)
        return self._requestData

    async def postRequest(self, request):
        """*This function is a coroutine.*

        A function that sends instructions to the API.

        :param str request: The URL for the request to be made to.

        """
        await self._event_handler._trigger_event("_trigger_on_post_request", request)
        self._requestData = self.session.post(request, headers=self.headers)
