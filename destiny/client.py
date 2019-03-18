import asyncio

from .http import GatewaySession

class Client:
    BASE_ROUTE = "https://www.bungie.net/Platform/Destiny2/" # API gateway here
    USER_ROUTE = "https://www.bungie.net/Platform/User/"
    GROUP_ROUTE = "https://www.bungie.net/Platform/GroupV2/"
    
    def __init__(self, appName, loop=None):
        self.userAgent = None
        self.apiToken = None
        self.loop = asyncio.get_event_loop() if loop is None else loop
        
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
