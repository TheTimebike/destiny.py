class GroupFeatures:
    """Represents the features that a group or clan has.

    maxMembers
        The maximum amount of members the group can hold.
    maxMembershipsOfGroupType
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
        self.maxMembers = features.get("maximumMembers", None)
        self.maxMembershipsOfGroupTypes = features.get("maximumMembershipOfGroupType", None)
        self.capabilities = features.get("capabilities", None)
        self.membershipTypes = features.get("membershipTypes", None)

        self.invitePermissionOverride = features.get("invitePermissionOverride", None)
        self.updateCulturePermissionOverride = features.get("updateCulturePermissionOverride", None)
        self.hostGuideGamePermissionOverride = features.get("hostGuideGamePermissionOverride", None)
        self.updateBannerPermissionOverride = features.get("updateBannerPermissionOverride", None)
        self.joinLevel = features.get("membershipTypes", None)