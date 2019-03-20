from .platform import Platform
from .characterGender import CharacterGender
from .characterRace import CharacterRace
from .characterClass import CharacterClass

class Character:
    def __init__(self, responseData):
        self.membershipID = responseData["Response"]["character"]["data"]["membershipId"]
        self.characterID = responseData["Response"]["character"]["data"]["characterId"]

        self.membershipType = Platform(responseData["Response"]["character"]["data"]["membershipType"])
        self.characterGender = CharacterGender(responseData["Response"]["character"]["data"]["genderType"])
        self.characterRace = CharacterRace(responseData["Response"]["character"]["data"]["raceType"])
        self.characterClass = CharacterClass(responseData["Response"]["character"]["data"]["classType"])

        self.dateLastPlayed = responseData["Response"]["character"]["data"]["dateLastPlayed"]

        self.lightLevel = responseData["Response"]["character"]["data"]["stats"]["1935470627"]
        self.mobilityLevel = responseData["Response"]["character"]["data"]["stats"]["2996146975"]
        self.resilienceLevel = responseData["Response"]["character"]["data"]["stats"]["392767087"]
        self.recoveryLevel = responseData["Response"]["character"]["data"]["stats"]["1943323491"]