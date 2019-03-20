import aiohttp
import asyncio

import http.cookies
http.cookies._is_legal_key = lambda _: True
from .errors import HTTPException

class GatewaySession:
    BASE_ROUTE = "https://www.bungie.net/Platform/Destiny2/" # API gateway here
    USER_ROUTE = "https://www.bungie.net/Platform/User/"
    GROUP_ROUTE = "https://www.bungie.net/Platform/GroupV2/"
    
    def __init__(self, session, apiToken=None, userAgent=None):
        if apiToken == None:
            raise # error
            
        self.userAgent = userAgent
        self.session = session
        self.headers = {"X-API-Key": apiToken}
        
    async def getRequest(self, request):
        try:
            #print(request)
            async with self.session.get(request, headers=self.headers) as _data:
                self._requestData = await _data.json()
            return self._requestData
        except Exception as ex:
            raise HTTPException
    
    async def postRequest(self, request):
        self._requestData = self.session.post(request, headers=self.headers).json()
