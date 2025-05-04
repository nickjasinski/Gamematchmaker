from typing import List
from game import Game


class Wishlist:
    def __init__(self, games: List[str] = None):
        self.games = games if games else []

    
