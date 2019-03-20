class Emblem:
    def __init__(self, responseData):
        self.emblemUrl = "https://www.bungie.net" + responseData["Response"]["character"]["data"]["emblemPath"]
        self.emblemBackgroundurl = self.emblemUrl = "https://www.bungie.net" + responseData["Response"]["character"]["data"]["emblemBackgroundPath"]
        self.emblemhash = responseData["Response"]["character"]["data"]["emblemHash"]
        self.emblemColours = responseData["Response"]["character"]["data"]["emblemColor"]
        self.emblemColors = self.emblemColours