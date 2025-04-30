from game import Game
from api_abstract import APIAbstract

class IGDB(APIAbstract):

    def __init__(self, game: Game):
        super().__init__(game)
    

    def queryGame(self, id: int):
        pass