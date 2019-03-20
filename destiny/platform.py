class Platform:
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
