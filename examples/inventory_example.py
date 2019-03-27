import destiny, asyncio, json
client = destiny.Client()

@client.auth
class Authorisation:
    def __init__(self):
        self.apiToken = "Token"

@client.event
async def on_run():
    myProfile = await client.get_profile(
        "4611686018468394612",
        4,
        components=[
            "ProfileInventories",
            "CharacterInventories",
            "CharacterEquipment"
            ]
    )
    table = {}
    itemList = myProfile.profileInventory["items"]
    for key, attr in myProfile.characterInventories.items():
        itemList += attr["items"]
    for key, attr in myProfile.characterEquipment.items():
        itemList += attr["items"]
    for item in itemList:
        try:
            thing = await client.decode_hash(item["itemHash"], "DestinyInventoryItemDefinition", "en")
            if table.get(thing["itemTypeAndTierDisplayName"], None) == None:
                table[thing["itemTypeAndTierDisplayName"]] = []
            table[thing["itemTypeAndTierDisplayName"]].append(thing["displayProperties"])
        except Exception as ex:
            print(ex)
    with open("inventory.json", "w+") as out:
        json.dump(table, out, indent=4)
    client.close()