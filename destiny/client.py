import aiohttp
import asyncio

from .http import GatewaySession
from .errors import *

class Client:    
    def __init__(self, loop=None):
        self.BASE_ROUTE = "https://www.bungie.net/Platform" # API gateway here

        self.userAgent = None
        self.apiToken = None

        self._loop = asyncio.get_event_loop() if loop is None else loop
        self._session = aiohttp.ClientSession(loop=self._loop)
        
    def mainfunc(self, coro):
        setattr(self, "mainFunction", coro)
        print("Added mainfunction")

    def run(self, apiToken=None):

        self.apiToken = apiToken
        if self.apiToken == None:
            raise TokenException   

        self.gatewaySession = GatewaySession(self._session, self.apiToken, self.userAgent)

        self._loop.run_until_complete(self.mainFunction())
        self._loop.close()

    def close(self):
        self._session.close()

    def set_user_agent(self, appName, appVersion, appID, appWebsite=None, appEmail=None):
        if appWebsite != None or appEmail != None:
            self.userAgent = "{0}/{1}/{2} (+{3};{4})".format(appName, appVersion, appID, appWebsite, appEmail)
        else:
            self.userAgent = "{0}/{1}/{2}".format(appName, appVersion, appID)
            
    async def get_user(self, bungieMembershipID, membershipType=-1):
        if self.gatewaySession == None:
            raise NoGatewayException

        self._userData = await self.gatewaySession.getRequest(self.BASE_ROUTE + "/User/GetMembershipsById/{0}/{1}".format(bungieMembershipID, membershipType))
        print(self._userData["Response"])
        if self._userData["Response"].get("bungieNetUser", None) != None:
            return BungieUser(self._userData["Response"]["bungieNetUser"])
        raise NotFound

    async def search_for_user(self, name, membershipType=-1):
        if self.gatewaySession == None:
            raise NoGatewayException

        self._possibleUsers = await self.gatewaySession.getRequest(self.BASE_ROUTE + "/Destiny2/SearchDestinyPlayer/{0}/{1}".format(membershipType, name))
        self._userObjectList = []
        for bungieUserData in self._possibleUsers["Response"]:
            self._userObjectList.append(InfoCard(bungieUserData))
        return self._userObjectList
    
    async def get_membership_type(self, bungieMembershipID):
        if self.gatewaySession == None:
            raise NoGatewayException
    
    async def get_manifest(self):
        if self.gatewaySession == None:
            raise NoGatewayException
        return await self.gatewaySession.getRequest(self.BASE_ROUTE + "/Destiny2/Manifest/")
        
