class Group:
    """Represents the data of a group.

    :param dict responseData: The raw data given back by the API request.

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
    creationDate
        The date of when the group was created.
    updateDate
        The date of when the group was last updated.
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
    
    """
    def __init__(self, responseData):
        self.groupID = responseData["Response"]["detail"].get("groupId", None)
        self.groupName = responseData["Response"]["detail"].get("groupName", None)
        self.groupTypeID = responseData["Response"]["detail"].get("groupType", None)
        self.groupBio = responseData["Response"]["detail"].get("about", None)
        self.groupTags = responseData["Response"]["detail"].get("tags", None)
        self.groupMotto = responseData["Tesponse"]["detail"].get("motto", None)

        self.membershipIDCreated = responseData["Response"]["detail"].get("membershipIdCreated", None)
        self.creationDate = responseData["Response"]["detail"].get("creationDate", None)
        self.updateDate = responseData["Response"]["detail"].get("updateDate", None)
        self.memberCount = responseData["Response"]["detail"].get("memberCount", None)
        self.locale = responseData["Response"]["detail"].get("locale", None)

        self.isPublic = responseData["Response"]["detail"].get("isPublic", None)
        self.isPublicTopicAdminOnly = responseData["Response"]["detail"].get("isPublicTopicAdminOnly", None)
        self.isDefaultPostPublic =responseData["Response"]["detail"].get("isDefaultPostPublic", None)

        self.chatSecurity = responseData["Response"]["detail"].get("chatSecurity", None)
        self.chatAllowed = responseData["Response"]["detail"].get("allowChat", None)
