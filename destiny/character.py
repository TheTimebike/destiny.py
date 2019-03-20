from .platform import Platform
from .character_gender import CharacterGender
from .character_race import CharacterRace
from .character_class import CharacterClass
from .emblem import Emblem
from .character_progress import CharacterProgress

class Character:
    def __init__(self, responseData):
        self.membershipID = responseData["Response"]["character"]["data"]["membershipId"]
        self.characterID = responseData["Response"]["character"]["data"]["characterId"]

        self.membershipType = Platform(responseData["Response"]["character"]["data"]["membershipType"])
        self.characterGender = CharacterGender(responseData["Response"]["character"]["data"]["genderType"])
        self.characterRace = CharacterRace(responseData["Response"]["character"]["data"]["raceType"])
        self.characterClass = CharacterClass(responseData["Response"]["character"]["data"]["classType"])

        self.emblem = Emblem(responseData)
        self.characterProgress = CharacterProgress(responseData)

        self.dateLastPlayed = responseData["Response"]["character"]["data"]["dateLastPlayed"]

        self.lightLevel = responseData["Response"]["character"]["data"]["stats"]["1935470627"]
        self.mobilityLevel = responseData["Response"]["character"]["data"]["stats"]["2996146975"]
        self.resilienceLevel = responseData["Response"]["character"]["data"]["stats"]["392767087"]
        self.recoveryLevel = responseData["Response"]["character"]["data"]["stats"]["1943323491"]