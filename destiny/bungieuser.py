from .membership import Membership

class BungieUser:
	def __init__(self, requestData):
		self.rawRequestData = requestData
		
		self.membership = Membership(self.rawRequestData["membershipId"])
		
		self.username = self.rawRequestData["uniqueName"]
		self.display_name = self.rawRequestData["displayName"]
		self.psn_name = self.rawRequestData["psnDisplayName"]
		self.xbox_name = self.rawRequestData["xboxDisplayName"]
		self.bnet_name = self.rawRequestData["blizzardDisplayName"]
		self.fb_name = self.rawRequestData["fbDisplayName"]		
		
		self.profile_picture = self.rawRequestData["profilePicture"]
		self.profile_theme = self.rawRequestData["profileTheme"]
		self.user_title = self.rawRequestData["userTitle"]
		self.is_deleted = self.rawRequestData["isDeleted"]
		self.join_date = self.rawRequestData["firstAccess"]
		self.last_online = self.rawRequestData["lastUpdate"]

