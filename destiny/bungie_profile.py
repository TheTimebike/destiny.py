class BungieProfile:
    """Represents the data of a users' bungie profile.

    :param dict responseData: The raw data given back by the API request.

    uniqueName
        The unique name of the bungie profile.
    membershipID
        The ID of the bungie profile.
    displayName
        The display name of the bungie profile.
    xboxName
        The username of the xbox account, if one is linked.
    psnName
        The username of the psn account, if one is linked.
    blizzardName
        The username of the blizzard account, if one is linked. Does not include discriminator
    lastAccess
        The date of the last time that the account was accessed.
    firstAccess
        The date of the first time that the account was accessed.
    isDeleted
        A boolean representing if the account has been deleted.
    showActivity
        Unknown
    localeInheretDefault
        Unknown
    showGroupMessaging
        Unknown
    locale
        The locale of the bungie profile.
    statusText
        The text representing the status of the account.
    statusDate
        The date that the status was updated.
    profilePicture
        The profile picture of the bungie profile.
    profilePictureUrl
        The URL of the profile picture.
    profileTheme
        The theme of the bungie profile.
    profileThemeID
        The ID of the theme of the bungie profile.
    successMessageFlags
        Unknown
    profileTitle
        The title of the bungie profile.
    profileTitleID
        The ID of the tile of the bungie profile.
    profileBio
        The bio of the bungie profile.
    """

    def __init__(self, responseData):
        self.uniqueName = responseData.get("uniqueName", None)
        self.membershipID = responseData.get("membershipId", None)

        self.displayName = responseData.get("displayName", None)
        self.xboxName = responseData.get("xboxDisplayName", None)
        self.psnName = responseData.get("psnDisplayName", None)
        self.blizzardName = responseData.get("blizzardDisplayName", None)

        self.lastAccess = responseData.get("lastUpdate", None)
        self.firstAccess = responseData.get("firstAccess", None)

        self.isDeleted = responseData.get("isDeleted", None)
        self.showActivity = responseData.get("showActivity", None)
        self.localeInheritDefault = responseData.get("localeInheritDefault", None)
        self.showGroupMessaging = responseData.get("showGroupMessaging", None)

        self.locale = responseData.get("locale", None)
        self.statusText = responseData.get("statusText", None)
        self.statusDate = responseData.get("statusDate", None)

        self.profilePicture = responseData.get("profilePicture", None)
        self.profilePictureUrl = responseData.get("profilePicturePath", None)
        self.profileTheme = responseData.get("profileThemeName", None)
        self.profileThemeID = responseData.get("profileTheme", None)
        self.successMessageFlags = responseData.get("successMessageFlags", None)
        self.profileTitleID = responseData.get("userTitle", None)
        self.profileTitle = responseData.get("userTitleDisplay", None)
        self.profileBio = responseData.get("about", None)