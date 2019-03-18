import requests

class GatewaySession:
    BASE_ROUTE = "" # API gateway here
    def __init__(self, apiToken=None, userAgent=None):
        if apiToken == None:
            raise # error
            
        self.userAgent = userAgent
        
        self.gatewaySession = requests.Session()
        self.gatewaySession.headers.update({"X-API-KEY": apiToken})
        
    def getRequest(self, request, headers=None):
        self.gatewaySession.get(request)
    
    def postRequest(self, request, headers=None):
        self.gatewaySession.post(request)
