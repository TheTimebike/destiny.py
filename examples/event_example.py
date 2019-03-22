import destiny
client = destiny.Client()

@client.auth
class Authorisation:
    def __init__(self):
        self.apiToken = "Token"
        self.appName = "Name"
        self.appVersion = "1"
        self.appID = "1"
        self.appWebsite = None
        self.verificationUrl = None
        self.appEmail = None

@client.event
async def on_run():
    myAccount = await client.get_user("4611686018440571747")
    for profile in myAccount.destinyMemberships:
        print("{0}: {1}: {2}".format(profile.displayName, profile.membershipObject.type, profile.membershipID))
    client.close()
    
@client.event
async def on_get_request(request):
    print("""
    ___________
    GET_REQUEST:
    {0}
    """.format(request))
    
@client.event
async def on_data_recieve(data):
    print("""
    _____________
    DATA_RECIEVED:
    {0}
    """.format(data))
    
client.run()
