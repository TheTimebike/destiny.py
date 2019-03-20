class BungieProfile:
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