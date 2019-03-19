import aiohttp
import asyncio

from .http import GatewaySession
from .bungieuser import BungieUser
from .userinfocard import InfoCard

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

    def run(self, apiToken):
        if self.userAgent == None:
            raise SyntaxError # Error, provided no token, use setUserAgent func
        self.apiToken = apiToken
        
        self.gatewaySession = GatewaySession(self._session, self.apiToken, self.userAgent)

        self._loop.run_until_complete(self.mainFunction())
        self._loop.close()

    def close(self):
        self._session.close()

    def setUserAgent(self, appName, appVersion, appID, appWebsite=None, appEmail=None):
        if appWebsite != None or appEmail != None:
            self.userAgent = "{0}/{1}/{2} (+{3};{4})".format(appName, appVersion, appID, appWebsite, appEmail)
        else:
            self.userAgent = "{0}/{1}/{2}".format(appName, appVersion, appID)
            
    async def get_user(self, bungieMembershipID):
        if self.gatewaySession == None:
            raise SyntaxError # Error, no client session
        self._userData = await self.gatewaySession.getRequest(self.BASE_ROUTE + "/Users/GetBungieNetUserById/{0}/".format(bungieMembershipID))
        return BungieUser(self._userData)

    async def search_for_user(self, name, membershipType=-1):
        if self.gatewaySession == None:
            raise SyntaxError # Error, no client session
        self._possibleUsers = await self.gatewaySession.getRequest(self.BASE_ROUTE + "/Destiny2/SearchDestinyPlayer/{1}/{0}".format(membershipType, name))
        self._userObjectList = []
        for bungieUserData in self._possibleUsers["Response"]:
            self._userObjectList.append(InfoCard(bungieUserData))
        return self._userObjectList
    
    async def get_membership_type(self, bungieMembershipID):
        if self.gatewaySession == None:
            raise SyntaxError # Error, no client session
    
    async def get_manifest(self):
        if self.gatewaySession == None:
            raise SyntaxError # Error, no client session
        return await self.gatewaySession.getRequest(self.BASE_ROUTE + "/Destiny2/Manifest/")
        
