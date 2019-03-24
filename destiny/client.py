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
from .group import Group

class Client:    
    """Represents a client connection that is used to interact with the API.

    :param event_loop loop: The event loop in which the client will be ran under. If one is not provided. the client creates one.

    userAgent
        A str that represents the applications' useragent. If one is not provided,
        it will default to template values.
    apiToken
        A str that represents the applications' API token. One is required to run a
        bot. 
    
    """
    def __init__(self, loop=None):
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
        """A function that runs the bot.
        """
        if self.auth.appEmail != None or self.auth.appWebsite != None:
            self.userAgent = "{0}/{1}/{2} (+{3};{4})".format(self.auth.appName, self.auth.appVersion, self.auth.appID, self.auth.appWebsite, self.auth.appEmail)
        else:
            self.userAgent = "{0}/{1}/{2}".format(self.auth.appName, self.auth.appVersion, self.auth.appID)

        self.apiToken = self.auth.apiToken 
        self.gatewaySession = GatewaySession(self._session, self._event_handler, self.apiToken, self.userAgent)

        self._loop.run_until_complete(self._event_handler._trigger_event("_trigger_on_run"))
        self._loop.close()

    def close(self):
        """
        Closes the connection to the Destiny2 API.
        """
        self._session.close()

    def _verify_auth(self):
        self._auth_attribute_list = ["appName", "appVersion", "appID", "appWebsite", "appEmail"]
        for attr in self._auth_attribute_list:
            setattr(self.auth, attr, attr if not hasattr(self.auth, attr) else getattr(self.auth, attr))

    def _generate_component(self, responseData):
        self._components = Components()
        for key, value in responseData["Response"].items():
            self._components._add_attr(key, value["data"])
        return self._components
            
    async def get_user(self, bungieMembershipID, membershipType=-1):
        """*This function is a coroutine.*

        A function that returns a ProfileBundle object containing data for the user specified.

        :param str bungieMembershipID: The ID of the bungie account.
        :param str membershipType: The membershipType of the bungie account. 

        :return: A ProfileBungle object containing the user data.
        :rtype: ProfileBundle
        """
        if self.gatewaySession == None:
            raise NoGatewayException

        self._userData = await self.gatewaySession.get_request(self.BASE_ROUTE + "/User/GetMembershipsById/{0}/{1}".format(bungieMembershipID, membershipType))

        if self._userData.get("Response", None) != None:
            return ProfileBundle(self._userData)
        return None

    async def search_for_user(self, name, membershipType=-1):
        """*This function is a coroutine.*

        A coroutine that returns a list of Membership objects containing data for the users that match the search.

        :param str name: The string that the API will return username matches for.
        :param str membershipType: The membershipType of the bungie account.

        :return: A list of Membership objects containing the user data.
        :rtype: List
        """
        if self.gatewaySession == None:
            raise NoGatewayException

        self._possibleUsers = await self.gatewaySession.get_request(self.BASE_ROUTE + "/Destiny2/SearchDestinyPlayer/{0}/{1}/".format(membershipType, name))
        
        self._userObjectList = []
        for bungieUserData in self._possibleUsers["Response"]:
            self._userObjectList.append(Membership(bungieUserData))
        return self._userObjectList
    
    async def get_manifest(self):
        """*This function is a coroutine.*

        A coroutine that returns a dictionary of the Destiny2 manifest.

        :return: The Destiny2 manifest.
        :rtype: dict
        """
        if self.gatewaySession == None:
            raise NoGatewayException
        self._manifestData = await self.gatewaySession.get_request(self.BASE_ROUTE + "/Destiny2/Manifest/")
        return self._manifestData["Response"]
        
    async def get_profile(self, membershipID, membershipType=-1, components=[]):
        """*This function is a coroutine.*

        A coroutine that returns a Components object with the specified data for the profile.

        :param str membershipID: The ID of the bungie account.
        :param str membershipType: The membershipType of the bungie account.
        :param list components: A list of the data that will be requested from the API.

        :return: A Components object containing the profile data.
        :rtype: Components
        """
        if self.gatewaySession == None:
            raise NoGatewayException

        componentList = ",".join(components)

        self._profileData = await self.gatewaySession.get_request(self.BASE_ROUTE + "/Destiny2/{0}/Profile/{1}/?components={2}".format(membershipType, membershipID, componentList))
        if self._profileData.get("Response", None) != None:
            return self._generate_component(self._profileData)
        return None

    async def get_character(self, membershipID, characterID, membershipType=-1, components=[]):
        """*This function is a coroutine.*

        A coroutine that returns a Components object with the specified data for the character.

        :param str membershipID: The ID of the bungie account.
        :param str characterID: The ID of the character that is connected to the bungie account.
        :param str membershipType: The membershipType of the bungie account.
        :param list components: A list of the data that will be requested from the API.

        :return: A Components object containing the character data.
        :rtype: Components
        """
        if self.gatewaySession == None:
            raise NoGatewayException

        componentList = ",".join(components)

        self._profileData = await self.gatewaySession.get_request(self.BASE_ROUTE + "/Destiny2/{0}/Profile/{1}/Character/{2}/?components={3}".format(membershipType, membershipID, characterID, componentList))
        if self._profileData.get("Response", None) != None:
            return self._generate_component(self._profileData)
        return None

    async def get_vendors(self, membershipID, characterID, membershipType=-1, components=[]):
        """*This function is a coroutine.*

        A coroutine that returns a Components object with the specified vendor data for the character.

        :param str membershipID: The ID of the bungie account.
        :param str characterID: The ID of the character that is connected to the bungie account.
        :param str membershipType: The membershipType of the bungie account.
        :param list components: A list of the data that will be requested from the API.

        :return: A Components object containing the vendor data.
        :rtype: Components
        """
        if self.gatewaySession == None:
            raise NoGatewayException

        componentList = ",".join(components)

        self._vendorData = await self.gatewaySession.get_request(self.BASE_ROUTE + "/Destiny2/{0}/Profile/{1}/Character/{2}/Vendors/?components={3}".format(membershipType, membershipID, characterID, componentList))
        if self._vendorData.get("Response", None) != None:
            return self._generate_component(self._vendorData)
        return None
    
    #async def get_group(self, name, groupType=-1):

    async def search_for_group(self, name, groupType):
        if self.gatewaySession == None:
            raise NoGatewayException

        self._groupData = await self.gatewaySession.get_request(self.BASE_ROUTE + "/GroupV2/Name/{0}/{1}/".format(name, groupType))
        if self._groupData.get("Response", None) != None:
            return Group(self._groupData)
        return None
