class Platform:
    """Represents membershipType data given back by the API in a more user-friendly format.
    Can be created any time by passing a numerical membershipType value. IE: 1, 2 or 3

    :param int enumID: A numerical membershipType value.

    type
        A shortened string of the platform name.
    typeLong
        An enlongated string of the platform name.
    membershipTypeID
        The numerical value of the platform.
    """
    def __init__(self, enumID):
        self._conversion = {
            1: ["xb", "xbox", 1], 
            2: ["ps", "playstation", 2], 
            3: [], 
            4: ["bnet", "blizzard", 4]
        }
        self.type = self._conversion[enumID][0]
        self.typeLong = self._conversion[enumID][1]
        self.membershipTypeID = self._conversion[enumID][2]
