import destiny
client = destiny.Client()

@client.event
class Authorisation:
    def __init__(self):
        self.apiToken = "Token"

@client.event
async def on_run():
    await client.get_manifest()
    
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
