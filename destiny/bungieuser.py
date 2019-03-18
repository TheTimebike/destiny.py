class BungieUser:
	def __init__(self, requestData):
		self.rawRequestData = requestData
		
		self.membershipID = self.rawRequestData["membershipId"]
