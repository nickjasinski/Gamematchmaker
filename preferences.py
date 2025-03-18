from game import Game
from genre import Genre

class Preferences:
    def __init__(self, preferenceId: int, preferredGame: Game, preferredPlatform: str, multiplayerPreference: bool):
        self.preferenceId = preferenceId
        self.preferredGame = preferredGame
        self.preferredPlatform = preferredPlatform
        self.multiplayerPreference = multiplayerPreference

    def updatePreferences(self, genre: Genre, platform: str, multiplayer: bool):
        pass