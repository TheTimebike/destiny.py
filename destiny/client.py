import aiohttp
import asyncio
import json

from .http import GatewaySession
from .errors import *
from .profile_bundle import ProfileBundle
from .membership import Membership
from .bungie_profile import BungieProfile
from .components import Components
from .event_handler import EventHandler

class Client:    
    def __init__(self, loop=None):
        """Represents a client connection that is used to interact with the API.

        Parameters
        ----------
        loop : Optional[event loop]
            The event loop in which the client will be ran under. If one is not provided,
            the client creates one.
        """
        self.BASE_ROUTE = "https://www.bungie.net/Platform" # API gateway here

        self.userAgent = None
        self.apiToken = None

        self._loop = asyncio.get_event_loop() if loop is None else loop
        self._session = aiohttp.ClientSession(loop=self._loop)
        
        self._event_handler = EventHandler(self)
        
    def event(self, obj):
        setattr(self._event_handler, obj.__name__, obj)
    
    def auth(self, classObject):
        setattr(self, "auth", classObject())
        self._verify_auth()
        
    def run(self):
        if self.auth.appEmail != None or self.auth.appWebsite != None:
            self.userAgent = "{0}/{1}/{2} (+{3};{4})".format(self.auth.appName, self.auth.appVersion, self.auth.appID, self.auth.appWebsite, self.auth.appEmail)
        else:
            self.userAgent = "{0}/{1}/{2}".format(self.auth.appName, self.auth.appVersion, self.auth.appID)

        self.apiToken = self.auth.apiToken 
        self.gatewaySession = GatewaySession(self._session, self._event_handler, self.apiToken, self.userAgent)

        self._loop.run_until_complete(self._event_handler._trigger_event("_trigger_on_run"))
        self._loop.close()

    def close(self):
        self._session.close()

    def _verify_auth(self):
        self._auth_attribute_list = ["appName", "appVersion", "appID", "appWebsite", "appEmail"]
        for attr in self._auth_attribute_list:
            setattr(self.auth, attr, attr if not hasattr(self.auth, attr) else getattr(self.auth, attr))

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
        self._manifestData = await self.gatewaySession.getRequest(self.BASE_ROUTE + "/Destiny2/Manifest/")
        return self._manifestData["Response"]
        
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
