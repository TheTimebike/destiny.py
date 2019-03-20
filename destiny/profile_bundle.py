from .bungie_profile import BungieProfile
from .membership import Membership

class ProfileBundle:
    def __init__(self, responseData):
        self.destinyMemberships = []
        for membershipData in responseData["Response"]["destinyMemberships"]:
            self.destinyMemberships.append(Membership(membershipData))
        self.bungieProfile = BungieProfile(responseData["Response"]["bungieNetUser"])