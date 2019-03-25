from .groups.group_features import GroupFeatures
from .progress import Progress
from .groups.group_member import GroupMember

class Group:
    """Represents the data of a group.

    groupID
        The ID of the group.
    groupName
        The name of the group.
    groupTypeID
        The ID of the group type.
    groupBio
        The group statement.
    groupTags
        The tags of the group.
    groupMotto
        The motto of the group.
    groupTheme
        The name of the group's theme.
    groupFeatures
        A GroupFeatures object containing the features of the group.
    clanProgress
        A Progress object containing the progress of the group.
    creationDate
        The date of when the group was created.
    updateDate
        The date of when the group was last updated.
    banExpireDate
        The date of when the groups ban will expire. 
    memberCount
        The amount of members in the group.
    locale
        The locale of the group.
    isPublic
        If the group set to public.
    isPublicTopicAdminOnly
        Unknown.
    isDefaultPostPublic
        Unknown.
    chatSecurity
        The security level of the group's chat.
    chatAllowed
        If the group allows its members to chat.
    avatarImageIndex
        Unknown.
    homepage
        Unknown.
    membershipOption
        Unknown.
    defaultPublicity
        Unknown.
    conversationID
        Unknown.
    enableInvitationMessagingForAdmins
        Unknown
    
    """
    def __init__(self, responseData):
        self.groupID = responseData["Response"]["detail"].get("groupId", None)
        self.groupName = responseData["Response"]["detail"].get("groupName", None)
        self.groupTypeID = responseData["Response"]["detail"].get("groupType", None)
        self.groupBio = responseData["Response"]["detail"].get("about", None)
        self.groupTags = responseData["Response"]["detail"].get("tags", None)
        self.groupMotto = responseData["Response"]["detail"].get("motto", None)
        self.groupTheme = responseData["Response"]["detail"].get("theme", None)
        self.groupFounder = GroupMember(responseData["Response"]["founder"])

        self.creationDate = responseData["Response"]["detail"].get("creationDate", None)
        self.updateDate = responseData["Response"]["detail"].get("updateDate", None)
        self.banExpireDate = responseData["Response"]["detail"].get("banExpireDate", None)

        self.membershipIDCreated = responseData["Response"]["detail"].get("membershipIdCreated", None)
        self.memberCount = responseData["Response"]["detail"].get("memberCount", None)
        self.locale = responseData["Response"]["detail"].get("locale", None)

        self.bannerUrl = responseData["Response"]["detail"].get("bannerPath", None)
        self.avatarUrl = responseData["Response"]["detail"].get("avatarPath", None)
        self.avatarImageIndex = responseData["Response"]["detail"].get("avatarImageIndex", None)

        self.homepage = responseData["Response"]["detail"].get("homepage", None)
        self.membershipOption = responseData["Response"]["detail"].get("membershipOption", None)
        self.defaultPublicity = responseData["Response"]["detail"].get("defaultPublicity", None)
        self.conversationID = responseData["Response"]["detail"].get("conversationId", None)
        self.enableInvitationMessagingForAdmins = responseData["Response"]["detail"].get("enableInvitationMessagingForAdmins", None)

        self.isPublic = responseData["Response"]["detail"].get("isPublic", None)
        self.isPublicTopicAdminOnly = responseData["Response"]["detail"].get("isPublicTopicAdminOnly", None)
        self.isDefaultPostPublic =responseData["Response"]["detail"].get("isDefaultPostPublic", None)

        self.chatSecurity = responseData["Response"]["detail"].get("chatSecurity", None)
        self.chatAllowed = responseData["Response"]["detail"].get("allowChat", None)

        self.groupFeatures = GroupFeatures(responseData["Response"]["detail"]["features"])
        if responseData["Response"]["detail"].get("clanInfo", None) != None:
            self.clanProgress = {}
            for key, value in responseData["Response"]["detail"]["clanInfo"]["d2ClanProgressions"].items():
                self.clanProgress[key] = Progress(value)
                
    async def get_members(self):
        """*This function is a coroutine*

        A coroutine that returns a list of GroupMember objects from a groupID. Returns an empty list if not found.

        :return: A list containing GroupMember objects.
        :rtype: List
        """

        if self.gatewaySession == None:
            raise NoGatewayException
        self._pageIndex = 1
        self._groupListData = await self.gatewaySession.get_request(self.BASE_ROUTE + "/GroupV2/{0}/Members/{1}/".format(self.groupID, self._pageIndex))
        self._memberObjectList = []
        while self._groupListData["Response"]["hasMore"]:
            for _groupMemberData in self._groupListData["Response"]["results"]:
                self._memberObjectList.append(GroupMember(_groupMemberData))
            self._pageIndex += 1
            self._groupListData = await self.gatewaySession.get_request(self.BASE_ROUTE + "/GroupV2/{0}/Members/{1}/".format(self.groupID, self._pageIndex))
            await asyncio.sleep(0.5)
        return self._memberObjectList
