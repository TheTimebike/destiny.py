from .milestones.milestone_type import MilestoneType
import json

class Milestone:
	def __init__(self, milestoneData, responseData):
		print(milestoneData)
		with open("milestonedump.json", "w+") as out:
			json.dump(responseData, out, indent=4)
		print(responseData)
		self._responseData = responseData
		if self._responseData.get("displayProperties", None) != None:
			self.displayName = self._responseData["displayProperties"].get("name", None)
			self.description = self._responseData["displayProperties"].get("description", None)
			self.hasIcon = self._responseData["displayProperties"].get("hasIcon", None)
			self.icon = self._responseData["displayProperties"].get("icon", None)
		self.milestoneType = MilestoneType(responseData["milestoneType"])
