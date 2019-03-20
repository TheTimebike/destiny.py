import aiohttp
import asyncio
import json
from collections import namedtuple
from types import SimpleNamespace as Namespace

from .http import GatewaySession
from .errors import *
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

    def auth(self, authClass):
        setattr(self, "auth", authClass)
        print("!!")

    def run(self):
        print("!")
        if self.auth.appEmail != None or self.auth.appWebsite != None:
            self.userAgent = "{0}/{1}/{2} (+{3};{4})".format(self.auth.appName, self.auth.appVersion, self.auth.appID, self.auth.appWebsite, self.auth.appEmail)
        else:
            self.userAgent = "{0}/{1}/{2}".format(appName, appVersion, appID)

        self.apiToken = self.auth.apiToken 
        self.gatewaySession = GatewaySession(self._session, self.apiToken, self.userAgent)

        self._loop.run_until_complete(self.mainFunction())
        self._loop.close()

    def close(self):
        self._session.close()

    def _generate_component(self, responseData):
        self._components = Components()
        for key, value in responseData["Response"].items():
            setattr(self._components, key, value["data"])
        return self._components
            
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
        return self._userObjectList
    
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
            return self._generate_component(self._profileData)
        return None

    async def get_character(self, membershipID, characterID, membershipType=-1, components=[]):
        if self.gatewaySession == None:
            raise NoGatewayException

        componentList = ",".join(components)

        self._profileData = await self.gatewaySession.getRequest(self.BASE_ROUTE + "/Destiny2/{0}/Profile/{1}/Character/{2}/?components={3}".format(membershipType, membershipID, characterID, componentList))
        if self._profileData.get("Response", None) != None:
            return self._generate_component(self._profileData)
        return None

    async def get_vendors(self, membershipID, characterID, membershipType=-1, components=[]):
        if self.gatewaySession == None:
            raise NoGatewayException

        componentList = ",".join(components)

        self._vendorData = await self.gatewaySession.getRequest(self.BASE_ROUTE + "/Destiny2/{0}/Profile/{1}/Character/{2}/Vendors/?components={3}".format(membershipType, membershipID, characterID, componentList))
        if self._vendorData.get("Response", None) != None:
            return self._generate_component(self._vendorData)
        return None