class BungieProfile:
    def __init__(self, responseData):
        self.uniqueName = responseData["uniqueName"]
        self.membershipID = responseData["membershipId"]

        self.displayName = responseData["displayName"]
        self.xboxName = responseData["xboxDisplayName"]
        self.psnName = responseData["psnDisplayName"]
        self.blizzardName = responseData["blizzardDisplayName"]

        self.lastAccess = responseData["lastUpdate"]
        self.firstAccess = responseData["firstAccess"]

        self.isDeleted = responseData["isDeleted"]
        self.showActivity = responseData["showActivity"]
        self.localeInheritDefault = responseData["localeInheritDefault"]
        self.showGroupMessaging = responseData["showGroupMessaging"]

        self.locale = responseData["locale"]
        self.statusText = responseData["statusText"]
        self.statusDate = responseData["statusDate"]

        self.profilePicture = responseData["profilePicture"]
        self.profilePictureUrl = responseData["profilePicturePath"]
        self.profileTheme = responseData["profileThemeName"]
        self.profileThemeID = responseData["profileTheme"]
        self.successMessageFlags = responseData["successMessageFlags"]
        self.profileTitleID = responseData["userTitle"]
        self.profileTitle = responseData["userTitleDisplay"]
        self.profileBio = responseData["about"]