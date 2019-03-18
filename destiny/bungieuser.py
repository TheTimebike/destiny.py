class BungieUser:
	def __init__(self, requestData):
		self.rawRequestData = requestData
		
		self.membershipType = self.rawRequestData["membershipId"]
