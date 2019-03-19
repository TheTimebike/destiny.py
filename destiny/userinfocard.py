class InfoCard:
	def __init__(self, requestData):
		self.rawRequestData = requestData

		self.membershipType = self.rawRequestData["membershipType"]
		self.id = self.rawRequestData["membershipId"]
		self.display_name = self.rawRequestData["displayName"]
