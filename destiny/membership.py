from .platform import Platform

class Membership:
    """Represents a users' Membership data.
    
    :param dict responseData: Returns The raw data given back by the API request.

    displayName
        Returns the display name of the user.
    iconUrl
        Returns the URL of the users' icon.
    membershipID
        Returns The ID of the users' membership.
    membershipType
        Returns The enum value of the users' membership type. 
        1=xbox, 2=psn, 4=blizzard
    membershipObject
        Returns The membershipType put into a class that makes it more readable.
    """    
    def __init__(self, responseData):
        self.displayName = responseData["displayName"]
        self.iconUrl = responseData["iconPath"]
        self.membershipID = responseData["membershipId"]
        self.membershipType = responseData["membershipType"]
        self.membershipObject = Platform(self.membershipType)