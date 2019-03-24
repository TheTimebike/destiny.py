from ..platform import Platform

class GroupMember:
    """Represents the data of a group member.

    groupMemberType
        The type of member that the member is to the group.
    groupJoinDate
        The date when the member joined the group.
    groupID
        The ID of the group.
    isOnline
        If the member is online or offline.
    lastOnlineStatusChange
        Unknown.
    destinyIconUrl
        The url for the destiny account's icon.
    destinyMembershipTypeID
        The ID of the destiny account's membership type.
    destinyMembership
        A Platform object containing information about the members platform in a user-friendly way.
    destinyMembershipID
        The membership ID for the destiny account.
    destinyDisplayName
        The display name of the bungie profile.
    bungieIconUrl
        The url for the bungie profile's icon.
    bungieSupplimentalDisplayName
        Unknown.
    bungieMembershipTypeID
        The ID of the bungie profile's membership type.
    bungieMembershipID
        The membership ID for the bungie profile.
    bungieDisplayName
        The display name of the bungie profile.
    
    """
    def __init__(self, responseData):
        self.groupMemberType = responseData.get("memberType", None)
        self.groupJoinDate = responseData.get("joinDate", None)
        self.groupID = responseData.get("groupId", None)
        self.isOnline = responseData.get("isOnline", None)
        self.lastOnlineStatusChange = responseData.get("lastOnlineStatusChange", None)
        
        if responseData.get("destinyUserInfo", None) != None:
            self.destinyIconUrl = responseData["destinyUserInfo"].get("iconUrl", None)
            self.destinyMembershipTypeID = responseData["destinyUserInfo"].get("membershipType", None)
            self.destinyMembership = Platform(self.destinyMembershipTypeID)
            self.destinyMembershipID = responseData["destinyUserInfo"].get("membershipId", None)
            self.destinyDisplayName = responseData["destinyUserInfo"].get("displayName", None)

        if responseData.get("bungieNetUserInfo", None) != None:
            self.bungieIconUrl = responseData["bungieNetUserInfo"].get("iconUrl", None)
            self.bungieSupplimentalDisplayName = responseData["bungieNetUserInfo"].get("supplimentalDisplayName", None)
            self.bungieMembershipTypeID = responseData["bungieNetUserInfo"].get("membershipType", None)
            self.bungieMembershipID = responseData["bungieNetUserInfo"].get("membershipId", None)
            self.bungieDisplayName = responseData["bungieNetUserInfo"].get("displayName", None)
