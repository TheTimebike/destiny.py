import destiny
client = destiny.Client()

@client.mainfunc
async def main():
    destinyManifest = await client.get_manifest()
    print(destinyManifest)
    client.close()

client.set_user_agent("AppName", "Version", "Version", "AppID")
client.run("Token")