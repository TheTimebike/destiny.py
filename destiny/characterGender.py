class CharacterGender:
    def __init__(self, genderType):
        self._conversion = {
            0: ["Male", 0],
            1: ["Female", 1]
        }
        self.type = self._conversion[genderType][0]
        self.CharacterGenderTypeID = self._conversion[genderType][1]