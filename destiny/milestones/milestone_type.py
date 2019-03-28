class MilestoneType:
	def __init__(self, milestoneType):
		self._conversion = {
            0: ["Unknown", 0],
			1: ["Tutorial", 1],
            2: ["One-Time", 2],
			3: ["Weekly", 3],
			4: ["Daily", 4].
			5: ["Special", 5]
        }
        self.type = self._conversion[milestoneType][0]
        self.milestoneTypeID = self._conversion[milestoneType][1]
