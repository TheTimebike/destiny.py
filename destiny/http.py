import aiohttp
import asyncio
import json

import http.cookies
http.cookies._is_legal_key = lambda _: True
from .errors import HTTPException

class GatewaySession:
    def __init__(self, session, eventHandler=None, apiToken=None, userAgent=None):
        if apiToken == None or eventHandler == None:
            raise # error
            
        self.userAgent = userAgent
        self.session = session
        self.headers = {"X-API-Key": apiToken}
        self._event_handler = eventHandler
        
    async def getRequest(self, request):
        await self._event_handler._trigger_event("_trigger_on_get_request", request)
        async with self.session.get(request, headers=self.headers) as _data:
        #print("making request")
            self._requestData = await _data.json()
        await self._event_handler._trigger_event("_trigger_on_data_recieve", self._requestData)
        return self._requestData

    async def postRequest(self, request):
        await self._event_handler._trigger_event("_trigger_on_post_request", request)
        self._requestData = self.session.post(request, headers=self.headers)
