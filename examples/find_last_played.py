import destiny
client = destiny.Client()

conversionDict = {1: "xbox", 2: "ps", 4:"bnet"}

@client.mainfunc
async def main():
    """
    Example for fetching each profile that is linked to a Bungie.net account, then
    finding the data that you last played on each profile.
    """
    myAccount = await client.get_user("MembershipID") # 4611686018464828555 for example
    for profile in myAccount.destinyMemberships:
        print("{0}: {1}: {2}".format(profile.displayName, conversionDict[x.membershipType], profile.membershipId))
        myProfile = await client.get_profile(x.membershipId, x.membershipType, components=["Profiles"])
        print(myProfile.profile.data.dateLastPlayed)
    client.close()

client.set_user_agent("AppName", "Version", "Version", "AppID")
client.run("Token")