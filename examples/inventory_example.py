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
            "ProfileInventories", # To get items in the vault
            "CharacterInventories", # To get items on your character
            "CharacterEquipment" # To get equipped items.
            ]
    )
    itemTable = {}
    itemList = myProfile.profileInventory["items"]
    
    for key, attr in myProfile.characterInventories.items():
        itemList += attr["items"] # Iterate through the characters and add the results to the itemList
        
    for key, attr in myProfile.characterEquipment.items():
        itemList += attr["items"]
        
    for item in itemList:
        try:
            itemData = await client.decode_hash(item["itemHash"], "DestinyInventoryItemDefinition", "en") # Decode the item hash into its data
            if itemTable.get(itemData["itemTypeAndTierDisplayName"], None) == None:
                itemTable[itemData["itemTypeAndTierDisplayName"]] = []
            itemTable[itemData["itemTypeAndTierDisplayName"]].append(itemData["displayProperties"])
        except Exception as ex:
            print(ex)
    with open("inventory.json", "w+") as out:
        json.dump(table, out, indent=4)
    client.close()
