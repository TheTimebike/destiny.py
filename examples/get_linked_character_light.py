import destiny
client = destiny.Client()

conversionDict = {1: "xbox", 2: "ps", 4:"bnet"}
classDict = {0: "Titan", 1: "Hunter", 2: "Warlock", 3: None}

@client.mainfunc
async def main():
    """
    Example for fetching each profile that is linked to a Bungie.net account, then
    finds the light level for each character of the account.
    """
    myAccount = await client.get_user("4611686018464828555")# for example
    for profile in myAccount.destinyMemberships:
        print("{0}: {1}: {2}".format(profile.displayName, conversionDict[profile.membershipType], profile.membershipId))
        myProfile = await client.get_profile(
            profile.membershipId, 
            profile.membershipType, 
            components=["Profiles"]
        )
        for characterID in myProfile.profile.data.characterIds:
            myCharacter = await client.get_character(
                profile.membershipId, 
                characterID, 
                profile.membershipType, 
                components=["Characters"]
            )
            print("{0} - {1}".format(myCharacter.character.data.light, classDict[myCharacter.character.data.classType]))
    client.close()

client.set_user_agent("AppName", "Version", "Version", "AppID")
client.run("Token")