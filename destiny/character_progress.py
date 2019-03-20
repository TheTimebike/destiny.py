class CharacterProgress:
    def __init__(self, responseData):
        self.progressionHash = responseData["Response"]["character"]["data"]["levelProgression"]["progressionHash"]
        self.currentProgress = responseData["Response"]["character"]["data"]["levelProgression"]["currentProgress"]
        self.stepIndex = responseData["Response"]["character"]["data"]["levelProgression"]["stepIndex"]

        self.dailyProgress = responseData["Response"]["character"]["data"]["levelProgression"]["dailyProgress"]
        self.dailyLimit = responseData["Response"]["character"]["data"]["levelProgression"]["dailyLimit"]
        
        self.weeklyProgress = responseData["Response"]["character"]["data"]["levelProgression"]["weeklyProgress"]
        self.weeklyLimit = responseData["Response"]["character"]["data"]["levelProgression"]["weeklyLimit"]
        
        self.level = responseData["Response"]["character"]["data"]["levelProgression"]["level"]
        self.levelCap = responseData["Response"]["character"]["data"]["levelProgression"]["levelCap"]
        self.levelProgress = responseData["Response"]["character"]["data"]["levelProgression"]["progressToNextLevel"]
        self.nextLevel = responseData["Response"]["character"]["data"]["levelProgression"]["nextLevelAt"]