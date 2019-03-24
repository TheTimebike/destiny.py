class Progress:
    """This represents the progression data for a group or object.

    progressionHash
        The hash for the objective that is being progressed towards.
    currentProgress
        The current progress that has been made towards the objectives completion.
    stepIndex
        The index of the step.
    dailyProgress
        The progress that was made in the last day.
    dailyLimit
        The limit of progress that can be made in a single day.
    weeklyProgress
        The progress that was made in the last week.
    weeklyLimit
        The limit of progress that can be made in a single week.
    level
        The level of the objective.
    levelCap
        The maximum level of the objective.
    levelProgress
        The progress made towards the next level.
    nextLevel
        The progress remaining before the next level.
    """
    def __init__(self, responseData):
        self.progressionHash = responseData["progressionHash"]
        self.currentProgress = responseData["currentProgress"]
        self.stepIndex = responseData["stepIndex"]

        self.dailyProgress = responseData["dailyProgress"]
        self.dailyLimit = responseData["dailyLimit"]
        
        self.weeklyProgress = responseData["weeklyProgress"]
        self.weeklyLimit = responseData["weeklyLimit"]
        
        self.level = responseData["level"]
        self.levelCap = responseData["levelCap"]
        self.levelProgress = responseData["progressToNextLevel"]
        self.nextLevel = responseData["nextLevelAt"]