from .http import GatewaySession
from .bungieuser import BungieUser

class Client:    
    def __init__(self):
        self.BASE_ROUTE = "https://www.bungie.net/Platform" # API gateway here

        self.userAgent = None
        self.apiToken = None
        
    def run(self, apiToken):
        if self.userAgent == None:
            raise SyntaxError # Error, provided no token, use setUserAgent func
        self.apiToken = apiToken
        
        self.gatewaySession = GatewaySession(self.apiToken, self.userAgent)
      
    def setUserAgent(self, appName, appVersion, appID, appWebsite=None, appEmail=None):
        if appWebsite != None or appEmail != None:
            self.userAgent = "{0}/{1}/{2} (+{3};{4})".format(appName, appVersion, appID, appWebsite, appEmail)
        else:
            self.userAgent = "{0}/{1}/{2}".format(appName, appVersion, appID)
            
    def get_user(self, bungieMembershipID):
        if self.gatewaySession == None:
            raise SyntaxError # Error, no client session
        self._userData = self.gatewaySession.getRequest(self.BASE_ROUTE + "/Users/GetBungieNetUserById/{0}/".format(bungieMembershipID))
        return BungieUser(self._userData)

    def get_user_by_name(self, searchQuery):
        if self.gatewaySession == None:
            raise SyntaxError # Error, no client session
        self._possibleUsers = self.gatewaySession.getRequest(self.BASE_ROUTE + "/Users/SearchUsers/{0}".format(searchQuery))
        self._userObjectList = []
        for bungieUserData in self._possibleUsers:
            self._userObjectList.append(BungieUser(bungieUserData))
        return self._userObjectList
    
    def get_membership_type(self, bungieMembershipID):
        if self.gatewaySession == None:
            raise SyntaxError # Error, no client session
    
    def get_manifest(self):
        if self.gatewaySession == None:
            raise SyntaxError # Error, no client session
        self._manifest = self.gatewaySession.getRequest(self.BASE_ROUTE + "/Destiny2/Manifest/")
        return self._manifest
        
