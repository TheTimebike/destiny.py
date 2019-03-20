from .platform import Platform

class Membership:
    def __init__(self, responseData):
        self.displayName = responseData["displayName"]
        self.iconUrl = responseData["iconPath"]
        self.membershipID = responseData["membershipId"]
        self.membershipType = responseData["membershipType"]
        self.membershipObject = Platform(self.membershipType)