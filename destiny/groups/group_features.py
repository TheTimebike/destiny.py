class GroupFeatures:
    """Represents the features that a group or clan has.

    maxMembers
        The maximum amount of members the group can hold.
    maxMembershipOfGroupTypes
        Unknown.
    capabilities
        Unknown.
    membershipTypes
        Unknown.
    invitePermissionOverride
        If members can invite other users to the group.
    updateCulturePermissionOverride
        If members can update the group culture.
    hostGuideGamePermissionOverride
        If members can host guided games.
    updateBannerPermissionOverride
        If members can edit the group banner.
    joinLevel
        The permission level that members hold when they join.

    """
    def __init__(self, features):
        self.maxMembers = features["maximumMembers"]
        self.maxMembershipOfGroupTypes = features["maximumMembershipOfGroupTypes"]
        self.capabilities = features["capabilities"]
        self.membershipTypes = features["membershipTypes"]

        self.invitePermissionOverride = features["invitePermissionOverride"]
        self.updateCulturePermissionOverride = features["updateCulturePermissionOverride"]
        self.hostGuideGamePermissionOverride = features["hostGuideGamePermissionOverride"]
        self.updateBannerPermissionOverride = features["updateBannerPermissionOverride"]
        self.joinLevel = features["membershipTypes"]