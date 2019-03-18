from .userinfocard import InfoCard
from .bungieuser import Bungieuser

class Membership:
	def __init__(self, requestData):
		self.rawRequestData = requestData
		
		self._other_memberships = self.rawRequestData["destinyMemberships"]
		self.other_memberships
		for membershipInfoCard in self.other_memberships:
			self.other_memberships.append(InfoCard(membershipInfoCard))
	
		self._userData = self.rawRequestData["bungieNetUser"]
		self.user = BungieUser(self._userData)
