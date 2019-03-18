import requests

class GatewaySession:
    BASE_ROUTE = "https://www.bungie.net/Platform/Destiny2/" # API gateway here
    USER_ROUTE = "https://www.bungie.net/Platform/User/"
    GROUP_ROUTE = "https://www.bungie.net/Platform/GroupV2/"
    
    def __init__(self, apiToken=None, userAgent=None):
        if apiToken == None:
            raise # error
            
        self.userAgent = userAgent
        
        self.gatewaySession = requests.Session()
        self.gatewaySession.headers.update({"X-API-KEY": apiToken})
        
    def getRequest(self, request, headers=None):
        self._requestData = self.gatewaySession.get(request)
        print(self._requestData)
        return self._requestData
    
    def postRequest(self, request, headers=None):
        self._requestData = self.gatewaySession.post(request)
