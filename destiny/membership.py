from .userinfocard import InfoCard

class Membership:
	def __init__(self, requestData):
		self.rawRequestData = requestData
		
		self._other_memberships = self.rawRequestData["destinyMemberships"]
		self.other_memberships
		for membershipInfoCard in self.other_memberships:
			self.other_memberships.append(InfoCard(membershipInfoCard))
	
		self.membership_id = self.rawRequestData["bungieNetUser"]["membershipId"]
