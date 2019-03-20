class CharacterRace:
    def __init__(self, raceType):
        self._conversion = {
            0: ["Human", 0],
            1: ["Awoken", 1],
            2: ["Exo", 2]
        }
        self.type = self._conversion[raceType][0]
        self.characterRaceTypeID = self._conversion[raceType][1]