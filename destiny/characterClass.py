class CharacterClass:
    def __init__(self, classType):
        self._conversion = {
            0: ["Hunter", 0],
            1: ["Warlock", 1],
            2: ["Titan", 2]
        }
        self.type = self._conversion[classType][0]
        self.characterClassTypeID = self._conversion[classType][1]