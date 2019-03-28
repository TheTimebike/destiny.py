from .milestones.milestone_type import MilestoneType

class Milestone:
	def __init__(self, client, milestoneData):
		_responseData = await client.decode_hash(milestoneData["milestoneHash"] "DestinyMilestoneDefinition", "en")
		self.milestoneHash = milestoneHash
		if self.displayName = _responseData.get("displayProperties", None) != None:
			self.displayName = _responseData["displayProperties"].get("name", None)
			self.description = _responseData["displayProperties"].get("description", None)
			self.hasIcon = _responseData["displayProperties"].get("hasIcon", None)
			self.icon = _responseData["displayProperties"].get("icon", None)
		self.milestoneType = MilestoneType(milestoneData["milestoneType"])
