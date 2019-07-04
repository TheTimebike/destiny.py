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
from .groups.group_member import GroupMember
from .manifest import Manifest
from .milestone import Milestone
from .authorisation import Authorisation

class Client:    
    """Represents a client connection that is used to interact with the API.

    :param event_loop loop: The event loop in which the client will be ran under. If one is not provided, the client creates one.

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
        self._manifest = Manifest(self)

        self.authorisation = Authorisation(self)

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
            try:
                self._components._add_attr(key, value["data"])
                print("added {0}".format(key))
            except:
                pass
        return self._components
            
    async def get_user(self, bungieMembershipID, membershipType=-1):
        """*This function is a coroutine.*

        A function that returns a ProfileBundle object with user data. 

        :param str bungieMembershipID: The ID of the bungie account.
        :param str membershipType: The membershipType of the bungie account. 

        :return: A ProfileBungle object containing the user data. Returns None if not found.
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

        :return: A list of Membership objects.
        :rtype: List
        """
        if self.gatewaySession == None:
            raise NoGatewayException

        self._possibleUsers = await self.gatewaySession.get_request(self.BASE_ROUTE + "/Destiny2/SearchDestinyPlayer/{0}/{1}/".format(membershipType, name))
        
        self._userObjectList = []
        for bungieUserData in self._possibleUsers["Response"]:
            self._userObjectList.append(Membership(bungieUserData))
        return self._userObjectList
    
    async def update_manifest(self, language):
        """*This function is a coroutine.*

        A coroutine that updates the current Destiny2 manifest to the latest version.

        :param str language: The language of the manifest to use. Ex: en

        """
        if self.gatewaySession == None:
            raise NoGatewayException
        await self._manifest._update_manifest(language)

    async def decode_hash(self, hash, definition, language):
        """*This function is a coroutine.*

        A coroutine that uses the Destiny2 manifest to retrieve data related to a hash.
        If there is no up-to-date manifest downloaded, the manifest handler will automatically
        download one.

        :param str hash: The hash of the data.
        :param str definition: The definition of the hash. In other words, which table to look for the hash data in.
        :param str language: The language of the manifest to use. Ex: en

        :return: The data for the decoded hash. Returns None if not found. 
        :rtype: dict

        """
        if self.gatewaySession == None:
            raise NoGatewayException
        return await self._manifest._decode_hash(hash, definition, language)

    async def get_profile(self, membershipID, membershipType=-1, components=[]):
        """*This function is a coroutine.*

        A coroutine that returns a Components object with profile data.

        :param str membershipID: The ID of the bungie account.
        :param str membershipType: The membershipType of the bungie account.
        :param list components: A list of the data that will be requested from the API.

        :return: A Components object containing the profile data. Returns None if not found.
        :rtype: Components
        """
        if self.gatewaySession == None:
            raise NoGatewayException
        if components == []:
            components = [
                "Profiles",
                "VendorReceipts",
                "ProfileInventories",
                "ProfileCurrencies",
                "ProfileProgression",
                "Characters",
                "CharacterInventories",
                "CharacterProgressions",
                "CharacterRenderData",
                "CharacterActivities",
                "CharacterEquipment"
            ]
        componentList = ",".join(components)

        self._profileData = await self.gatewaySession.get_request(self.BASE_ROUTE + "/Destiny2/{0}/Profile/{1}/?components={2}".format(membershipType, membershipID, componentList))
        if self._profileData.get("Response", None) != None:
            return self._generate_component(self._profileData)
        return None

    async def get_character(self, membershipID, characterID, membershipType=-1, components=[]):
        """*This function is a coroutine.*

        A coroutine that returns a Components object with character-specific data.

        :param str membershipID: The ID of the bungie account.
        :param str characterID: The ID of the character that is connected to the bungie account.
        :param str membershipType: The membershipType of the bungie account.
        :param list components: A list of the data that will be requested from the API.

        :return: A Components object containing the character data.  Returns None if not found.
        :rtype: Components
        """
        if self.gatewaySession == None:
            raise NoGatewayException
        if components == []:
            components = [
                "Characters",
                "CharacterInventories",
                "CharacterProgressions",
                "CharacterRenderData",
                "CharacterActivities",
                "CharacterEquipment"
            ]
        componentList = ",".join(components)

        self._profileData = await self.gatewaySession.get_request(self.BASE_ROUTE + "/Destiny2/{0}/Profile/{1}/Character/{2}/?components={3}".format(membershipType, membershipID, characterID, componentList))
        if self._profileData.get("Response", None) != None:
            return self._generate_component(self._profileData)
        return None

    async def get_vendors(self, membershipID, characterID, membershipType=-1, components=[]):
        """*This function is a coroutine.*

        A coroutine that returns a Components object with character-specific vendor data.

        :param str membershipID: The ID of the bungie account.
        :param str characterID: The ID of the character that is connected to the bungie account.
        :param str membershipType: The membershipType of the bungie account.
        :param list components: A list of the data that will be requested from the API.

        :return: A Components object containing the vendor data. Returns None if not found.
        :rtype: Components
        """
        if self.gatewaySession == None:
            raise NoGatewayException
        if components == []:
            components = [
                "Vendors",
                "VendorCategories",
                "VendorSales",
            ]
        componentList = ",".join(components)

        self._vendorData = await self.gatewaySession.get_request(self.BASE_ROUTE + "/Destiny2/{0}/Profile/{1}/Character/{2}/Vendors/?components={3}".format(membershipType, membershipID, characterID, componentList))
        if self._vendorData.get("Response", None) != None:
            return self._generate_component(self._vendorData)
        return None
    
    async def get_group(self, groupID):
        """*This function is a coroutine*

        A coroutine that returns a Group object from a groupID.

        :param str groupID: The ID of the group to find.

        :return: A Group object containing the group data. Returns None if not found.
        :rtype: Group
        """

        if self.gatewaySession == None:
            raise NoGatewayException
        
        self._groupData = await self.gatewaySession.get_request(self.BASE_ROUTE + "/GroupV2/{0}/".format(groupID))
        if self._groupData.get("Response", None) != None:
            return Group(self._groupData)
        return None
    
    async def search_for_group(self, name, groupType):
        """*This function is a coroutine.*

        A coroutine that returns a Group object from a name and group type.

        :param str name: The string of the group name to search for
        :param str groupType: The type of group to search for. 0 for group, 1 for clan.

        :return: A Group object containing the group data. Returns None if not found.
        :rtype: Group
        """        
        if self.gatewaySession == None:
            raise NoGatewayException

        self._groupData = await self.gatewaySession.get_request(self.BASE_ROUTE + "/GroupV2/Name/{0}/{1}/".format(name, groupType))
        if self._groupData.get("Response", None) != None:
            return Group(self._groupData)
        return None
    
    async def get_milestones(self):
        """*This function is a coroutine*

        A coroutine that returns a list containing the milestone data from the Destiny2 API.

        :return: A list containing the milestone data in a dict. Returns an empty list if not found.
        :rtype: List
        """
        if self.gatewaySession == None:
            raise NoGatewayException
        
        self._milestoneData = await self.gatewaySession.get_request(self.BASE_ROUTE + "/Destiny2/Milestones/")
        self._milestoneList = []
        for key, attr in self._milestoneData["Response"].items():
            self._milestoneList.append(attr)
        #    self._milestoneList.append(Milestone(attr, await self.decode_hash(attr["milestoneHash"], "DestinyMilestoneDefinition", "en")))
        return self._milestoneList

    async def equip_item(self, characterID, itemID, membershipType, tokenID):
        """*This function is a coroutine*.

        A coroutine that moves an item from a characters inventory into a characters equipped slot.
        Note that it does not move the item from another character or the vault.

        :param str characterID: The ID of the character to equip the item on.
        :param str itemID: The ID of the item to equip on the character.
        :param str membershipType: The numerical value of an accounts' membership type. IE: 1,2 or 4
        :param str tokenID: The ID of the *bungie net account* that the character is linked to.

        """
        self._request = self.BASE_ROUTE + "/Destiny2/Actions/Items/EquipItem/"
        self._headers = {
            "X-API-Key": self.gatewaySession.apiToken,
            "Authorization": "Bearer {0}".format(self.authorisation.tokens[tokenID]["access_token"]),
            "Content-Type": "application/json"
        }
        self._data = json.dumps({
            "itemId": itemID,
            "characterId": characterID,
            "membershipType": membershipType
        })
    
        self._response = await self.gatewaySession.post_request(self._request, self._headers, self._data)
        return 

    async def move_item(self, characterID, itemID, itemHash, itemAmount, toVault, membershipType, tokenID):
        """*This function is a coroutine*

        A coroutine that moves an item to or from a players vault. Keep in mind that this cannot move items
        between characters.

        :param str characterID: The ID of the character to move the item to or from.
        :param str itemID: The ID of the item to move.
        :param int itemAmount: The amount of the item to move.
        :param bool toVault: If the item should be moved to or from the vault. True = to vault, False = from vault
        :param str membershipType: The numerical value of an accounts' membership type. IE: 1,2 or 4
        :param str tokenID: The ID of the *bungie net account* that the character is linked to.

        """
        self._request = self.BASE_ROUTE + "/Destiny2/Actions/Items/TransferItem/"
        self._headers = {
            "X-API-Key": self.gatewaySession.apiToken,
            "Authorization": "Bearer {0}".format(self.authorisation.tokens[tokenID]["access_token"]),
            "Content-Type": "application/json"
        }    
        self._data = json.dumps({
            "characterId": characterID,
            "itemId": itemID,
            "stackSize": itemAmount,
            "transferToVault": toVault,
            "itemReferenceHash": itemHash,
            "membershipType": membershipType
        })    
        self._response = await self.gatewaySession.post_request(self._request, self._headers, self._data)
        return 

    async def get_item(self, itemID, membershipID, membershipType, components=[]):
        if components == []:
            components = [
                "ItemInstances",
                "ItemObjectives",
                "ItemPerks",
                "ItemRenderData",
                "ItemStats",
                "ItemSockets",
                "ItemTalentGrids",
                "ItemCommonData",
                "ItemPlugStates"
            ]
        self._components = ",".join(components)
        self._request = self.BASE_ROUTE + "/Destiny2/{0}/Profile/{1}/Item/{2}/?components={3}".format(membershipType, membershipID, itemID, self._components)
        self._itemData = await self.gatewaySession.get_request(self._request)
        if self._itemData.get("Response", None) != None:
            return self._generate_component(self._itemData)
        return None

    async def GET_EVERYTHING(self, membershipID, membershipType):
        self._profileData = await self.get_profile(
            membershipID,
            membershipType,
        )
        self._dictConversion = self._profileData.__dict__
        for attr in self._dictConversion["profileInventory"]["items"]:
            attr["itemHashObject"] = await self.decode_hash(attr["itemHash"], "DestinyInventoryItemDefinition", "en")
        for key, attr in self._dictConversion["profileProgression"]["checklists"].items():
            print(attr)
            attr["progressHashObject"] = await self.decode_hash(key, "DestinyChecklistDefinition", "en")
        for key, attr in self._dictConversion["characters"].items():
            attr["raceObject"] = await self.decode_hash(attr["raceHash"], "DestinyRaceDefinition", "en")
            attr["genderObject"] = await self.decode_hash(attr["genderHash"], "DestinyGenderDefinition", "en")
            attr["classObject"] = await self.decode_hash(attr["classHash"], "DestinyClassDefinition", "en")
            attr["statsObject"] = []
            for subKey, subAttr in attr["stats"].items():
                attr["statsObject"].append(await self.decode_hash(subKey, "DestinyStatDefinition", "en"))
        
        return self._dictConversion

        
