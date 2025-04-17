from typing import List
from game import Game


class Wishlist:
    def __init__(self, wishlistID: int = None, games: List[Game] = None):
        self.wishlistID = wishlistID
        self.games = games if games else []

    def addGame(self, game: Game) -> bool:
        if game not in self.games:
            self.games.append(game)
            return True
        return False

    def removeGame(self, game: Game) -> bool:
        if game in self.games:
            self.games.remove(game)
            return True
        return False
