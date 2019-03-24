class GroupType:
    """Represents groupType data given back by the API in a more user-friendly format.
    Can be created any time by passing a numerical groupType value, 0 or 1.

    :param int groupTyPe: A numerical membershipType value.

    type
        A string of the group type.
    groupTypeID
        The numerical value of the group type.
    """
    def __init__(self, groupType):
        self._conversion = {
            0: ["Group", 0], 
            1: ["Clan", 1]
        }
        self.type = self._conversion[groupType][0]
        self.groupTypeID = self._conversion[groupType][1]
        