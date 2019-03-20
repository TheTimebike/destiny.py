import aiohttp
import asyncio
import json
from collections import namedtuple
from types import SimpleNamespace as Namespace

from .http import GatewaySession
from .errors import *
from .character import Character
from .profile_bundle import ProfileBundle
from .membership import Membership
from .bungie_profile import BungieProfile
from .components import Components

class Client:    
    def __init__(self, loop=None):
        self.BASE_ROUTE = "https://www.bungie.net/Platform" # API gateway here

        self.userAgent = None
        self.apiToken = None

        self._loop = asyncio.get_event_loop() if loop is None else loop
        self._session = aiohttp.ClientSession(loop=self._loop)
        
    def mainfunc(self, coro):
        setattr(self, "mainFunction", coro)

    def run(self, apiToken=None):

        self.apiToken = apiToken
        if self.apiToken == None:
            raise TokenException   

        self.gatewaySession = GatewaySession(self._session, self.apiToken, self.userAgent)

        self._loop.run_until_complete(self.mainFunction())
        self._loop.close()

    def close(self):
        self._session.close()

    def _convert(self, data):
        self._jsonDump = json.dumps(data)
        return json.loads(self._jsonDump, object_hook=lambda d: Namespace(**d))

    def set_user_agent(self, appName, appVersion, appID, appWebsite=None, appEmail=None):
        if appWebsite != None or appEmail != None:
            self.userAgent = "{0}/{1}/{2} (+{3};{4})".format(appName, appVersion, appID, appWebsite, appEmail)
        else:
            self.userAgent = "{0}/{1}/{2}".format(appName, appVersion, appID)
            
    async def get_user(self, bungieMembershipID, membershipType=-1):
        if self.gatewaySession == None:
            raise NoGatewayException

        self._userData = await self.gatewaySession.getRequest(self.BASE_ROUTE + "/User/GetMembershipsById/{0}/{1}".format(bungieMembershipID, membershipType))

        if self._userData.get("Response", None) != None:
            return ProfileBundle(self._userData)
        return None

    async def search_for_user(self, name, membershipType=-1):
        if self.gatewaySession == None:
            raise NoGatewayException

        self._possibleUsers = await self.gatewaySession.getRequest(self.BASE_ROUTE + "/Destiny2/SearchDestinyPlayer/{0}/{1}/".format(membershipType, name))
        
        self._userObjectList = []
        for bungieUserData in self._possibleUsers["Response"]:
            self._userObjectList.append(Membership(bungieUserData))

        if len(self._userObjectList) == 0:
            return []
        return self._userObjectList
    
    async def get_membership_type(self, bungieMembershipID):
        if self.gatewaySession == None:
            raise NoGatewayException
    
    async def get_manifest(self):
        if self.gatewaySession == None:
            raise NoGatewayException
        
        return await self.gatewaySession.getRequest(self.BASE_ROUTE + "/Destiny2/Manifest/")["Response"]
        
    async def get_profile(self, membershipID, membershipType=-1, components=[]):
        if self.gatewaySession == None:
            raise NoGatewayException

        componentList = ",".join(components)

        self._profileData = await self.gatewaySession.getRequest(self.BASE_ROUTE + "/Destiny2/{0}/Profile/{1}/?components={2}".format(membershipType, membershipID, componentList))
        if self._profileData.get("Response", None) != None:
            self._components = Components()
            for key, value in self._profileData["Response"].items():
                setattr(self._components, key, value["data"])
            return self._components
        return None

    async def get_character(self, membershipID, characterID, membershipType=-1, components=[]):
        if self.gatewaySession == None:
            raise NoGatewayException

        componentList = ",".join(components)

        self._profileData = await self.gatewaySession.getRequest(self.BASE_ROUTE + "/Destiny2/{0}/Profile/{1}/Character/{2}/?components={3}".format(membershipType, membershipID, characterID, componentList))
        if self._profileData.get("Response", None) != None:
            #return self._convert(self._profileData["Response"]["character"]["data"])
            return Character(self._profileData)

        elif self._profileData.get("ErrorStatus", None) != None:
            return self._profileData
        return None
        