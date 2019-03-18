from .http import GatewaySession
from .bungieuser import BungieUser

class Client:
    BASE_ROUTE = "https://www.bungie.net/Platform/Destiny2" # API gateway here
    USER_ROUTE = "https://www.bungie.net/Platform/User"
    GROUP_ROUTE = "https://www.bungie.net/Platform/GroupV2"
    
    def __init__(self, appName):
        self.userAgent = None
        self.apiToken = None
        
    def run(self, apiToken):
        if self.userAgent = None:
            raise # Error, provided no token, use setUserAgent func
        self.apiToken = apiToken
        
        self.gatewaySession = GatewaySession(self.apiToken, self.userAgent)
      
    def setUserAgent(self, appName, appVersion, appID, appWebsite=None, appEmail=None):
        if appWebsite != None or appEmail != None:
            self.userAgent = "{0}/{1}/{2} (+{3};{4}).format(appName, appVersion, appID, appWebsite, appEmail)"
        else:
            self.userAgent = "{0}/{1}/{2}".format(appName, appVersion, appID)
            
    def get_user(self, bungieMembershipID):
        if self.gatewaySession == None:
            raise # Error, no client session
        self._userData = self.gatewaySession.getRequest(USER_ROUTE + "/GetBungieNetUserById/{0}/".format(bungieMembershipID))
        return BungieUser(self._userData)

    def get_user_by_name(self, searchQuery):
        if self.gatewaySession = None:
            raise # Error, no client session
        self._possibleUsers = self.gatewaySession.getRequest(USER_ROUTE + "/SearchUsers/{0}".format(searchQuery))
        self._userObjectList = []
        for bungieUserData in self._possibleUsers:
            self._userObjectList.append(BungieUser(bungieUserData))
        return self._userObjectList
    
    def get_membership_type(self, bungieMembershipID):
        if self.gatewaySession = None:
            raise # Error, no client session
        
