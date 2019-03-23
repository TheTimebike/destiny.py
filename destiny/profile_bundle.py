from .bungie_profile import BungieProfile
from .membership import Membership

class ProfileBundle:
    """This represents a bundle of membership and profile information from a search request.

    :param dict responseData: The raw data given back by the API request.

    destinyMemberships
        A list of Membership objects containing information about each linked account.
    bungieProfile
        If the API gave a linked bungieNetUser profile, a BungieProfile object will be created to store the data.
    """
    def __init__(self, responseData):
        self.destinyMemberships = []
        for membershipData in responseData["Response"]["destinyMemberships"]:
            self.destinyMemberships.append(Membership(membershipData))
        self.bungieProfile = BungieProfile(responseData["Response"]["bungieNetUser"]) if responseData["Response"].get("bungieNetUser", None) != None else None