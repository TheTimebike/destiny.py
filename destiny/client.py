from .http import GatewaySession

class Client:
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
